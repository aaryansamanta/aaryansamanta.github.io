'use strict';
// Isolated V14 decision explorer. The full official Kaggle engine and replay-derived
// 719-turn route remain in the Python notebook, not in this static browser build.
const PARAMS={
 STRAWBERRY:{base:120,T:100,below:'sqrt',bt:.70,above:'linear',at:1.60},
 MELON:{base:250,T:300,below:'log',bt:.20,above:'sq',at:3.60},
 MILK:{base:160,T:122,below:'sqrt',bt:.60,above:'linear',at:1.60},
 WOOL:{base:200,T:105,below:'log',bt:.20,above:'sq',at:3.20}
};
const $=id=>document.getElementById(id);
const num=id=>Math.max(0,Number($(id).value)||0);
function shape(type,x,T){const u=x/T;switch(type){case 'sqrt':return Math.sqrt(x);case 'sq':return x*x;case 'linear':return x;case 'log':return Math.log1p(x);case 'log10':return Math.log10(1+x);case 'hinge':return u+8*Math.max(0,u-1)**2;default:return x;}}
function price(product,inventory){const p=PARAMS[product];const x=Math.abs(inventory-10000);if(!x)return p.base;const scarce=inventory<10000;const fn=scarce?p.below:p.above,target=scarce?p.bt:p.at;const amp=target*p.base/shape(fn,p.T,p.T);return Math.max(1,Math.round(p.base+(scarce?1:-1)*amp*shape(fn,x,p.T)));}
function setBar(id,n,max){$(id).style.width=`${Math.max(0,Math.min(100,n/max*100))}%`;$(id+'n').textContent=n;}
function execute(){
 const product=$('product').value,step=Math.floor(num('step')),distance=Math.floor(num('distance')),
 next=Math.floor(num('next')),shed=Math.floor(num('shed')),orders=Math.floor(num('orders')),
 inventory=Math.floor(num('inventory')),existing=Math.floor(num('existing')),pending=$('pending').value==='yes';
 const remaining=Math.max(0,shed-existing),currentPrice=price(product,inventory),threshold=PARAMS[product].base*0.02364641;
 const checks=[
 ['Season window',step>=120&&step<680,`120 ≤ ${step} < 680`],
 ['No previous shift awaiting repayment',!pending,pending?'Pending repayment exists':'No pending shift'],
 ['Near-clone public farm signature',distance<=6,`distance ${distance} ≤ 6`],
 ['Market order capacity',orders<10,`${orders} of 10 slots occupied`],
 ['Future SELL minimum',next>=4,`${next} units; minimum 4`],
 ['Market price floor gate',currentPrice>=threshold,`${currentPrice} ≥ ${threshold.toFixed(2)} coins`],
 ['Stock after current SELL orders',remaining>0,`${shed} − ${existing} = ${remaining} units`]
 ];
 const passed=checks.every(c=>c[1]);
 const fractionTarget=Math.max(1,Math.round(next*2.34358964641));
 const shift=passed?Math.min(remaining,next,30,fractionTarget):0,repay=next-shift;
 const max=Math.max(40,next,shift)*1.12;
 setBar('base0',0,max);setBar('base1',next,max);setBar('v140',shift,max);setBar('v141',repay,max);
 $('shift').textContent=shift;$('repay').textContent=repay;
 $('gate').textContent=shift>0?'ACTIVE':'BLOCKED';$('gate').style.color=shift>0?'#b5e4ac':'#edb08e';
 $('reason').textContent=shift>0?'V14 preemption gates passed':checks.filter(c=>!c[1]).map(c=>c[0]).join(' · ');
 $('runstate').textContent=shift>0?'ORDER SHIFT EXECUTED':'BASELINE RETAINED';
 $('conservation').textContent=`Shifted future SELL: ${shift} now + ${repay} next = ${next} ${product.toLowerCase()} units`;
 const trace=[
 `Input represents one premium product in the next-turn baseline market orders; public-farm clone distance is supplied as a scenario input.`,
 ...checks.map(c=>`${c[1]?'✓':'×'} ${c[0]} — ${c[2]}`),
 `V14 target = min(remaining stock ${remaining}, future SELL ${next}, cap 30, max(1, round(${next} × 2.34358964641)) = ${fractionTarget}).`,
 shift>0?`Append SELL ${product} ${shift} after the existing ranked market orders; set due_step = ${step+1}.`:'No preemption SELL appended; keep baseline market orders.',
 shift>0?`At turn ${step+1}, _repay_shift subtracts up to ${shift} from matching SELL orders (possibly across multiple orders).`:'No repayment scheduled because no shift was appended.',
 `Price model: inventory ${inventory.toLocaleString()} → ${currentPrice} coins; V14 compares against base price × 0.02364641.`,
 `The complete agent also executes route actions, weed repair, market SELL ranking, and terminal liquidation; those steps are not executed in this focused browser experiment.`
 ];
 $('trace').replaceChildren(...trace.map(t=>{const li=document.createElement('li');li.textContent=t;return li;}));
 draw();$('run').textContent='Run again ↗';
}
function draw(){const canvas=$('chart'),ctx=canvas.getContext('2d'),w=canvas.width,h=canvas.height;ctx.clearRect(0,0,w,h);const product=$('product').value,p=PARAMS[product],selected=Math.floor(num('inventory'));$('resource').textContent=product;$('price').textContent=price(product,selected).toLocaleString();const left=58,right=20,top=18,bottom=40;const xMin=9500,xMax=10500;const values=Array.from({length:121},(_,i)=>price(product,xMin+(xMax-xMin)*i/120));const yMax=Math.max(p.base*1.6,...values)*1.04;const X=v=>left+(v-xMin)/(xMax-xMin)*(w-left-right),Y=v=>h-bottom-v/yMax*(h-top-bottom);
ctx.font='12px Verdana';ctx.textAlign='right';for(let i=0;i<=4;i++){const v=yMax*i/4,y=Y(v);ctx.strokeStyle='#34533f';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(left,y);ctx.lineTo(w-right,y);ctx.stroke();ctx.fillStyle='#8da995';ctx.fillText(Math.round(v),left-9,y+4);}ctx.textAlign='center';for(let i=0;i<=4;i++){let v=xMin+(xMax-xMin)*i/4;ctx.fillStyle='#8da995';ctx.fillText(v.toLocaleString(),X(v),h-14);}ctx.strokeStyle='#d8aa6f';ctx.lineWidth=4;ctx.lineJoin='round';ctx.beginPath();values.forEach((v,i)=>{const x=X(xMin+(xMax-xMin)*i/120),y=Y(v);i?ctx.lineTo(x,y):ctx.moveTo(x,y)});ctx.stroke();if(selected>=xMin&&selected<=xMax){const x=X(selected),y=Y(price(product,selected));ctx.strokeStyle='#a2d9aa';ctx.setLineDash([5,5]);ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(x,top);ctx.lineTo(x,h-bottom);ctx.stroke();ctx.setLineDash([]);ctx.fillStyle='#f4ce91';ctx.beginPath();ctx.arc(x,y,7,0,Math.PI*2);ctx.fill();}}
function restore(){const defaults={product:'STRAWBERRY',step:320,distance:3,next:48,shed:24,orders:5,inventory:9980,existing:0,pending:'no'};Object.entries(defaults).forEach(([k,v])=>$(k).value=v);$('run').innerHTML='Run agent decision <span>↗</span>';$('shift').textContent='—';$('repay').textContent='—';$('gate').textContent='READY';$('gate').style.color='';$('reason').textContent='Press Run agent decision';$('runstate').textContent='AWAITING EXECUTION';$('trace').innerHTML='<li>Configure the market and click <strong>Run agent decision</strong>.</li>';setBar('base0',0,60);setBar('base1',48,60);setBar('v140',0,60);setBar('v141',48,60);$('conservation').textContent='Quantity conservation: 0 + 48 = 48';draw();}
$('run').addEventListener('click',execute);$('reset').addEventListener('click',restore);$('product').addEventListener('change',draw);$('inventory').addEventListener('input',draw);document.querySelectorAll('[data-preset]').forEach(b=>b.addEventListener('click',()=>{restore();if(b.dataset.preset==='far')$('distance').value=12;if(b.dataset.preset==='late')$('step').value=710;execute();}));restore();
