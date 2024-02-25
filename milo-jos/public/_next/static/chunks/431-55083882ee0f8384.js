(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[431],{947:function(e,t,n){"use strict";n.d(t,{Vq:function(){return el}});var r=n(7294),a=n(3967),o=n.n(a),i=n(7462),l=n(6206),c=n(8771),u=n(5360),s=n(1276),d=n(7342),f=n(8083),p=n(5420),v=n(2651),m=n(9115),g=n(5320),h=n(7552),b=n(6223),y=n(3541),$=n(8426);let E="Dialog",[w,S]=(0,u.b)(E),[C,R]=w(E),_=(0,r.forwardRef)((e,t)=>{let{__scopeDialog:n,...a}=e,o=R("DialogTrigger",n),u=(0,c.e)(t,o.triggerRef);return(0,r.createElement)(g.WV.button,(0,i.Z)({type:"button","aria-haspopup":"dialog","aria-expanded":o.open,"aria-controls":o.contentId,"data-state":$5d3850c4d0b4e6c7$var$getState(o.open)},a,{ref:u,onClick:(0,l.M)(e.onClick,o.onOpenToggle)}))}),T="DialogPortal",[D,k]=w(T,{forceMount:void 0}),M="DialogOverlay",x=(0,r.forwardRef)((e,t)=>{let n=k(M,e.__scopeDialog),{forceMount:a=n.forceMount,...o}=e,l=R(M,e.__scopeDialog);return l.modal?(0,r.createElement)(m.z,{present:a||l.open},(0,r.createElement)(O,(0,i.Z)({},o,{ref:t}))):null}),O=(0,r.forwardRef)((e,t)=>{let{__scopeDialog:n,...a}=e,o=R(M,n);return(0,r.createElement)(b.Z,{as:$.g7,allowPinchZoom:!0,shards:[o.contentRef]},(0,r.createElement)(g.WV.div,(0,i.Z)({"data-state":$5d3850c4d0b4e6c7$var$getState(o.open)},a,{ref:t,style:{pointerEvents:"auto",...a.style}})))}),A="DialogContent",F=(0,r.forwardRef)((e,t)=>{let n=k(A,e.__scopeDialog),{forceMount:a=n.forceMount,...o}=e,l=R(A,e.__scopeDialog);return(0,r.createElement)(m.z,{present:a||l.open},l.modal?(0,r.createElement)(N,(0,i.Z)({},o,{ref:t})):(0,r.createElement)(I,(0,i.Z)({},o,{ref:t})))}),N=(0,r.forwardRef)((e,t)=>{let n=R(A,e.__scopeDialog),a=(0,r.useRef)(null),o=(0,c.e)(t,n.contentRef,a);return(0,r.useEffect)(()=>{let e=a.current;if(e)return(0,y.Ry)(e)},[]),(0,r.createElement)(L,(0,i.Z)({},e,{ref:o,trapFocus:n.open,disableOutsidePointerEvents:!0,onCloseAutoFocus:(0,l.M)(e.onCloseAutoFocus,e=>{var t;e.preventDefault(),null===(t=n.triggerRef.current)||void 0===t||t.focus()}),onPointerDownOutside:(0,l.M)(e.onPointerDownOutside,e=>{let t=e.detail.originalEvent,n=0===t.button&&!0===t.ctrlKey,r=2===t.button||n;r&&e.preventDefault()}),onFocusOutside:(0,l.M)(e.onFocusOutside,e=>e.preventDefault())}))}),I=(0,r.forwardRef)((e,t)=>{let n=R(A,e.__scopeDialog),a=(0,r.useRef)(!1),o=(0,r.useRef)(!1);return(0,r.createElement)(L,(0,i.Z)({},e,{ref:t,trapFocus:!1,disableOutsidePointerEvents:!1,onCloseAutoFocus:t=>{var r,i;null===(r=e.onCloseAutoFocus)||void 0===r||r.call(e,t),t.defaultPrevented||(a.current||null===(i=n.triggerRef.current)||void 0===i||i.focus(),t.preventDefault()),a.current=!1,o.current=!1},onInteractOutside:t=>{var r,i;null===(r=e.onInteractOutside)||void 0===r||r.call(e,t),t.defaultPrevented||(a.current=!0,"pointerdown"!==t.detail.originalEvent.type||(o.current=!0));let l=t.target,c=null===(i=n.triggerRef.current)||void 0===i?void 0:i.contains(l);c&&t.preventDefault(),"focusin"===t.detail.originalEvent.type&&o.current&&t.preventDefault()}}))}),L=(0,r.forwardRef)((e,t)=>{let{__scopeDialog:n,trapFocus:a,onOpenAutoFocus:o,onCloseAutoFocus:l,...u}=e,s=R(A,n),d=(0,r.useRef)(null),v=(0,c.e)(t,d);return(0,h.EW)(),(0,r.createElement)(r.Fragment,null,(0,r.createElement)(p.M,{asChild:!0,loop:!0,trapped:a,onMountAutoFocus:o,onUnmountAutoFocus:l},(0,r.createElement)(f.XB,(0,i.Z)({role:"dialog",id:s.contentId,"aria-describedby":s.descriptionId,"aria-labelledby":s.titleId,"data-state":$5d3850c4d0b4e6c7$var$getState(s.open)},u,{ref:v,onDismiss:()=>s.onOpenChange(!1)}))),!1)}),P="DialogTitle",W=(0,r.forwardRef)((e,t)=>{let{__scopeDialog:n,...a}=e,o=R(P,n);return(0,r.createElement)(g.WV.h2,(0,i.Z)({id:o.titleId},a,{ref:t}))}),B=(0,r.forwardRef)((e,t)=>{let{__scopeDialog:n,...a}=e,o=R("DialogDescription",n);return(0,r.createElement)(g.WV.p,(0,i.Z)({id:o.descriptionId},a,{ref:t}))}),Z=(0,r.forwardRef)((e,t)=>{let{__scopeDialog:n,...a}=e,o=R("DialogClose",n);return(0,r.createElement)(g.WV.button,(0,i.Z)({type:"button"},a,{ref:t,onClick:(0,l.M)(e.onClick,()=>o.onOpenChange(!1))}))});function $5d3850c4d0b4e6c7$var$getState(e){return e?"open":"closed"}let[Y,j]=(0,u.k)("DialogTitleWarning",{contentName:A,titleName:P,docsSlug:"dialog"}),$5d3850c4d0b4e6c7$export$be92b6f5f03c0fe9=e=>{let{__scopeDialog:t,children:n,open:a,defaultOpen:o,onOpenChange:i,modal:l=!0}=e,c=(0,r.useRef)(null),u=(0,r.useRef)(null),[f=!1,p]=(0,d.T)({prop:a,defaultProp:o,onChange:i});return(0,r.createElement)(C,{scope:t,triggerRef:c,contentRef:u,contentId:(0,s.M)(),titleId:(0,s.M)(),descriptionId:(0,s.M)(),open:f,onOpenChange:p,onOpenToggle:(0,r.useCallback)(()=>p(e=>!e),[p]),modal:l},n)},$5d3850c4d0b4e6c7$export$602eac185826482c=e=>{let{__scopeDialog:t,forceMount:n,children:a,container:o}=e,i=R(T,t);return(0,r.createElement)(D,{scope:t,forceMount:n},r.Children.map(a,e=>(0,r.createElement)(m.z,{present:n||i.open},(0,r.createElement)(v.h,{asChild:!0,container:o},e))))},z={size:{type:"enum",values:["1","2","3","4"],default:"3",responsive:!0}};var X=n(6776),H=n(3416),V=n(617),K=n(7361),G=n(8291),q=n(6679);H.b.values;let U={size:{type:"enum",values:["1","2","3","4","5","6","7","8","9"],default:"6",responsive:!0},weight:{...H.b,default:"bold"},align:V.L,trim:K.a,color:G.m,highContrast:q.B};var Q=n(3843);let J=r.forwardRef((e,t)=>{let{rest:n,...a}=(0,Q.FY)(e),{children:i,className:l,asChild:c=!1,as:u="h1",size:s=U.size.default,weight:d=U.weight.default,align:f=U.align.default,trim:p=U.trim.default,color:v=U.color.default,highContrast:m=U.highContrast.default,...g}=n;return r.createElement($.g7,{"data-accent-color":v,...g,ref:t,className:o()("rt-Heading",l,(0,X.g)(s,"rt-r-size"),(0,X.g)(d,"rt-r-weight"),(0,X.g)(f,"rt-r-ta"),(0,X.g)(p,"rt-r-lt"),{"rt-high-contrast":m},(0,Q.we)(a))},c?i:r.createElement(u,null,i))});J.displayName="Heading";var ee=n(6445),et=n(5722);let DialogRoot=e=>r.createElement($5d3850c4d0b4e6c7$export$be92b6f5f03c0fe9,{...e,modal:!0});DialogRoot.displayName="DialogRoot";let en=r.forwardRef((e,t)=>r.createElement(_,{...e,ref:t,asChild:!0}));en.displayName="DialogTrigger";let er=r.forwardRef((e,t)=>{let{className:n,forceMount:a,container:i,size:l=z.size.default,...c}=e;return r.createElement($5d3850c4d0b4e6c7$export$602eac185826482c,{container:i,forceMount:a},r.createElement(et.Q2,{asChild:!0},r.createElement(x,{className:"rt-DialogOverlay"},r.createElement(F,{...c,ref:t,className:o()("rt-DialogContent",n,(0,X.g)(l,"rt-r-size"))}))))});er.displayName="DialogContent";let ea=r.forwardRef((e,t)=>r.createElement(W,{asChild:!0},r.createElement(J,{size:"5",mb:"3",trim:"start",...e,ref:t})));ea.displayName="DialogTitle";let eo=r.forwardRef((e,t)=>r.createElement(B,{asChild:!0},r.createElement(ee.x,{as:"p",size:"3",...e,ref:t})));eo.displayName="DialogDescription";let ei=r.forwardRef((e,t)=>r.createElement(Z,{...e,ref:t,asChild:!0}));ei.displayName="DialogClose";let el=Object.assign({},{Root:DialogRoot,Trigger:en,Content:er,Title:ea,Description:eo,Close:ei})},6445:function(e,t,n){"use strict";n.d(t,{x:function(){return s}});var r=n(7294),a=n(3967),o=n.n(a),i=n(8426),l=n(3356),c=n(3843),u=n(6776);let s=r.forwardRef((e,t)=>{let{rest:n,...a}=(0,c.FY)(e),{children:s,className:d,asChild:f=!1,as:p="span",size:v=l.S.size.default,weight:m=l.S.weight.default,align:g=l.S.align.default,trim:h=l.S.trim.default,color:b=l.S.color.default,highContrast:y=l.S.highContrast.default,...$}=n;return r.createElement(i.g7,{"data-accent-color":b,...$,ref:t,className:o()("rt-Text",d,(0,u.g)(v,"rt-r-size"),(0,u.g)(m,"rt-r-weight"),(0,u.g)(g,"rt-r-ta"),(0,u.g)(h,"rt-r-lt"),{"rt-high-contrast":y},(0,c.we)(a))},f?s:r.createElement(p,null,s))});s.displayName="Text"},3356:function(e,t,n){"use strict";n.d(t,{S:function(){return c}});var r=n(3416),a=n(617),o=n(7361),i=n(8291),l=n(6679);let c={size:{type:"enum",values:["1","2","3","4","5","6","7","8","9"],default:void 0,responsive:!0},weight:r.b,align:a.L,trim:o.a,color:i.m,highContrast:l.B}},6776:function(e,t,n){"use strict";function withBreakpoints(e,t="",n){var r,a,o,i;let l=[];if("object"==typeof e){for(let o of Object.keys(e))if(o in e){let i=null===(r=e[o])||void 0===r?void 0:r.toString(),c=null==i?void 0:i.startsWith("-"),u=""===t?"":"-",s=c?`-${t}`:t,d=c?null==i?void 0:i.substring(1):i;if(void 0===d)continue;let f=null!==(a=null==n?void 0:n[d])&&void 0!==a?a:d,p="initial"===o?`${s}${u}${f}`:`${o}:${s}${u}${f}`;l.push(p)}}if("string"==typeof e){let r=e.startsWith("-"),a=""===t?"":"-",i=r?`-${t}`:t,c=r?e.substring(1):e,u=null!==(o=null==n?void 0:n[c])&&void 0!==o?o:c;l.push(`${i}${a}${u}`)}if("boolean"==typeof e){let r=""===t?"":"-",a=e.toString(),o=null!==(i=null==n?void 0:n[a])&&void 0!==i?i:a;l.push(`${t}${r}${o}`)}return l.join(" ")}n.d(t,{g:function(){return withBreakpoints}})},8291:function(e,t,n){"use strict";n.d(t,{m:function(){return a}});var r=n(269);let a={type:"enum",values:r.yT.accentColor.values,default:void 0}},6679:function(e,t,n){"use strict";n.d(t,{B:function(){return r}});let r={type:"boolean",default:void 0}},7361:function(e,t,n){"use strict";n.d(t,{a:function(){return r}});let r={type:"enum",values:["normal","start","end","both"],default:void 0,responsive:!0}},3843:function(e,t,n){"use strict";n.d(t,{FY:function(){return extractMarginProps},we:function(){return withMarginProps}});var r=n(6776);let a=["auto","0","1","2","3","4","5","6","7","8","9","-1","-2","-3","-4","-5","-6","-7","-8","-9"],o={m:{type:"enum",values:a,default:void 0,responsive:!0},mx:{type:"enum",values:a,default:void 0,responsive:!0},my:{type:"enum",values:a,default:void 0,responsive:!0},mt:{type:"enum",values:a,default:void 0,responsive:!0},mr:{type:"enum",values:a,default:void 0,responsive:!0},mb:{type:"enum",values:a,default:void 0,responsive:!0},ml:{type:"enum",values:a,default:void 0,responsive:!0}};function extractMarginProps(e){let{m:t=o.m.default,mx:n=o.mx.default,my:r=o.my.default,mt:a=o.mt.default,mr:i=o.mr.default,mb:l=o.mb.default,ml:c=o.ml.default,...u}=e;return{m:t,mx:n,my:r,mt:a,mr:i,mb:l,ml:c,rest:u}}function withMarginProps(e){return[(0,r.g)(e.m,"rt-r-m"),(0,r.g)(e.mx,"rt-r-mx"),(0,r.g)(e.my,"rt-r-my"),(0,r.g)(e.mt,"rt-r-mt"),(0,r.g)(e.mr,"rt-r-mr"),(0,r.g)(e.mb,"rt-r-mb"),(0,r.g)(e.ml,"rt-r-ml")].filter(Boolean).join(" ")}},617:function(e,t,n){"use strict";n.d(t,{L:function(){return r}});let r={type:"enum",values:["left","center","right"],default:void 0,responsive:!0}},3416:function(e,t,n){"use strict";n.d(t,{b:function(){return r}});let r={type:"enum",values:["light","regular","medium","bold"],default:void 0,responsive:!0}},3541:function(e,t,n){"use strict";n.d(t,{Ry:function(){return hideOthers}});var r=new WeakMap,a=new WeakMap,o={},i=0,unwrapHost=function(e){return e&&(e.host||unwrapHost(e.parentNode))},applyAttributeToOthers=function(e,t,n,l){var c=(Array.isArray(e)?e:[e]).map(function(e){if(t.contains(e))return e;var n=unwrapHost(e);return n&&t.contains(n)?n:(console.error("aria-hidden",e,"in not contained inside",t,". Doing nothing"),null)}).filter(function(e){return!!e});o[n]||(o[n]=new WeakMap);var u=o[n],s=[],d=new Set,f=new Set(c),keep=function(e){!e||d.has(e)||(d.add(e),keep(e.parentNode))};c.forEach(keep);var deep=function(e){!e||f.has(e)||Array.prototype.forEach.call(e.children,function(e){if(d.has(e))deep(e);else{var t=e.getAttribute(l),o=null!==t&&"false"!==t,i=(r.get(e)||0)+1,c=(u.get(e)||0)+1;r.set(e,i),u.set(e,c),s.push(e),1===i&&o&&a.set(e,!0),1===c&&e.setAttribute(n,"true"),o||e.setAttribute(l,"true")}})};return deep(t),d.clear(),i++,function(){s.forEach(function(e){var t=r.get(e)-1,o=u.get(e)-1;r.set(e,t),u.set(e,o),t||(a.has(e)||e.removeAttribute(l),a.delete(e)),o||e.removeAttribute(n)}),--i||(r=new WeakMap,r=new WeakMap,a=new WeakMap,o={})}},hideOthers=function(e,t,n){void 0===n&&(n="data-aria-hidden");var r=Array.from(Array.isArray(e)?e:[e]),a=t||("undefined"==typeof document?null:(Array.isArray(e)?e[0]:e).ownerDocument.body);return a?(r.push.apply(r,Array.from(a.querySelectorAll("[aria-live]"))),applyAttributeToOthers(r,a,n,"aria-hidden")):function(){return null}}},9008:function(e,t,n){e.exports=n(9201)},6223:function(e,t,n){"use strict";n.d(t,{Z:function(){return w}});var r,a,o,__assign=function(){return(__assign=Object.assign||function(e){for(var t,n=1,r=arguments.length;n<r;n++)for(var a in t=arguments[n])Object.prototype.hasOwnProperty.call(t,a)&&(e[a]=t[a]);return e}).apply(this,arguments)};function __rest(e,t){var n={};for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&0>t.indexOf(r)&&(n[r]=e[r]);if(null!=e&&"function"==typeof Object.getOwnPropertySymbols)for(var a=0,r=Object.getOwnPropertySymbols(e);a<r.length;a++)0>t.indexOf(r[a])&&Object.prototype.propertyIsEnumerable.call(e,r[a])&&(n[r[a]]=e[r[a]]);return n}function __spreadArray(e,t,n){if(n||2==arguments.length)for(var r,a=0,o=t.length;a<o;a++)!r&&a in t||(r||(r=Array.prototype.slice.call(t,0,a)),r[a]=t[a]);return e.concat(r||Array.prototype.slice.call(t))}"function"==typeof SuppressedError&&SuppressedError;var i=n(7294),l="right-scroll-bar-position",c="width-before-scroll-bar";function assignRef(e,t){return"function"==typeof e?e(t):e&&(e.current=t),e}function useCallbackRef(e,t){var n=(0,i.useState)(function(){return{value:e,callback:t,facade:{get current(){return n.value},set current(value){var r=n.value;r!==value&&(n.value=value,n.callback(value,r))}}}})[0];return n.callback=t,n.facade}var u=new WeakMap;function useMergeRefs(e,t){var n=useCallbackRef(t||null,function(t){return e.forEach(function(e){return assignRef(e,t)})});return i.useLayoutEffect(function(){var t=u.get(n);if(t){var r=new Set(t),a=new Set(e),o=n.current;r.forEach(function(e){a.has(e)||assignRef(e,null)}),a.forEach(function(e){r.has(e)||assignRef(e,o)})}u.set(n,e)},[e]),n}function ItoI(e){return e}var s=(void 0===r&&(r={}),(a=function innerCreateMedium(e,t){void 0===t&&(t=ItoI);var n=[],r=!1;return{read:function(){if(r)throw Error("Sidecar: could not `read` from an `assigned` medium. `read` could be used only with `useMedium`.");return n.length?n[n.length-1]:e},useMedium:function(e){var a=t(e,r);return n.push(a),function(){n=n.filter(function(e){return e!==a})}},assignSyncMedium:function(e){for(r=!0;n.length;){var t=n;n=[],t.forEach(e)}n={push:function(t){return e(t)},filter:function(){return n}}},assignMedium:function(e){r=!0;var t=[];if(n.length){var a=n;n=[],a.forEach(e),t=n}var executeQueue=function(){var n=t;t=[],n.forEach(e)},cycle=function(){return Promise.resolve().then(executeQueue)};cycle(),n={push:function(e){t.push(e),cycle()},filter:function(e){return t=t.filter(e),n}}}}}(null)).options=__assign({async:!0,ssr:!1},r),a),nothing=function(){},d=i.forwardRef(function(e,t){var n=i.useRef(null),r=i.useState({onScrollCapture:nothing,onWheelCapture:nothing,onTouchMoveCapture:nothing}),a=r[0],o=r[1],l=e.forwardProps,c=e.children,u=e.className,d=e.removeScrollBar,f=e.enabled,p=e.shards,v=e.sideCar,m=e.noIsolation,g=e.inert,h=e.allowPinchZoom,b=e.as,y=void 0===b?"div":b,$=__rest(e,["forwardProps","children","className","removeScrollBar","enabled","shards","sideCar","noIsolation","inert","allowPinchZoom","as"]),E=useMergeRefs([n,t]),w=__assign(__assign({},$),a);return i.createElement(i.Fragment,null,f&&i.createElement(v,{sideCar:s,removeScrollBar:d,shards:p,noIsolation:m,inert:g,setCallbacks:o,allowPinchZoom:!!h,lockRef:n}),l?i.cloneElement(i.Children.only(c),__assign(__assign({},w),{ref:E})):i.createElement(y,__assign({},w,{className:u,ref:E}),c))});d.defaultProps={enabled:!0,removeScrollBar:!0,inert:!1},d.classNames={fullWidth:c,zeroRight:l};var SideCar=function(e){var t=e.sideCar,n=__rest(e,["sideCar"]);if(!t)throw Error("Sidecar: please provide `sideCar` property to import the right car");var r=t.read();if(!r)throw Error("Sidecar medium not found");return i.createElement(r,__assign({},n))};function exportSidecar(e,t){return e.useMedium(t),SideCar}function makeStyleTag(){if(!document)return null;var e=document.createElement("style");e.type="text/css";var t=o||n.nc;return t&&e.setAttribute("nonce",t),e}function injectStyles(e,t){e.styleSheet?e.styleSheet.cssText=t:e.appendChild(document.createTextNode(t))}function insertStyleTag(e){(document.head||document.getElementsByTagName("head")[0]).appendChild(e)}SideCar.isSideCarExport=!0;var stylesheetSingleton=function(){var e=0,t=null;return{add:function(n){0==e&&(t=makeStyleTag())&&(injectStyles(t,n),insertStyleTag(t)),e++},remove:function(){--e||!t||(t.parentNode&&t.parentNode.removeChild(t),t=null)}}},styleHookSingleton=function(){var e=stylesheetSingleton();return function(t,n){i.useEffect(function(){return e.add(t),function(){e.remove()}},[t&&n])}},styleSingleton=function(){var e=styleHookSingleton();return function(t){return e(t.styles,t.dynamic),null}},f={left:0,top:0,right:0,gap:0},parse=function(e){return parseInt(e||"",10)||0},getOffset=function(e){var t=window.getComputedStyle(document.body),n=t["padding"===e?"paddingLeft":"marginLeft"],r=t["padding"===e?"paddingTop":"marginTop"],a=t["padding"===e?"paddingRight":"marginRight"];return[parse(n),parse(r),parse(a)]},getGapWidth=function(e){if(void 0===e&&(e="margin"),"undefined"==typeof window)return f;var t=getOffset(e),n=document.documentElement.clientWidth,r=window.innerWidth;return{left:t[0],top:t[1],right:t[2],gap:Math.max(0,r-n+t[2]-t[0])}},p=styleSingleton(),v="data-scroll-locked",getStyles=function(e,t,n,r){var a=e.left,o=e.top,i=e.right,u=e.gap;return void 0===n&&(n="margin"),"\n  .".concat("with-scroll-bars-hidden"," {\n   overflow: hidden ").concat(r,";\n   padding-right: ").concat(u,"px ").concat(r,";\n  }\n  body[").concat(v,"] {\n    overflow: hidden ").concat(r,";\n    overscroll-behavior: contain;\n    ").concat([t&&"position: relative ".concat(r,";"),"margin"===n&&"\n    padding-left: ".concat(a,"px;\n    padding-top: ").concat(o,"px;\n    padding-right: ").concat(i,"px;\n    margin-left:0;\n    margin-top:0;\n    margin-right: ").concat(u,"px ").concat(r,";\n    "),"padding"===n&&"padding-right: ".concat(u,"px ").concat(r,";")].filter(Boolean).join(""),"\n  }\n  \n  .").concat(l," {\n    right: ").concat(u,"px ").concat(r,";\n  }\n  \n  .").concat(c," {\n    margin-right: ").concat(u,"px ").concat(r,";\n  }\n  \n  .").concat(l," .").concat(l," {\n    right: 0 ").concat(r,";\n  }\n  \n  .").concat(c," .").concat(c," {\n    margin-right: 0 ").concat(r,";\n  }\n  \n  body[").concat(v,"] {\n    ").concat("--removed-body-scroll-bar-size",": ").concat(u,"px;\n  }\n")},RemoveScrollBar=function(e){var t=e.noRelative,n=e.noImportant,r=e.gapMode,a=void 0===r?"margin":r,o=i.useMemo(function(){return getGapWidth(a)},[a]);return i.useEffect(function(){return document.body.setAttribute(v,""),function(){document.body.removeAttribute(v)}},[]),i.createElement(p,{styles:getStyles(o,!t,a,n?"":"!important")})},m=!1;if("undefined"!=typeof window)try{var g=Object.defineProperty({},"passive",{get:function(){return m=!0,!0}});window.addEventListener("test",g,g),window.removeEventListener("test",g,g)}catch(e){m=!1}var h=!!m&&{passive:!1},elementCanBeScrolled=function(e,t){var n=window.getComputedStyle(e);return"hidden"!==n[t]&&!(n.overflowY===n.overflowX&&"TEXTAREA"!==e.tagName&&"visible"===n[t])},locationCouldBeScrolled=function(e,t){var n=t;do{if("undefined"!=typeof ShadowRoot&&n instanceof ShadowRoot&&(n=n.host),elementCouldBeScrolled(e,n)){var r=getScrollVariables(e,n);if(r[1]>r[2])return!0}n=n.parentNode}while(n&&n!==document.body);return!1},elementCouldBeScrolled=function(e,t){return"v"===e?elementCanBeScrolled(t,"overflowY"):elementCanBeScrolled(t,"overflowX")},getScrollVariables=function(e,t){return"v"===e?[t.scrollTop,t.scrollHeight,t.clientHeight]:[t.scrollLeft,t.scrollWidth,t.clientWidth]},handleScroll=function(e,t,n,r,a){var o,i=(o=window.getComputedStyle(t).direction,"h"===e&&"rtl"===o?-1:1),l=i*r,c=n.target,u=t.contains(c),s=!1,d=l>0,f=0,p=0;do{var v=getScrollVariables(e,c),m=v[0],g=v[1]-v[2]-i*m;(m||g)&&elementCouldBeScrolled(e,c)&&(f+=g,p+=m),c=c.parentNode}while(!u&&c!==document.body||u&&(t.contains(c)||t===c));return d&&(a&&0===f||!a&&l>f)?s=!0:!d&&(a&&0===p||!a&&-l>p)&&(s=!0),s},getTouchXY=function(e){return"changedTouches"in e?[e.changedTouches[0].clientX,e.changedTouches[0].clientY]:[0,0]},getDeltaXY=function(e){return[e.deltaX,e.deltaY]},extractRef=function(e){return e&&"current"in e?e.current:e},b=0,y=[],$=exportSidecar(s,function(e){var t=i.useRef([]),n=i.useRef([0,0]),r=i.useRef(),a=i.useState(b++)[0],o=i.useState(function(){return styleSingleton()})[0],l=i.useRef(e);i.useEffect(function(){l.current=e},[e]),i.useEffect(function(){if(e.inert){document.body.classList.add("block-interactivity-".concat(a));var t=__spreadArray([e.lockRef.current],(e.shards||[]).map(extractRef),!0).filter(Boolean);return t.forEach(function(e){return e.classList.add("allow-interactivity-".concat(a))}),function(){document.body.classList.remove("block-interactivity-".concat(a)),t.forEach(function(e){return e.classList.remove("allow-interactivity-".concat(a))})}}},[e.inert,e.lockRef.current,e.shards]);var c=i.useCallback(function(e,t){if("touches"in e&&2===e.touches.length)return!l.current.allowPinchZoom;var a,o=getTouchXY(e),i=n.current,c="deltaX"in e?e.deltaX:i[0]-o[0],u="deltaY"in e?e.deltaY:i[1]-o[1],s=e.target,d=Math.abs(c)>Math.abs(u)?"h":"v";if("touches"in e&&"h"===d&&"range"===s.type)return!1;var f=locationCouldBeScrolled(d,s);if(!f)return!0;if(f?a=d:(a="v"===d?"h":"v",f=locationCouldBeScrolled(d,s)),!f)return!1;if(!r.current&&"changedTouches"in e&&(c||u)&&(r.current=a),!a)return!0;var p=r.current||a;return handleScroll(p,t,e,"h"===p?c:u,!0)},[]),u=i.useCallback(function(e){if(y.length&&y[y.length-1]===o){var n="deltaY"in e?getDeltaXY(e):getTouchXY(e),r=t.current.filter(function(t){var r;return t.name===e.type&&t.target===e.target&&(r=t.delta)[0]===n[0]&&r[1]===n[1]})[0];if(r&&r.should){e.cancelable&&e.preventDefault();return}if(!r){var a=(l.current.shards||[]).map(extractRef).filter(Boolean).filter(function(t){return t.contains(e.target)});(a.length>0?c(e,a[0]):!l.current.noIsolation)&&e.cancelable&&e.preventDefault()}}},[]),s=i.useCallback(function(e,n,r,a){var o={name:e,delta:n,target:r,should:a};t.current.push(o),setTimeout(function(){t.current=t.current.filter(function(e){return e!==o})},1)},[]),d=i.useCallback(function(e){n.current=getTouchXY(e),r.current=void 0},[]),f=i.useCallback(function(t){s(t.type,getDeltaXY(t),t.target,c(t,e.lockRef.current))},[]),p=i.useCallback(function(t){s(t.type,getTouchXY(t),t.target,c(t,e.lockRef.current))},[]);i.useEffect(function(){return y.push(o),e.setCallbacks({onScrollCapture:f,onWheelCapture:f,onTouchMoveCapture:p}),document.addEventListener("wheel",u,h),document.addEventListener("touchmove",u,h),document.addEventListener("touchstart",d,h),function(){y=y.filter(function(e){return e!==o}),document.removeEventListener("wheel",u,h),document.removeEventListener("touchmove",u,h),document.removeEventListener("touchstart",d,h)}},[]);var v=e.removeScrollBar,m=e.inert;return i.createElement(i.Fragment,null,m?i.createElement(o,{styles:"\n  .block-interactivity-".concat(a," {pointer-events: none;}\n  .allow-interactivity-").concat(a," {pointer-events: all;}\n")}):null,v?i.createElement(RemoveScrollBar,{gapMode:"margin"}):null)}),E=i.forwardRef(function(e,t){return i.createElement(d,__assign({},e,{ref:t,sideCar:$}))});E.classNames=d.classNames;var w=E},7552:function(e,t,n){"use strict";n.d(t,{EW:function(){return $3db38b7d1fb3fe6a$export$b7ece24a22aeda8c}});var r=n(7294);let a=0;function $3db38b7d1fb3fe6a$export$b7ece24a22aeda8c(){(0,r.useEffect)(()=>{var e,t;let n=document.querySelectorAll("[data-radix-focus-guard]");return document.body.insertAdjacentElement("afterbegin",null!==(e=n[0])&&void 0!==e?e:$3db38b7d1fb3fe6a$var$createFocusGuard()),document.body.insertAdjacentElement("beforeend",null!==(t=n[1])&&void 0!==t?t:$3db38b7d1fb3fe6a$var$createFocusGuard()),a++,()=>{1===a&&document.querySelectorAll("[data-radix-focus-guard]").forEach(e=>e.remove()),a--}},[])}function $3db38b7d1fb3fe6a$var$createFocusGuard(){let e=document.createElement("span");return e.setAttribute("data-radix-focus-guard",""),e.tabIndex=0,e.style.cssText="outline: none; opacity: 0; position: fixed; pointer-events: none",e}},5420:function(e,t,n){"use strict";n.d(t,{M:function(){return d}});var r=n(7462),a=n(7294),o=n(8771),i=n(5320),l=n(9698);let c="focusScope.autoFocusOnMount",u="focusScope.autoFocusOnUnmount",s={bubbles:!1,cancelable:!0},d=(0,a.forwardRef)((e,t)=>{let{loop:n=!1,trapped:d=!1,onMountAutoFocus:p,onUnmountAutoFocus:v,...m}=e,[g,h]=(0,a.useState)(null),b=(0,l.W)(p),y=(0,l.W)(v),$=(0,a.useRef)(null),E=(0,o.e)(t,e=>h(e)),w=(0,a.useRef)({paused:!1,pause(){this.paused=!0},resume(){this.paused=!1}}).current;(0,a.useEffect)(()=>{if(d){function handleFocusIn(e){if(w.paused||!g)return;let t=e.target;g.contains(t)?$.current=t:$d3863c46a17e8a28$var$focus($.current,{select:!0})}function handleFocusOut(e){if(w.paused||!g)return;let t=e.relatedTarget;null===t||g.contains(t)||$d3863c46a17e8a28$var$focus($.current,{select:!0})}function handleMutations(e){let t=document.activeElement;if(t===document.body)for(let t of e)t.removedNodes.length>0&&$d3863c46a17e8a28$var$focus(g)}document.addEventListener("focusin",handleFocusIn),document.addEventListener("focusout",handleFocusOut);let e=new MutationObserver(handleMutations);return g&&e.observe(g,{childList:!0,subtree:!0}),()=>{document.removeEventListener("focusin",handleFocusIn),document.removeEventListener("focusout",handleFocusOut),e.disconnect()}}},[d,g,w.paused]),(0,a.useEffect)(()=>{if(g){f.add(w);let e=document.activeElement,t=g.contains(e);if(!t){let t=new CustomEvent(c,s);g.addEventListener(c,b),g.dispatchEvent(t),t.defaultPrevented||($d3863c46a17e8a28$var$focusFirst($d3863c46a17e8a28$var$removeLinks($d3863c46a17e8a28$var$getTabbableCandidates(g)),{select:!0}),document.activeElement===e&&$d3863c46a17e8a28$var$focus(g))}return()=>{g.removeEventListener(c,b),setTimeout(()=>{let t=new CustomEvent(u,s);g.addEventListener(u,y),g.dispatchEvent(t),t.defaultPrevented||$d3863c46a17e8a28$var$focus(null!=e?e:document.body,{select:!0}),g.removeEventListener(u,y),f.remove(w)},0)}}},[g,b,y,w]);let S=(0,a.useCallback)(e=>{if(!n&&!d||w.paused)return;let t="Tab"===e.key&&!e.altKey&&!e.ctrlKey&&!e.metaKey,r=document.activeElement;if(t&&r){let t=e.currentTarget,[a,o]=$d3863c46a17e8a28$var$getTabbableEdges(t),i=a&&o;i?e.shiftKey||r!==o?e.shiftKey&&r===a&&(e.preventDefault(),n&&$d3863c46a17e8a28$var$focus(o,{select:!0})):(e.preventDefault(),n&&$d3863c46a17e8a28$var$focus(a,{select:!0})):r===t&&e.preventDefault()}},[n,d,w.paused]);return(0,a.createElement)(i.WV.div,(0,r.Z)({tabIndex:-1},m,{ref:E,onKeyDown:S}))});function $d3863c46a17e8a28$var$focusFirst(e,{select:t=!1}={}){let n=document.activeElement;for(let r of e)if($d3863c46a17e8a28$var$focus(r,{select:t}),document.activeElement!==n)return}function $d3863c46a17e8a28$var$getTabbableEdges(e){let t=$d3863c46a17e8a28$var$getTabbableCandidates(e),n=$d3863c46a17e8a28$var$findVisible(t,e),r=$d3863c46a17e8a28$var$findVisible(t.reverse(),e);return[n,r]}function $d3863c46a17e8a28$var$getTabbableCandidates(e){let t=[],n=document.createTreeWalker(e,NodeFilter.SHOW_ELEMENT,{acceptNode:e=>{let t="INPUT"===e.tagName&&"hidden"===e.type;return e.disabled||e.hidden||t?NodeFilter.FILTER_SKIP:e.tabIndex>=0?NodeFilter.FILTER_ACCEPT:NodeFilter.FILTER_SKIP}});for(;n.nextNode();)t.push(n.currentNode);return t}function $d3863c46a17e8a28$var$findVisible(e,t){for(let n of e)if(!$d3863c46a17e8a28$var$isHidden(n,{upTo:t}))return n}function $d3863c46a17e8a28$var$isHidden(e,{upTo:t}){if("hidden"===getComputedStyle(e).visibility)return!0;for(;e&&(void 0===t||e!==t);){if("none"===getComputedStyle(e).display)return!0;e=e.parentElement}return!1}function $d3863c46a17e8a28$var$isSelectableInput(e){return e instanceof HTMLInputElement&&"select"in e}function $d3863c46a17e8a28$var$focus(e,{select:t=!1}={}){if(e&&e.focus){let n=document.activeElement;e.focus({preventScroll:!0}),e!==n&&$d3863c46a17e8a28$var$isSelectableInput(e)&&t&&e.select()}}let f=$d3863c46a17e8a28$var$createFocusScopesStack();function $d3863c46a17e8a28$var$createFocusScopesStack(){let e=[];return{add(t){let n=e[0];t!==n&&(null==n||n.pause()),(e=$d3863c46a17e8a28$var$arrayRemove(e,t)).unshift(t)},remove(t){var n;null===(n=(e=$d3863c46a17e8a28$var$arrayRemove(e,t))[0])||void 0===n||n.resume()}}}function $d3863c46a17e8a28$var$arrayRemove(e,t){let n=[...e],r=n.indexOf(t);return -1!==r&&n.splice(r,1),n}function $d3863c46a17e8a28$var$removeLinks(e){return e.filter(e=>"A"!==e.tagName)}}}]);