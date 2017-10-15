from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C2101   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2101.x',
        MapIndex            = 98,
        MapDefaultBGM       = "ed60033",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10160 ._CH',             # 00
        'ED6_DT09/CH10161 ._CH',             # 01
        'ED6_DT09/CH10450 ._CH',             # 02
        'ED6_DT09/CH10451 ._CH',             # 03
        'ED6_DT09/CH10220 ._CH',             # 04
        'ED6_DT09/CH10221 ._CH',             # 05
        'ED6_DT09/CH10470 ._CH',             # 06
        'ED6_DT09/CH10471 ._CH',             # 07
        'ED6_DT09/CH10480 ._CH',             # 08
        'ED6_DT09/CH10481 ._CH',             # 09
        'ED6_DT09/CH11060 ._CH',             # 0A
        'ED6_DT09/CH11061 ._CH',             # 0B
        'ED6_DT09/CH10460 ._CH',             # 0C
        'ED6_DT09/CH10461 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT09/CH10160P._CP',             # 00
        'ED6_DT09/CH10161P._CP',             # 01
        'ED6_DT09/CH10450P._CP',             # 02
        'ED6_DT09/CH10451P._CP',             # 03
        'ED6_DT09/CH10220P._CP',             # 04
        'ED6_DT09/CH10221P._CP',             # 05
        'ED6_DT09/CH10470P._CP',             # 06
        'ED6_DT09/CH10471P._CP',             # 07
        'ED6_DT09/CH10480P._CP',             # 08
        'ED6_DT09/CH10481P._CP',             # 09
        'ED6_DT09/CH11060P._CP',             # 0A
        'ED6_DT09/CH11061P._CP',             # 0B
        'ED6_DT09/CH10460P._CP',             # 0C
        'ED6_DT09/CH10461P._CP',             # 0D
    )

    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_11B",          # 01, 1
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Return()

    # Function_0_11A end

    def Function_1_11B(): pass

    label("Function_1_11B")

    Return()

    # Function_1_11B end

    SaveToFile()

Try(main)
