import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-lyric-search',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './lyric-search.component.html',
  styleUrls: ['./lyric-search.component.scss']
})
export class LyricSearchComponent {
  lyrics = '';
  results: string[] = [];

  constructor(private http: HttpClient) {}

  search() {
    this.http.post<any>('http://localhost:8000/search/', { lyrics: this.lyrics })
      .subscribe(response => {
        this.results = response.songs || [];
      }, error => {
        console.error('API error', error);
        this.results = [];
      });
  }
}