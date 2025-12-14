package main

import ( 
	"fmt"
	"time"
	"net/http"
	"encoding/json"
	"github.com/shirou/gopsutil/v4/host"
	"github.com/shirou/gopsutil/v4/mem"
	"github.com/shirou/gopsutil/v4/cpu"
)


		type SystemStats struct {
			Platform	string `json:"platform"`
			Family		string `json:"family"`
			Version		string `json:"version"`
			MemTotal	uint64 `json:"totalMemory"`
			MemFree		uint64 `json:"freeMemory"`
			MemUsedP	float64 `json:"memoryUsedPercent"`
			TcpuUsedP	[]float64 `json:"totalCpuUsedPercent"`
			CpuUsedP	[]float64 `json:"cpuUsedPercent"`
		}

func rawStatsHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
		
	v, _ := mem.VirtualMemory()
	platform, family, version, _ := host.PlatformInformation()
	tCpuPercent, _ := cpu.Percent(time.Second, false)
	cpuPercent, _ := cpu.Percent(time.Second, true)
	
	data := SystemStats{
		Platform:	platform,
		Family: family,
		Version: version,
		MemTotal: v.Total,
		MemFree: v.Free,
		MemUsedP: v.UsedPercent,
		TcpuUsedP: tCpuPercent,
		CpuUsedP: cpuPercent,
	}

	json.NewEncoder(w).Encode(data)
}
// guide to the right place
func rootHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "text/plain")
	
	fmt.Fprintf(w, "Head to /rawstats to get the stats")
}

func main() {
	
	http.HandleFunc("/", rootHandler)

	http.HandleFunc("/rawstats", rawStatsHandler)

	fmt.Println("Go worker running on port 9000")

	if err := http.ListenAndServe(":9000", nil);
	err != nil {
		fmt.Println("Error starting server: ", err)
	}
}


