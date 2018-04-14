from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0411   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0411.x',
        MapIndex            = 1,
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
        ' ',                                    # 9
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
        'ED6_DT09/CH10040 ._CH',             # 00
        'ED6_DT09/CH10041 ._CH',             # 01
        'ED6_DT09/CH10070 ._CH',             # 02
        'ED6_DT09/CH10071 ._CH',             # 03
        'ED6_DT09/CH10150 ._CH',             # 04
        'ED6_DT09/CH10151 ._CH',             # 05
        'ED6_DT09/CH10190 ._CH',             # 06
        'ED6_DT09/CH10191 ._CH',             # 07
        'ED6_DT29/CH12140 ._CH',             # 08
        'ED6_DT29/CH12141 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH10040P._CP',             # 00
        'ED6_DT09/CH10041P._CP',             # 01
        'ED6_DT09/CH10070P._CP',             # 02
        'ED6_DT09/CH10071P._CP',             # 03
        'ED6_DT09/CH10150P._CP',             # 04
        'ED6_DT09/CH10151P._CP',             # 05
        'ED6_DT09/CH10190P._CP',             # 06
        'ED6_DT09/CH10191P._CP',             # 07
        'ED6_DT29/CH12140P._CP',             # 08
        'ED6_DT29/CH12141P._CP',             # 09
    )

    DeclNpc(
        X                   = 90860,
        Z                   = 0,
        Y                   = 40240,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_13F",          # 01, 1
        "Function_2_140",          # 02, 2
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E")
    SetChrPos(0x0, 270, 0, -17670, 357)
    OP_69(0x0, 0x0)

    label("loc_13E")

    Return()

    # Function_0_11A end

    def Function_1_13F(): pass

    label("Function_1_13F")

    Return()

    # Function_1_13F end

    def Function_2_140(): pass

    label("Function_2_140")

    OP_C8(0x200, 0x1E, "C_PLAC19._CH", 0x1, 0x1F4)
    Return()

    # Function_2_140 end

    SaveToFile()

Try(main)
