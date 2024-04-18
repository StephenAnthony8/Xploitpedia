<!-- Layout for entire website -->
<script>
    import "../app.css";
    import Header from "../components/Header.svelte";
    import Footer from "../components/Footer.svelte";

    let y;
    let innerHeight = 0;
    let innerWidth = 0;

    function gotoTop() {
      document.body.scrollIntoView()
    }
</script>
<!-- background and scroll configurations for entire website -->
<div class="relative flex flex-col max-w-[100%] mx-auto w-full text-sm sm:text-base min-h-screen">

  <div class={"fixed bottom-0 w-full justify= duration-200 flex p-10 z-[10] " + (
    y > 0 ? 'opacity-full pointer-events-auto': 'opacity-0 pointer-events-none'
  )}>
    <button on:click={gotoTop} class="ml-auto rounded-full bg-slate-900
    text-violet-400 px-3 sm:px-4 hover:bg-slate-800 cursor-pointer">
      <i class="fa-solid fa-arrow-up" />
    </button>
  </div>
  <!-- header -->
  <Header {y}/>
  <!-- body -->
  <div class="mb-auto"><slot /></div>
  <!-- footer -->
  <Footer />
</div>



<svelte:window bind:scrollY={y} bind:innerHeight bind:innerWidth />