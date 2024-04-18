<script>
    /* handle stiix object fetch events depending on the category required*/
    import { whichCategory } from '$lib/SecondPage';

    export let category;
    export let currentId;
    export let listItems;
    const tag = whichCategory(category);


    /* import { apiLink } from '$lib/LandingPage'; */
    /* if the route is equal to the current value, highlight it */

</script>

<!-- Page container -->

<div class="w-70 mr-10">
    <!-- sections -->
    <!-- left list --> 
    <div class=" w-[380px] border-slate-900">
            <a href={'/' + tag} class="w-[248px]">
                <h3 class=" px-12 py-5"><b class="opacity-85 top-0 hover:underline underline-offset-4 tracking-widest decoration-1 text-2xl">{category}</b></h3>
            </a>

        <div class="w-[304px] overflow-y-auto flex flex-col max-h-[65.5vh] ml-[40px]  shadow rounded-sm tracking-wide scrollbar-hide">
            <!-- ul : category name -->
            {#each listItems as items, count}
                <a href={'/' + tag +'/' + (tag === 'iocs' ? items.category : items.id)} class={" border-l-2 border-l-slate-900 opacity-75 hover:opacity-100 hover:border-l-slate-400 " + ((currentId === items.id && currentId !== undefined) ? " bg-slate-900" : "bg-slate-950" )}>
                    <div class="mx-16 py-5 tracking-wide">
                        <b class="poppins">{items.name}<!-- {count} --></b>
                    </div>
                </a>
            {/each}

        </div>
    </div>
</div>
    <!-- central information block -->
        <!-- name -->
        <!-- description -->
        <!-- groups, software & campaign relations # retractable-->
        <!-- right side: Type, platform --> 
    