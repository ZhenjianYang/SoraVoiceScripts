from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3403   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Rudi',                                 # 9
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
        'ED6_DT07/CH01500 ._CH',             # 00
        'ED6_DT07/CH01760 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01500P._CP',             # 00
        'ED6_DT07/CH01760P._CP',             # 01
    )

    DeclNpc(
        X                   = 609110,
        Z                   = 0,
        Y                   = -64290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )


    ScpFunction(
        "Function_0_DA",           # 00, 0
        "Function_1_EC",           # 01, 1
        "Function_2_110",          # 02, 2
        "Function_3_282",          # 03, 3
    )


    def Function_0_DA(): pass

    label("Function_0_DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB")
    ClearChrFlags(0x10, 0x80)

    label("loc_EB")

    Return()

    # Function_0_DA end

    def Function_1_EC(): pass

    label("Function_1_EC")

    OP_16(0x2, 0xFA0, 0x76E58, 0xFFFD40E0, 0x23003A)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F")
    OP_1B(0x0, 0x0, 0x3)

    label("loc_10F")

    Return()

    # Function_1_EC end

    def Function_2_110(): pass

    label("Function_2_110")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_27E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1CA")
    OP_8C(0xFE, 90, 0)

    ChrTalk(    #0
        0xFE,
        (
            "I... I've gotta try and tell her how I feel about\x01",
            "her. This might be the last chance I ever get!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "But how am I best going about doing it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_27E")

    label("loc_1CA")


    ChrTalk(    #3
        0xFE,
        "Y-You there! Listen to my tale of woe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I heard Faye's going to be a mechanic on\x01",
            "board the Arseille now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Which means I won't be able to see her again!\x01",
            "Nooooooooo!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_27E")

    TalkEnd(0xFE)
    Return()

    # Function_2_110 end

    def Function_3_282(): pass

    label("Function_3_282")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2FC")

    ChrTalk(    #6
        0x106,
        (
            "#552FI can't see how they could have ended up in\x01",
            "Kaldia Tunnel. I should stick to searching the\x01",
            "factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39A")

    label("loc_2FC")


    ChrTalk(    #7
        0x106,
        (
            "#050FWait. This way leads to Kaldia Tunnel.\x02\x03",

            "#552FI can't see how they could have ended up in\x01",
            "Kaldia Tunnel. I should stick to searching the\x01",
            "factory.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_39A")

    OP_90(0x106, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    EventEnd(0x2)
    Return()

    # Function_3_282 end

    SaveToFile()

Try(main)
