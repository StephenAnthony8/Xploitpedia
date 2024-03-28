<!-- Defines the layout of the webpage / section of the webpage  -->
<script>
    /* imports */
    import "../app.css";
    import Header from "../components/Header.svelte";
    import Footer from "../components/Footer.svelte";

    let y;
    let innerHeight = 0;
    let innerWidth = 0;
    /* scroll to top function */
    function goTop() {
        document.body.scrollIntoView()
    }
</script>
<!-- body of the landing page (also entire page I think) -->
<div class="relative flex flex-col max-w-[1400px] mx-auto w-full text-sm sm:text-base min-h-screen">
    <!-- scroll up button - has js portion changing opacity + pointer-events -->
    <div class={"fixed bottom-0 w-full duration-200 flex p-10 z-[10] " + (
        y > 0 ? 'opacity-full pointer-events-auto' : 'pointer-events-none opacity-0'
    )}>
        <button on:click={goTop} class="ml-auto rounded-full bg-slate-900 text-violet-400 px-3 sm:px-4 hover:bg-slate-800 cursor-pointer ">
            <i class="fa-solid fa-arrow-up grid place-items-center aspect-square"></i>
        </button>
    </div>
    <!-- header -->
    <Header {y}/>
    <!-- body - to be included -->
    <slot />
    <!-- footer -->
    <Footer />
</div>
<!-- keeps track of the scrollY(attached to y), inner height & inner width -->
<svelte:window bind:scrollY={y} bind:innerHeight bind:innerWidth />