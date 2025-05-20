<script lang="ts">
  import Item  from '../lib/Item.svelte'
  import type { ItemData } from '../api/entities.ts'

  export let data: Array<ItemData> = [];
  export let columns: number = 4;
  export let onClick: ((item: ItemData) => void) | null = null;
  export let classes: String = ""
</script>

<div class="grid gap-12 p-4 {classes}" style="grid-template-columns: repeat({columns}, minmax(0, 1fr));">
  {#each data as item, i}
      <Item item={item} onClick={onClick}/>
  {/each}
</div>
