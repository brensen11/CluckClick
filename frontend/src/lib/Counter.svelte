<script lang="ts">
  let count: number = $state(0)
  const increment = () => {
    count += 1
  }
</script>

<button type="button" class="btn preset-filled-primary-50-950" onclick={increment}>
  count is {count}
</button>
