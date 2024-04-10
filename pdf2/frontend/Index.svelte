<script lang="ts">
	// import { JsonView } from "@zerodevx/svelte-json-view";

	import type { Gradio } from "@gradio/utils";
	import { Block, BlockLabel  } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import type { SelectData } from "@gradio/utils";

	import { tick } from "svelte";
	// import { File } from "@gradio/icons";
	import type { FileData } from "@gradio/client";
	import { Upload, ModifyUpload } from "@gradio/upload";

	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value: FileData | null = null;
	export let container = true;
	export let scale: number | null = null;
	export let root: string;
	// export let height: number | null = 500;
	export let label: string;
	// export let proxy_url: string;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus;
	export let gradio: Gradio<{
		change: never;
		input: never;
	}>;

	let _value = value;
    let old_value = _value;
</script>

<Block {visible} {elem_id} {elem_classes} {container} {scale} {min_width}>
    {#if loading_status}
        <StatusTracker
            autoscroll={gradio.autoscroll}
            i18n={gradio.i18n}
            {...loading_status}
        />
    {/if}
    <BlockLabel
        show_label={label !== null}
        Icon={File}
        float={value === null}
        label={label || "File"}
    />
    {#if _value}
        <ModifyUpload i18n={gradio.i18n} absolute />
    {:else}
        <Upload
            filetype={"application/pdf"}
            file_count="single"
            {root}
        >
            Upload your PDF
        </Upload>
    {/if}
</Block>
