<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class="overflow-hidden bg-white shadow sm:rounded-lg">
    <div class="m-auto flex px-4 py-5 sm:px-6">
      <h3 class="mr-auto text-lg font-medium leading-6 text-gray-900">Books</h3>
      <button @click="showAddBookModal = true" class="btn btn-primary ml-auto mt-0" href="#">Add Book</button>
    </div>
    <div class="border-t border-gray-200">
      <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-2 sm:gap-4 sm:px-6">
        <div class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
          <ul
            v-if="books.length > 0"
            role="list"
            class="divide-y divide-gray-200 rounded-md border border-gray-200"
          >
            <li
              v-for="(book, index) in books"
              :key="index"
              class="flex items-center justify-between py-3 pl-3 pr-4 text-sm"
            >
              <div class="flex w-0 flex-1 items-center">
                <PaperClipIcon
                  class="h-5 w-5 flex-shrink-0 text-gray-400"
                  aria-hidden="true"
                />
                <span class="ml-2 w-0 flex-1 truncate">
                  {{ book.title }}<br />
                  <span class="text-xs text-gray-400"
                    >by {{ book.author }}</span
                  >
                </span>
                <span
                  v-if="book.read"
                  class="ml-2 w-0 flex-1 truncate text-xs uppercase tracking-wider text-gray-300"
                >
                  Read
                </span>
                <span
                  v-else
                  class="ml-2 w-0 flex-1 truncate text-xs uppercase tracking-wider text-gray-500"
                >
                  Not Yet Read
                </span>
              </div>
              <div class="ml-4 flex-shrink-0">
                <a
                  href="#"
                  class="text-brand-light hover:text-brand-dark hover:underline focus:text-brand-light"
                  >Update</a
                >
                <a
                  href="#"
                  class="ml-2 text-red-600 hover:text-red-900 hover:underline focus:text-red-500"
                  >Delete</a
                >
              </div>
            </li>
          </ul>
          <div v-else>No Books Found</div>
        </div>
      </div>
    </div>
  </div>
  <ModalAddBook :show="showAddBookModal" @close-modal="showAddBookModal = false" @keydown.esc="showAddBookModal = false" @book-added="getBooks"></ModalAddBook>
</template>

<script setup>
import { PaperClipIcon } from '@heroicons/vue/solid';
</script>

<script>
import { defineComponent } from 'vue';
import axios from 'axios';
import ModalAddBook from './ModalAddBook.vue';

export default defineComponent({
  components: {
    ModalAddBook,
  },
  data() {
    return {
      showAddBookModal: false,
      books: [],
    };
  },
  created() {
    this.getBooks();
  },
  methods: {
    getBooks() {
      const path = 'http://' + window.location.hostname + ':5000/books';
      axios
        .get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
});
</script>
