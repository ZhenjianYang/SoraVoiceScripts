from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0102   ._SN',
        MapName             = 'event',
        Location            = 'E0102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60087",
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
        'Ryan',                                 # 9
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01380 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01380P._CP',             # 00
    )

    DeclNpc(
        X                   = -95850,
        Z                   = 5550,
        Y                   = -92830,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_D8",           # 01, 1
        "Function_2_D9",           # 02, 2
        "Function_3_EF",           # 03, 3
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    ClearChrFlags(0x10, 0x80)
    Return()

    # Function_0_D2 end

    def Function_1_D8(): pass

    label("Function_1_D8")

    Return()

    # Function_1_D8 end

    def Function_2_D9(): pass

    label("Function_2_D9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_D9")

    label("loc_EE")

    Return()

    # Function_2_D9 end

    def Function_3_EF(): pass

    label("Function_3_EF")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        (
            "Ahh... Being up on the deck on a nice day really\x01",
            "is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "It's even better now that we don't have to be all\x01",
            "stealthy, too.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_EF end

    SaveToFile()

Try(main)
