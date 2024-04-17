<script>
    import { ItemIoc } from "$lib/SecondPage";
</script>


<div class="flex flex-wrap overflow-y-auto max-h-[730px]">
    {#each ItemIoc as iocs, count}
        <div class="flex flex-col p-4 overflow-auto border-solid m-8 border-8 rounded-2xl bg-stone-900 w-[400px] h-[210px] border-slate-400">
            <p><b>Name:</b>{iocs.name}</p>
            <p><b>Value:</b>{iocs.value}</p>
            <p><b>Type:</b>{iocs.type}</p>
            <p><b>Confidence:</b>{iocs.confidence}</p>
            <p><b>Printable name:</b>{iocs.malware_printable}</p>
            <p><b>alias:</b>{iocs.alias}</p>
            
        </div>
    {/each}

</div>