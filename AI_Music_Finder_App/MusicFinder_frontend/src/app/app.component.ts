import { Component } from '@angular/core';
import { LyricSearchComponent } from './lyric-search/lyric-search.component';

@Component({
  selector: 'app-root',
  standalone: true,           // make app component standalone too
  imports: [LyricSearchComponent],  // import your standalone lyric-search here
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {}