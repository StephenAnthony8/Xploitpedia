<script>
export let linksContent;
export let referenceContent;
/* export let stiixLink; */
export let mainBody;
import {linkedLinks, capitalizeLetter } from '$lib/LandingPage';
/*  = [
        {name: 123, url: 'http://beatbox.com'},
        {name: 123, url: 'http://beatbox.com'}
    ] */
</script>

<div class=" mb-10 mt-[72px] w-full overflow-auto ">
    <div class="flex min-w-[780px] max-w-[1200px] max-h-[350px] flex-row">

        <div class="flex flex-col md:flex h-[450px] w-[1600px]"><!--   -->
            
            <!-- Name -->
            <h2 class=" text-5xl font-light w-fit h-fit my-20">
                <b>{mainBody.name}<!-- Name --></b> <!-- replace with obj name -->
            </h2>

            <!-- Description -->
            <div class="lg:w-[70%] max-w-[1400px] max-h-full overflow-y-auto text-lg">
                {mainBody.description}
                <!-- Lorem ipsum dolor sit amet consectetur adipisicing elit. Ratione nisi earum corrupti iusto, dolores illo adipisci inventore ut? Hic dignissimos quia laborum. Quo, commodi vel sapiente est esse architecto eaque! -->
            </div >
            
        </div>

        <!-- Additional info: replace with labels from correct variable -->
        <div class=" px-6 py-4 lg:w-[60%] border-[7px] border-solid border-slate-400 rounded-lg h-[230px] bg-stone-900"><!-- lg:mr-40   -->
            <p><b>ID: </b><span>{mainBody.id}</span></p>
            <p><b>Type: </b><span>{mainBody.type}</span></p>
            <p><b>Aliases: </b><span>{mainBody.aliases}</span></p>
            <p><b>First Seen: </b><span>{mainBody.last_seen}</span></p>
            <p><b>Last Seen: </b><span>{mainBody.first_seen}</span></p>
            <p><b>Contributors: </b><span>{mainBody['x_mitre_contributors']}</span></p>
        </div>
    </div>

    
    <div class="mt-[140px] mr-80 w-[80%] flex grow content-center flex-col min-h-[190px] h-[190px] border-[7px] border-solid border-slate-400 rounded-lg divide-y-[7px] divide-inherit bg-stone-900"> <!-- references, other linked stiix objects -->
        <!-- group links 1 -->
        <!-- <div class="h-[33.3%] flex">
            <div class="flex grow max-w-[15%] justify-center border-r-[7px] border-slate-400">
                <p class="my-auto "><b class="text-xl">Group link 1</b></p>
            </div>
            <article class="flex grow my-auto px-10 ">
                {#each referenceContent as link, count}
    
                    <p class="tracking-widest">{ (count === 0 ? "": ",  " )+ link.name}</p>
    
                {/each}
            </article>
        </div> -->
    
        <!-- Group links 2 -->
        {#each linksContent as stiix_links }
            
        <div class="h-[33.3%] flex overflow-auto">
            <div class="flex w-[224px] justify-center border-r-[7px] border-slate-400">
                <p class="my-auto "><b class="text-xl">{capitalizeLetter(stiix_links.name.split('_')[0]) + ' use'}<!-- Group link 2 --></b></p>
            </div>
            <article class="flex my-auto overflow-x-auto h-full">
                {#each stiix_links.content as links, count}
                
                    <a href={(linkedLinks[links.id.split('--')[0]] + links.id)} class="hover:text-violet-400 tracking-widest mx-2 my-auto line-clamp-1 overflow-hidden">{ (count === 0 ? "": ",  " )+ links.name}</a>
                
                {/each}
            </article>
        </div>
        {/each}
        
        <!-- References -->
        <div class="h-[33.3%] flex w-full">
            <div class="flex min-w-[224px] justify-center border-r-[7px] border-slate-400">
                <p class="my-auto "><b class="text-xl">References</b></p>
            </div>
            <article class="flex my-auto overflow-x-auto">
                {#each referenceContent as link, count}

                    <a href={link.link} class="hover:text-violet-400 tracking-widest mx-2 line-clamp-1 overflow-hidden ">{ (count === 0 ? "": ",  " ) + link.name}</a>

                {/each}
            </article>
        </div>

    </div>

</div>