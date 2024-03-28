<script>
    export let y;
    /* attach other page links (api, github, about me) once they have been created */
    let tabs = [
        {name: 'API Documentation', link:'#API'},
        {name: 'Github', link:'#Github'},
        {name: 'About me', link:'about me'}

    ]
</script>

<header class={'sticky z-[10] top-0 duration-200 px-6 flex items-center justify-between border border-solid ' + (
    y > 0 ? 'py-4 bf-slate-950 border-violet-950': 'py-6 bg-transparent border-transparent'
)}>
    <!-- Top right section -->
    <h1 class="font-medium">
        <b class="font-bold poppins">Xploitpedia</b>
    </h1>
    <!-- top left section -->
    <div class="sm:flex items-center gap-4 hidden">
        {#each tabs as tab, index}
            <a href={tab.link} class="duration-200 hover:text-violet-400">
                <p>{tab.name}</p>
            </a>
        {/each}
    </div>
</header>