/* empty css             *//* empty css                     */import{_ as E,r as m,h as M,c as r,a as t,b as c,w as d,u as y,F as g,i as k,E as b,o as u,e as _,t as v,f as A,g as B}from"./index-CU6pVD8_.js";import{i as D}from"./request-C08gkA4w.js";const I={class:"Header"},N={style:{"background-color":"#f5f7fb","padding-top":"30px"}},V={class:"header"},F={class:"list"},G=["onClick"],H=["src"],L={class:"right"},P={class:"title"},T={class:"risk_value"},j={__name:"index",setup(q){const i=A();var f=m([]),h=m("3");const x=e=>{console.log(e),h.value=e,e==1?i.push("/Main"):e==2?i.push("/Categories"):e==3?i.push("/Application"):e==4&&i.push("/Sensors")},w=async()=>{try{const e=await D.get("/api/get_all_apps");console.log(e.data);const s=e.data.reduce(async(o,a)=>{const n=await o,p=n.find(l=>l.type===a.category);return p?p.list.push(a):n.push({type:a.category,list:[a]}),n},Promise.resolve([]));f.value=await s,console.log(f.value)}catch{}},S=e=>{i.push({path:"/appDetail",query:{searchText:e.id,type:"id",page:"3"}})};return M(()=>{w()}),(e,s)=>{const o=B,a=b;return u(),r(g,null,[t("div",I,[s[4]||(s[4]=t("div",{class:"logo"},null,-1)),c(a,{"default-active":y(h),class:"el-menu-demo",mode:"horizontal",onSelect:x,style:{width:"80%"}},{default:d(()=>[c(o,{index:"1"},{default:d(()=>s[0]||(s[0]=[_("Home")])),_:1}),c(o,{index:"2"},{default:d(()=>s[1]||(s[1]=[_("Categories")])),_:1}),c(o,{index:"3"},{default:d(()=>s[2]||(s[2]=[_("Applications")])),_:1}),c(o,{index:"4"},{default:d(()=>s[3]||(s[3]=[_("Sensors/Permission Data")])),_:1})]),_:1},8,["default-active"])]),t("div",N,[(u(!0),r(g,null,k(y(f),(n,p)=>(u(),r("div",{class:"Game",key:p},[t("div",V,v(n.type),1),t("div",F,[(u(!0),r(g,null,k(n.list,(l,C)=>(u(),r("div",{class:"list_one",key:C,onClick:z=>S(l)},[t("img",{src:"http://47.90.217.63:8000/logo/"+l.id+".jpg",alt:""},null,8,H),t("div",L,[t("div",P,v(l.new_names),1),t("div",T,v(l.risk_score),1)])],8,G))),128))])]))),128))])],64)}}},O=E(j,[["__scopeId","data-v-2883811d"]]);export{O as default};