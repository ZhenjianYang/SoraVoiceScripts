from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2813   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2813.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        'Rigel',                                # 9
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
        'ED6_DT07/CH02910 ._CH',             # 00
        'ED6_DT07/CH02910 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH02910P._CP',             # 00
        'ED6_DT07/CH02910P._CP',             # 01
    )

    DeclNpc(
        X                   = -2330,
        Z                   = 0,
        Y                   = 4680,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )


    ScpFunction(
        "Function_0_DA",           # 00, 0
        "Function_1_E7",           # 01, 1
        "Function_2_E8",           # 02, 2
    )


    def Function_0_DA(): pass

    label("Function_0_DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6")

    label("loc_E6")

    Return()

    # Function_0_DA end

    def Function_1_E7(): pass

    label("Function_1_E7")

    Return()

    # Function_1_E7 end

    def Function_2_E8(): pass

    label("Function_2_E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_29C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 7)), scpexpr(EXPR_END)), "loc_1C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_166")

    ChrTalk(    #0
        0x10,
        "(She's looking really down...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "If you're not feeling well, you should\x01",
            "go and rest, Kloe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0")

    label("loc_166")


    ChrTalk(    #2
        0x10,
        "...What's up, Kloe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x105,
        "#047FOh... It's nothing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        "W-Well, if you say so...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1C0")

    Jump("loc_29C")

    label("loc_1C3")


    ChrTalk(    #5
        0x10,
        "Kloe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        "What're you doing here this late in the evening?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x105,
        (
            "#043FWell...\x02\x03",

            "#047F...nothing in particular, really.\x02\x03",

            "Sorry. I didn't mean to get in the way\x01",
            "of your practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        "Oh, no! It's not like that.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F7F)

    label("loc_29C")

    TalkEnd(0xFE)
    Return()

    # Function_2_E8 end

    SaveToFile()

Try(main)
