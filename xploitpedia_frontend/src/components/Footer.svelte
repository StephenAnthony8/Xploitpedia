<script>
    import { links } from '$lib/LandingPage'
</script>

<footer class=" w-full py-10 bg-black border-t border-solid border-x-violet-950 flex flex-col gap-4 sm:gap-8 justify-center items-center">
    <p class="px-4 py-2 bg-black text-white">
        Get in touch &darr;
    </p>
    <div class="flex flex-row gap-4 items-center justify-center z-[11]">
        <p><b class="pr-2">Email: </b>steveanthony02@gmail.com</p>
        {#each links as link}
        <p>
            <b class="pr-2">{link.name}: </b>
            <a class="text-violet-400" href={link.link}>{link.identifier}
                <sup><span class="text-xs scale-75 pl-0.5">
                    <i class="fa-solid fa-arrow-up-right-from-square text-xs scale-[75%]" />
                </span></sup>
            </a>
        </p>
        {/each}
    </div>

</footer>