/* empty css             *//* empty css                                                              */import{i as w}from"./request-C08gkA4w.js";import{_ as k,r as _,h as V,u as i,c,a as o,F as E,i as S,b as m,j as C,w as D,d as I,k as T,l as U,o as p,t as g,e as b,f as j}from"./index-DYh4OMqa.js";const A={key:0},B={class:"appList"},N=["onClick"],z=["src"],L={class:"wenzi"},P={class:"text"},q={class:"risk_number"},F={class:"search"},R={__name:"index",setup($){const d=j(),h=()=>{n.value&&d.push({path:"/appDetail",query:{searchText:n.value,type:"name"}})},f=s=>{d.push({path:"/appDetail",query:{searchText:s.id,type:"id"}})};var r=_([]),n=_(null);const x=()=>{w({method:"get",url:"/api/homepage_rand"}).then(async s=>{console.log(s,"##########");const e=await Promise.all(s.data.map(async t=>(t.imgUrl=await y(t.id),t)));r.value=e})},y=async s=>{const e=`http://47.90.217.63:8000/logo/${s}.jpg`,t=`http://47.90.217.63:8000/logo/${s}.png`,l=await u(e),a=await u(t);return l?e:a?t:"default-image.png"},u=s=>new Promise(e=>{const t=new Image;t.onload=()=>e(!0),t.onerror=()=>e(!1),t.src=s});return V(async()=>{console.log("!!!!!!!!!!"),await x()}),(s,e)=>{const t=T,l=U;return i(r).length?(p(),c("div",A,[e[2]||(e[2]=o("h1",null,"Sensor Detection Tool",-1)),o("div",B,[(p(!0),c(E,null,S(i(r),(a,v)=>(p(),c("div",{class:"one",key:v,onClick:H=>f(a)},[o("img",{src:a.imgUrl,alt:""},null,8,z),o("div",L,[o("div",P,g(a.new_names),1),o("div",q,g(a.risk_score),1)])],8,N))),128))]),o("div",F,[m(t,{modelValue:i(n),"onUpdate:modelValue":e[0]||(e[0]=a=>C(n)?n.value=a:n=a),size:"large",placeholder:"Please input",style:{width:"850px"}},null,8,["modelValue"]),m(l,{style:{"margin-left":"5px"},type:"primary",size:"large",onClick:h},{default:D(()=>e[1]||(e[1]=[b("Search")])),_:1})])])):I("",!0)}}},O=k(R,[["__scopeId","data-v-cefbd048"]]);export{O as default};
