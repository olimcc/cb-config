![Workflow](https://github.com/olimcc/cb-config/actions/workflows/run-tests.yml/badge.svg)

## Modify config.yaml


## Format


```
  # one of [reserve_ca, recreation_gov]
- api: reserve_ca

  # For reservecalifornia, place is the park id
  # https://www.reservecalifornia.com/Web/#!park/682
  place: '682'

  # placeName is annoying to retrieve from the API, so we include
  # it here so message print outs are nice

  placeName: Steep Ravine

  # individual campgrounds within the park
  # for example, cabins are 766, campsites are 590
  # https://www.reservecalifornia.com/Web/#!park/682/766
  campground:
  - 590
  - 766

  # sites are optional, if you want to be picky
  # for reserve_ca these site ids are typically after a #
  # in the site name listed on the website
  sites: [
        "CB04", "CB07", "CB08", "CB09", "CB10",
        "EN01", "EN02", "EN03", "EN04", "EN05", "EN06"]

  # days of week the trip could start on
  day: ["fri", "sat"]

  # duration of stay
  nights: 1

  # months forward to search for
  months: 6

  # optionally use "ranges" to look for specific dates only
  # possible to set multiple ranges
  ranges:
  - startDate: '2022-09-12'
    endDate: '2022-10-19'
  - startDate: '2023-05-12'
    endDate: '2023-05-19'

  # who should availability go to
  telegramChats:
  - "-12345"
```