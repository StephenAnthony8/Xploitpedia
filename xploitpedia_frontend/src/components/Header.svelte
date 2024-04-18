<script>
    import { frontendRoute, tabs } from '$lib/LandingPage';
    export let y;

</script>
<!-- Header object containing website name/icon and categories -->
<header class={"px-8 bg-black font-bold text-xl poppins sticky z-[10] top-0 duration-100 flex border-b justify-between border-solid " + (
    y > 0 ? 'py-4 border-violet-950' : 'py-6  border-transparent'
)}>
    <h1 class="mx-4 w-fit">
        <a href={frontendRoute}>XploitPedia</a> <!-- replace with icon -->
    </h1>

    <div class="opacity-95 hover:opacity-100 transition ease-in-out duration-500 mx-3 w-[60%] lg:flex items-center justify-around hidden">

        {#each tabs as tab, i}
            <a href={tab.link}>
                <p class={"transition ease-in-out duration-300 hover:underline underline-offset-4 " + tab.color}>{tab.name}</p>
            </a>
        {/each}
    </div>
</header>