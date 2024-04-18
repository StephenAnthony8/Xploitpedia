<script>

    import { categories }  from '$lib/LandingPage';

    export let landingPageItems = {};

    /* loop attaching API responses to categories object */
    for (let i = 0; i < 5; i++ ) {
        if (categories[i]['name'] !== 'Indicators Of Compromise') {
            categories[i]['body'] = landingPageItems[0][categories[i]['name']];
        }
        else {
            categories[i]['body'] = landingPageItems[1];
        }
    }
    const tag = 'Indicators Of Compromise';


</script>

<!-- landing page body -->
<!-- two page scroll enabled -->
<main class="flex flex-col flex-1 p-4">
    
    <!-- landing page  description-->
    <section id="introPage" class="max-w-full grid gap-10 py-8 sm:py-14">
        <div class="mx-auto lg:max-w-[80%] flex justify-items-center flex-col lg:justify-center text-center lg:text-center gap-6 md:gap-8 ">
            <h2 class="font-semibold leading-relaxed text-4xl/none sm:text-5xl/snug md:text-6xl/tight">
                Your go-to platform for in-depth insights into the intricate world of cybersecurity threats.
            </h2>
            <div class="font-light p_color text-lg sm:text-xl md:text-2xl roboto sm:tracking-wider">
            <p class="mb-4 ">
                From <span class="hover:text-rose-400">malware families</span> to <span class="hover:text-cyan-400">threat groups and campaigns</span>  associated with various exploits, <span class="hover:italic font-bold">Xploitpedia</span> is your go-to for comprehensive insights to help you understand the complex inner working of modern malware operations and strengthen your organization's defenses.    
            </p>
            <p>
                Xploitpedia provides an extensive database for all things malware related for your research needs.
            </p>
        </div>
        </div>
    </section>
    <!-- landing page section 2: category showcase -->
    <section id="landingPage" class="max-w-full grid gap-10 my-8 sm:my-14">
        <div>
            <h1 class="w-[80%] mx-auto my-8 font-semibold sm:my-12 text-2xl sm:text-3xl lg:text-4xl tracking-normal sm:tracking-wider text-center italic underline decoration-violet-950 decoration-[1px] underline-offset-[10px] poppins ">XploitPedia Information Categories</h1>
        </div>
        
        {#each categories as category, count}
        <!-- Format: Example : description -->
                <div class={"w-[80%] mx-auto flex justify-center " + (count % 2 ? 'flex-row-reverse' : 'flex-row')}>
                    <a href={category.link + '/' + category.body.id} class="mx-[5%] w-[45%] flex flex-col justify-center bg-slate-930 border border-violet-950 rounded-3xl shadow md:flex-row md:max-w-xl duration-500 transition-ease-in-out hover:bg-gray-100/10 tracking-wide p-4">
                        <div class="flex">
                            <!-- -- comment: function to obtain name: values here -->
                            <!-- {#each category.body as info} -->
                            <ul class="flex text-left flex-col gap-3 font-semibold w-[542px]">
                                <div class="flex flex-col font-normal"><b>Name:</b>
                                    {(category.name !== tag ? category.body.name : category.body.malware_printable)}
                                </div>
                                <li>Type:  <span class="line-clamp-1 font-normal">{(category.name !== tag ? category.body.type : category.body.ioc_type + " (" + category.body.threat_type + ")")}</span></li>
                                <li>Date of Discovery:<span class="line-clamp-1 font-normal">{(category.name !== tag ? category.body.created : category.body.first_seen_utc) }</span></li>
                                <li class="w-full">{(category.name !== tag ? 'Description: ' : 'Indicator Of Compromise Value:')}<span class="line-clamp-3 font-normal">{(category.name !== tag ? category.body.description : category.body.ioc_value)}</span></li>
                                <!--
                            -->
                                </ul> 
                            <!-- {/each} -->
                        </div>
                    </a>
                    
                    <!-- --comment: description -->
                    <div class="mx-[5%] w-[45%] flex flex-col p-4 leading-normal justify-center text-center  md:max-w-xl">

                        <a href={category.link}><h3 class="mb-2 text-2xl font-bold hover:text-3xl duration-300 hover:underline decoration-dotted poppins">
                            {category.name}
                        </h3></a>
                        <p class="mb-3 font-normal text-base p_color roboto">{category.description}</p>
                    </div>
                </div>
            {/each}

    </section>
</main>