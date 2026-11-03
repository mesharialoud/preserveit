(function(){
  var root=document.documentElement, KEY="pi-theme";
  function store(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}}
  function apply(t){root.setAttribute("data-theme",t);var m=document.querySelector('meta[name="theme-color"]');if(m)m.setAttribute("content",t==="dark"?"#0F1E2A":"#FFFFFF");
    document.dispatchEvent(new CustomEvent("themechange",{detail:t}))}
  var saved=store(KEY);
  var sys=window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light";
  apply(saved||sys);
  document.addEventListener("DOMContentLoaded",function(){
    var tb=document.getElementById("themeBtn");
    if(tb)tb.addEventListener("click",function(){var n=root.getAttribute("data-theme")==="dark"?"light":"dark";apply(n);store(KEY,n)});
    var mb=document.getElementById("menuBtn"),dr=document.getElementById("drawer");
    if(mb&&dr){mb.addEventListener("click",function(){var o=dr.classList.toggle("open");mb.setAttribute("aria-expanded",o)});
      dr.querySelectorAll("a").forEach(function(a){a.addEventListener("click",function(){dr.classList.remove("open");mb.setAttribute("aria-expanded","false")})})}
    var els=document.querySelectorAll(".reveal");
    if("IntersectionObserver" in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}})},{rootMargin:"0px 0px -8% 0px"});
      els.forEach(function(el){io.observe(el)})}else{els.forEach(function(el){el.classList.add("in")})}
    var y=document.getElementById("yr");if(y)y.textContent=new Date().getFullYear();
  });
})();
