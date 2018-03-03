from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3118   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3118.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Dr. Miriam',                           # 9
        'Antoine',                              # 10
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
        'ED6_DT07/CH01430 ._CH',             # 00
        'ED6_DT07/CH01700 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01430P._CP',             # 00
        'ED6_DT07/CH01700P._CP',             # 01
    )

    DeclNpc(
        X                   = -1410,
        Z                   = 0,
        Y                   = 6690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -5510,
        Z                   = 0,
        Y                   = -3140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_FA",           # 00, 0
        "Function_1_111",          # 01, 1
        "Function_2_112",          # 02, 2
        "Function_3_136",          # 03, 3
        "Function_4_2EE",          # 04, 4
    )


    def Function_0_FA(): pass

    label("Function_0_FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_110")

    Return()

    # Function_0_FA end

    def Function_1_111(): pass

    label("Function_1_111")

    Return()

    # Function_1_111 end

    def Function_2_112(): pass

    label("Function_2_112")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_135")
    OP_8D(0xFE, -6290, -6030, -3150, 520, 1000)
    Jump("Function_2_112")

    label("loc_135")

    Return()

    # Function_2_112 end

    def Function_3_136(): pass

    label("Function_3_136")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_2EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_200")

    ChrTalk(    #0
        0xFE,
        (
            "I'm surprised he hasn't shown up today,\x01",
            "to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Maybe he's gone to the church?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "That might calm him down. Maybe he could\x01",
            "get a prayer or two in while he's at it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA")

    label("loc_200")


    ChrTalk(    #3
        0xFE,
        "...Erika's back, I hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "She's quite similar to her father...and poor\x01",
            "Murdock's got the gray hairs to prove it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "He's rushed in here demanding something\x01",
            "for his stomach pain more times than I can\x01",
            "count at this point.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2EA")

    TalkEnd(0xFE)
    Return()

    # Function_3_136 end

    def Function_4_2EE(): pass

    label("Function_4_2EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_309")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #6
        0xFE,
        "Nyaon?\x02",
    )

    CloseMessageWindow()

    label("loc_309")

    TalkEnd(0xFE)
    Return()

    # Function_4_2EE end

    SaveToFile()

Try(main)
