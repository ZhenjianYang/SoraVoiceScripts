from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1310   ._SN',
        MapName             = 'Bose',
        Location            = 'T1310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1310_1 ._SN',
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
        'CWO Zelste',                           # 9
        'Warrant Officer Serose',               # 10
        'Private Egel',                         # 11
        'Private Mikey',                        # 12
        'Felicity',                             # 13
        'Ray',                                  # 14
        'Antoine',                              # 15
        '小説',                                 # 16
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
        'ED6_DT07/CH01310 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
        'ED6_DT07/CH01300 ._CH',             # 02
        'ED6_DT07/CH01300 ._CH',             # 03
        'ED6_DT07/CH01090 ._CH',             # 04
        'ED6_DT07/CH01220 ._CH',             # 05
        'ED6_DT07/CH01700 ._CH',             # 06
        'ED6_DT06/CH20021 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01310P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
        'ED6_DT07/CH01300P._CP',             # 03
        'ED6_DT07/CH01090P._CP',             # 04
        'ED6_DT07/CH01220P._CP',             # 05
        'ED6_DT07/CH01700P._CP',             # 06
        'ED6_DT06/CH20021P._CP',             # 07
    )

    DeclNpc(
        X                   = 82120,
        Z                   = 0,
        Y                   = 12850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 19950,
        Z                   = 0,
        Y                   = 22480,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 7310,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 80100,
        Z                   = 0,
        Y                   = 11110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 82940,
        Z                   = 0,
        Y                   = 52010,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 20490,
        Z                   = 0,
        Y                   = 14850,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 20480,
        Z                   = 0,
        Y                   = 13660,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 77080,
        Z                   = 750,
        Y                   = 6240,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1703943,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 20950,
        TriggerZ            = 0,
        TriggerY            = 22480,
        TriggerRange        = 800,
        ActorX              = 19950,
        ActorZ              = 1600,
        ActorY              = 22480,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 20950,
        TriggerZ            = 0,
        TriggerY            = 7310,
        TriggerRange        = 800,
        ActorX              = 20000,
        ActorZ              = 1600,
        ActorY              = 7310,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18440,
        TriggerZ            = 0,
        TriggerY            = 12120,
        TriggerRange        = 1000,
        ActorX              = 18440,
        ActorZ              = 1000,
        ActorY              = 12120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_256",          # 00, 0
        "Function_1_2F7",          # 01, 1
        "Function_2_390",          # 02, 2
        "Function_3_50D",          # 03, 3
        "Function_4_11A7",         # 04, 4
        "Function_5_2854",         # 05, 5
        "Function_6_33F0",         # 06, 6
        "Function_7_3CED",         # 07, 7
        "Function_8_4756",         # 08, 8
        "Function_9_4E99",         # 09, 9
        "Function_10_4EB3",        # 0A, 10
        "Function_11_4EB8",        # 0B, 11
        "Function_12_4EBD",        # 0C, 12
        "Function_13_535D",        # 0D, 13
        "Function_14_5899",        # 0E, 14
    )


    def Function_0_256(): pass

    label("Function_0_256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_272")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26F")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)

    label("loc_26F")

    Jump("loc_2F6")

    label("loc_272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2C3")
    SetChrPos(0xB, 77380, 0, 7430, 186)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_297")
    ClearChrFlags(0xF, 0x80)

    label("loc_297")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C0")
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C0")
    SetChrFlags(0xC, 0x10)

    label("loc_2C0")

    Jump("loc_2F6")

    label("loc_2C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2DE")
    SetChrPos(0xB, 82080, 0, 56640, 357)
    Jump("loc_2F6")

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2F6")
    SetChrPos(0xB, 19210, 0, 15060, 270)

    label("loc_2F6")

    Return()

    # Function_0_256 end

    def Function_1_2F7(): pass

    label("Function_1_2F7")

    OP_B1("T1310_n")
    OP_72(0x2, 0x10)
    OP_6F(0x2, 99)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31D")
    OP_1B(0x0, 0x0, 0xC)

    label("loc_31D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32E")
    OP_1B(0x5, 0x0, 0xD)

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 3)), scpexpr(EXPR_END)), "loc_33A")
    SetChrFlags(0xF, 0x80)

    label("loc_33A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38F")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_38F")

    Return()

    # Function_1_2F7 end

    def Function_2_390(): pass

    label("Function_2_390")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B5")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4F7")

    label("loc_3B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CE")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4F7")

    label("loc_3CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4F7")

    label("loc_3E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_400")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4F7")

    label("loc_400")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_419")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4F7")

    label("loc_419")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_432")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4F7")

    label("loc_432")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4F7")

    label("loc_44B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_464")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4F7")

    label("loc_464")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4F7")

    label("loc_47D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_496")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4F7")

    label("loc_496")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AF")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4F7")

    label("loc_4AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C8")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4F7")

    label("loc_4C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4F7")

    label("loc_4E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4F7")

    label("loc_50C")

    Return()

    # Function_2_390 end

    def Function_3_50D(): pass

    label("Function_3_50D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_6A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F")

    ChrTalk(    #0
        0xFE,
        (
            "I heard there was some kind of incident\x01",
            "at the royal academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Guard forces from the army have already\x01",
            "responded, thankfully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "We were able to respond so quickly because\x01",
            "communications were restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Ignorance really is the greatest thing to fear.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6A1")

    label("loc_62F")


    ChrTalk(    #4
        0xFE,
        (
            "A guard force was dispatched to the\x01",
            "royal academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Perhaps we should step up our patrols\x01",
            "here, as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A1")

    Jump("loc_11A3")

    label("loc_6A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_85A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A4")

    ChrTalk(    #6
        0xFE,
        (
            "Thanks to that generator, we managed to\x01",
            "at least restore our communications.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "The army can finally act as a unified\x01",
            "whole again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "We're still neck-deep in problems, but\x01",
            "at least we can rely on General Bright's\x01",
            "leadership.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_857")

    label("loc_7A4")


    ChrTalk(    #9
        0xFE,
        (
            "Thanks to that generator, we managed to\x01",
            "at least restore our communications.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "We're still neck-deep in problems, but\x01",
            "at least we can rely on General Bright's\x01",
            "leadership.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_857")

    Jump("loc_11A3")

    label("loc_85A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_97C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8D3")

    ChrTalk(    #11
        0xFE,
        "I hope things stay quiet for a bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I'd like to let the men rest for at least\x01",
            "a little while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_979")

    label("loc_8D3")


    ChrTalk(    #13
        0xFE,
        "We've finally stood down from alert status.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I know that, as a leader, I should never\x01",
            "complain like this, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "I hope things stay quiet for a bit.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_979")

    Jump("loc_11A3")

    label("loc_97C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_A45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9BE")

    ChrTalk(    #16
        0xFE,
        "To think a legendary dragon would appear...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A42")

    label("loc_9BE")


    ChrTalk(    #17
        0xFE,
        "To think a legendary dragon would appear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "It seems She Above doesn't want the\x01",
            "Royal Army to have an easy time of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A42")

    Jump("loc_11A3")

    label("loc_A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_C4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B1A")

    ChrTalk(    #19
        0xFE,
        (
            "With the uprising in Grancel stopped,\x01",
            "the Intelligence Division's insurrection\x01",
            "has finally, truly ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "We men of the border garrison can finally\x01",
            "sleep the sleep of the just, for once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C49")

    label("loc_B1A")


    ChrTalk(    #21
        0xFE,
        (
            "I was surprised that Amalthea and the\x01",
            "rest of the Intelligence Division\x01",
            "were bold enough for one more attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "But with their defeat, the threat of\x01",
            "insurrection within the kingdom has\x01",
            "truly ended at last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "We men of the border garrison can finally\x01",
            "sleep the sleep of the just, for once.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C49")

    Jump("loc_11A3")

    label("loc_C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_DF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D35")

    ChrTalk(    #24
        0xFE,
        (
            "Apparently a member of a criminal organization\x01",
            "infiltrated the royal academy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "The Capuas, the I.D. insurrectionists, and\x01",
            "now this 'Ouroboros.' We can't let our guard\x01",
            "down for a moment with these criminals!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF4")

    label("loc_D35")

    OP_A2(0x0)

    ChrTalk(    #26
        0xFE,
        (
            "Apparently a member of a criminal organization\x01",
            "infiltrated the royal academy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "It's an organization that command is evidently\x01",
            "worried about. We're keeping an eye out,\x01",
            "never fear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF4")

    Jump("loc_11A3")

    label("loc_DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_F3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E77")

    ChrTalk(    #28
        0xFE,
        (
            "The Ruan mayoral race is just about\x01",
            "to come to a vote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "I hope the election, at least, goes smoothly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F38")

    label("loc_E77")

    OP_A2(0x0)

    ChrTalk(    #30
        0xFE,
        (
            "The Ruan mayoral race is just about\x01",
            "to come to a vote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "There hasn't been any outright chaos,\x01",
            "but the election's running white hot,\x01",
            "as they say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Hopefully nothing will happen.\x02",
    )

    CloseMessageWindow()

    label("loc_F38")

    Jump("loc_11A3")

    label("loc_F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_11A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1010")

    ChrTalk(    #33
        0xFE,
        (
            "The Royal Army remains at a very high\x01",
            "state of general alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Mostly because we don't know the location\x01",
            "of the Capua sky bandits or the remaining\x01",
            "Intelligence Division insurrectionists.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A3")

    label("loc_1010")

    OP_A2(0x0)

    ChrTalk(    #35
        0xFE,
        (
            "The Royal Army remains at a very high\x01",
            "state of general alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Mostly because we don't know the location\x01",
            "of the Capua sky bandits or the remaining\x01",
            "Intelligence Division insurrectionists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Even setting the Capua gang aside, those\x01",
            "I.D. rebels are quite a problem on their own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Say whatever else you will about them,\x01",
            "they're also highly trained killers.\x01",
            "We need to find and stop them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A3")

    TalkEnd(0xFE)
    Return()

    # Function_3_50D end

    def Function_4_11A7(): pass

    label("Function_4_11A7")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1346")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129A")

    ChrTalk(    #39
        0x9,
        (
            "The biggest problem I have with the\x01",
            "orbments not working is that it interferes\x01",
            "with my cooking hobby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "Not being able to use the stove?\x01",
            "It's awful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "I wish we could get another of those\x01",
            "generators somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1343")

    label("loc_129A")


    ChrTalk(    #42
        0x9,
        (
            "The biggest problem I have with the\x01",
            "orbments not working is that it interferes\x01",
            "with my cooking hobby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "I wish we could get another of those\x01",
            "generators somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1343")

    Jump("loc_2850")

    label("loc_1346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_14BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142E")

    ChrTalk(    #44
        0x9,
        (
            "Those crimson soldiers who attacked\x01",
            "earlier had armored beasts with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "We don't know who they are,\x01",
            "but they're extremely strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "If they hit us again, I'm not sure we\x01",
            "could hold, to be honest.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_14BB")

    label("loc_142E")


    ChrTalk(    #47
        0x9,
        (
            "Those crimson soldiers who attacked\x01",
            "earlier had armored beasts with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "I wish we could get another of those\x01",
            "generators somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14BB")

    Jump("loc_2850")

    label("loc_14BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_16C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_15A2")

    ChrTalk(    #49
        0x9,
        (
            "I heard that the guild's been supporting\x01",
            "us even in this most recent incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "Personally, I think the brass absolutely\x01",
            "has the right idea, trying to deepen our\x01",
            "relationship with the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C2")

    label("loc_15A2")


    ChrTalk(    #51
        0x9,
        "Hello! How goes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "I heard that the guild's been supporting\x01",
            "us even in this most recent incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "Personally, I think the brass absolutely\x01",
            "has the right idea, trying to deepen our\x01",
            "relationship with the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "If we worked together, we'd both\x01",
            "be much stronger for it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_16C2")

    Jump("loc_1BA9")

    label("loc_16C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_180C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_176E")

    ChrTalk(    #55
        0x9,
        (
            "That dragon's apparently fled deep into\x01",
            "Nebel Valley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "Getting an airship in there is impossible;\x01",
            "the fog's too deep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        "Hmph. Clever beast.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1809")

    label("loc_176E")


    ChrTalk(    #58
        0x9,
        (
            "That dragon's apparently fled deep into\x01",
            "Nebel Valley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "Getting an airship in there is impossible;\x01",
            "the fog's too deep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        "Hmph. Clever beast.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1809")

    Jump("loc_1BA9")

    label("loc_180C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_18A6")

    ChrTalk(    #61
        0x9,
        "We haven't had to be as alert recently.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "I'm glad we can finally return to business\x01",
            "as normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        "I finally have time to cook again!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BA9")

    label("loc_18A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_19C2")

    ChrTalk(    #64
        0x9,
        (
            "By the way, we did get word from the guild\x01",
            "about what happened at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "Another suspicious individual, probably a\x01",
            "member of some criminal organization,\x01",
            "was hiding on the old grounds?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "One disaster after another, isn't it?\x01",
            "No rest for heroes, I suppose!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA9")

    label("loc_19C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1AA1")

    ChrTalk(    #67
        0x9,
        (
            "The strength of the monsters lately has\x01",
            "been on everyone's mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "We actually gave shelter to a junior bracer not\x01",
            "too long ago. Poor fellow was very nearly killed\x01",
            "by the beasts wandering the countryside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA9")

    label("loc_1AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1BA9")

    ChrTalk(    #69
        0x9,
        "The post's watch is as severe as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "We're surrounded by threats, after all.\x01",
            "The Intelligence Division remnants are\x01",
            "spread all over the country, for starters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "As hard as it is to admit, we'll need the\x01",
            "guild's help to bring them to justice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA9")

    Jump("loc_2850")

    label("loc_1BAC")

    OP_A2(0x122C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_237B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1F66")

    ChrTalk(    #72
        0x9,
        "Oho! Hello, friends!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x106,
        (
            "#051FHey, Serose.\x01",
            "How's the border treatin' you?\x02\x03",

            "Haven't seen you since that incident\x01",
            "with those monster mutts.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C94")

    ChrTalk(    #74
        0x103,
        "#023FOh? I never heard anything about this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D03")

    label("loc_1C94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CD8")

    ChrTalk(    #75
        0x104,
        "#033FOh? An adventure I am not familiar with?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D03")

    label("loc_1CD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D03")

    ChrTalk(    #76
        0x108,
        "#073FWhat's this about?\x02",
    )

    CloseMessageWindow()

    label("loc_1D03")


    ChrTalk(    #77
        0x101,
        (
            "#1015FYeah, it was the first time Joshua and I fought\x01",
            "alongside Agate. We drove off the Intelligence\x01",
            "Division's dog monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        "Haha, yes, they were a big help!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        "So what brings you around here today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x106,
        (
            "#050FA guild job to hunt a wanted monster,\x01",
            "actually.\x02\x03",

            "Figured we'd stop by and stretch the\x01",
            "legs a bit since we were out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        "Ah, well, good luck with that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "And that being the case, feel free to\x01",
            "use the facilities to rest if you need to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        (
            "The monsters have been hell lately.\x01",
            "I think I preferred those dog things!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1001FHaha, no kidding.\x01",
            "Thanks, we'll take you up on that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2378")

    label("loc_1F66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2378")
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x106, 0)
    Sleep(400)

    ChrTalk(    #85
        0x9,
        "Oho! Hello, friends!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x106,
        (
            "#051FHey, Serose.\x01",
            "How's the border treatin' you?\x02\x03",

            "Haven't seen you since that incident\x01",
            "with those monster mutts.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2059")

    ChrTalk(    #87
        0x107,
        "#064FOh, wow, I never heard about that!\x02",
    )

    CloseMessageWindow()
    Jump("loc_210A")

    label("loc_2059")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_209B")

    ChrTalk(    #88
        0x103,
        "#023FOh? I never heard anything about this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_210A")

    label("loc_209B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20DF")

    ChrTalk(    #89
        0x104,
        "#033FOh? An adventure I am not familiar with?\x02",
    )

    CloseMessageWindow()
    Jump("loc_210A")

    label("loc_20DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_210A")

    ChrTalk(    #90
        0x108,
        "#073FWhat's this about?\x02",
    )

    CloseMessageWindow()

    label("loc_210A")


    ChrTalk(    #91
        0x101,
        (
            "#1015FYeah, it was the first time Joshua and I fought\x01",
            "alongside Agate. We drove off the Intelligence\x01",
            "Division's dog monsters.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #92
        0x9,
        "Haha, yes, they were a big help!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        "So what brings you around here today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x106,
        (
            "#050FA guild job to hunt a wanted monster,\x01",
            "actually.\x02\x03",

            "Figured we'd stop by and stretch the\x01",
            "legs a bit since we were out here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)

    ChrTalk(    #95
        0x9,
        "Ah, well, good luck with that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x9,
        (
            "And that being the case, feel free to\x01",
            "use the facilities to rest if you need to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x9,
        (
            "The monsters have been hell lately.\x01",
            "I think I preferred those dog things!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1006FHaha, no kidding.\x01",
            "Thanks, we'll take you up on that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2378")

    Jump("loc_2850")

    label("loc_237B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_248D")

    ChrTalk(    #99
        0x9,
        "Oho! Hello, friends!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x106,
        (
            "#051FHey, Serose.\x01",
            "How's the border treatin' you?\x02\x03",

            "Haven't seen you since that incident\x01",
            "with those monster mutts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        (
            "#1011FOh, yeah, I remember that!\x02\x03",

            "#1015FThat was actually the first time we\x01",
            "fought together with Agate, wasn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25CB")

    label("loc_248D")

    TurnDirection(0x9, 0x101, 0)

    ChrTalk(    #102
        0x9,
        "Oho! Hello, friends!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#1011FOh, hey, Serose!\x02\x03",

            "I think we saw each other last when we\x01",
            "fought those dog monster things, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x103,
        "#023FOh? I never heard anything about this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1006FIt was back when we first fought together\x01",
            "with Agate. We drove off some of the\x01",
            "Intelligence Division's dog monsters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25CB")


    ChrTalk(    #106
        0x9,
        "Haha, yes, they were a big help!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        "So what brings you around here today?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2681")

    ChrTalk(    #108
        0x106,
        (
            "#050FJust stretchin' our legs a bit and gettin'\x01",
            "back into form. Figured we'd come by.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26EA")

    label("loc_2681")


    ChrTalk(    #109
        0x103,
        (
            "#020FWe're just on a bit of a warm-up lap\x01",
            "before getting to serious work, and\x01",
            "thought we'd stop by.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26EA")


    ChrTalk(    #110
        0x9,
        "Ahh, I see, a bit of bracer training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x9,
        (
            "Well, since you came all the way out\x01",
            "here, feel free to use the facilities to\x01",
            "rest if you need to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        (
            "You want to talk about monsters, the\x01",
            "ones on the roads lately have been\x01",
            "ridiculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1001FThanks! We'll do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        "I'll get back to work, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x9,
        (
            "If I can help with anything,\x01",
            "just give the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2850")

    TalkEnd(0x9)
    Return()

    # Function_4_11A7 end

    def Function_5_2854(): pass

    label("Function_5_2854")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_29DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2949")

    ChrTalk(    #116
        0xFE,
        (
            "Our guns not working is, like,\x01",
            "really, really bad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "I mean, aside from the officers, none of\x01",
            "us have any REAL hand-to-hand training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "If those guys in red attack again, how\x01",
            "are we supposed to drive them off?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_29D7")

    label("loc_2949")


    ChrTalk(    #119
        0xFE,
        (
            "Our guns not working is, like,\x01",
            "really, really bad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "I mean, aside from the officers, none of\x01",
            "us have any REAL hand-to-hand training.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29D7")

    Jump("loc_33EC")

    label("loc_29DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2B6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE9")

    ChrTalk(    #121
        0xFE,
        (
            "Weird things are showing up in the sky,\x01",
            "and we can't use our guns...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "Really feels like Liberl's in a heck of a pinch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "If Erebonia tried to invade us in the\x01",
            "middle of all this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "...I-I'd rather not think about that,\x01",
            "to be honest!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2B69")

    label("loc_2AE9")


    ChrTalk(    #125
        0xFE,
        (
            "Weird things are showing up in the sky,\x01",
            "and we can't use our guns...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "Really feels like Liberl's in a heck of a pinch.\x02",
    )

    CloseMessageWindow()

    label("loc_2B69")

    Jump("loc_33EC")

    label("loc_2B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2C25")

    ChrTalk(    #127
        0xFE,
        (
            "I haven't heard all the details, but it\x01",
            "sounds like that whole mess with the\x01",
            "dragon is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "Yeah, you can count on General Morgan\x01",
            "to take care of things like that!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33EC")

    label("loc_2C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2DB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2CB6")

    ChrTalk(    #129
        0xFE,
        (
            "The dragon's in Nebel Valley, so why\x01",
            "are WE on alert?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "The army's pretty inefficient when it\x01",
            "comes to stuff like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DAE")

    label("loc_2CB6")


    ChrTalk(    #131
        0xFE,
        (
            "*sigh* If we're on alert, that means the\x01",
            "night patrols are back on. Yay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "But the dragon's in Nebel Valley, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "Why the hell does the Krone Pass have\x01",
            "to be on alert for stuff on the other side\x01",
            "of Bose? That's what I wanna know!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2DAE")

    Jump("loc_33EC")

    label("loc_2DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_30A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 3)), scpexpr(EXPR_END)), "loc_2E58")

    ChrTalk(    #134
        0xFE,
        (
            "At this point, the only pleasure left to\x01",
            "us is Officer Serose's cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "He always says, 'Oh, it's just a hobby,'\x01",
            "but he's seriously a pro.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A1")

    label("loc_2E58")


    ChrTalk(    #136
        0xFE,
        "Aaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "Er, yeah, hi! I was gonna read this\x01",
            "over dinner, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "Well, I got so into it I burned right\x01",
            "through it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "There's not much to do for fun here at\x01",
            "a posting like this, so you tend to blow\x01",
            "through that sort of thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        "Anyway, here, might as well share, right?\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xF, 0x80)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #141
        "\x07\x00Received #576i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x240, 1)
    OP_A2(0x10BB)
    OP_0D()

    ChrTalk(    #142
        0xFE,
        (
            "At this point, the only pleasure left to\x01",
            "us is Officer Serose's cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "He always says, 'Oh, it's just a hobby,'\x01",
            "but he's seriously a pro.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "Lately he's had some time and\x01",
            "has been in the kitchen a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A1")

    Jump("loc_33EC")

    label("loc_30A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_31A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_311C")

    ChrTalk(    #145
        0xFE,
        (
            "Officer Serose is on kitchen duty today!\x01",
            "Lucky!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "I'm so happy... I can't wait for dinner now!\x02",
    )

    CloseMessageWindow()
    Jump("loc_31A6")

    label("loc_311C")

    OP_A2(0x2)

    ChrTalk(    #147
        0xFE,
        (
            "Officer Serose is on kitchen duty today!\x01",
            "Lucky!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "I wonder what he's going to make.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "Oh, man, now I can't wait for dinner!\x02",
    )

    CloseMessageWindow()

    label("loc_31A6")

    Jump("loc_33EC")

    label("loc_31A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_3240")

    ChrTalk(    #150
        0xFE,
        (
            "We're stocked on firewood, and I've\x01",
            "checked over our food supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "All done, thank Aidios!\x01",
            "Now I can relax until the next patrol.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33EC")

    label("loc_3240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_33EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_32E3")

    ChrTalk(    #152
        0xFE,
        (
            "About the only pleasure we have up\x01",
            "here is Officer Serose's cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "If he ever leaves the service, he\x01",
            "should definitely become a chef!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33EC")

    label("loc_32E3")

    OP_A2(0x2)

    ChrTalk(    #154
        0xFE,
        (
            "*sigh* It's hard up here in the mountains\x01",
            "with so little to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "I heard a new casino opened in Ruan, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "About the only pleasure we have up\x01",
            "here is Officer Serose's cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "If he ever leaves the service, he\x01",
            "should definitely become a cook!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33EC")

    TalkEnd(0xFE)
    Return()

    # Function_5_2854 end

    def Function_6_33F0(): pass

    label("Function_6_33F0")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_35A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3505")

    ChrTalk(    #158
        0xA,
        (
            "We've stepped up security here, but it's\x01",
            "kinda pointless if nobody actually comes\x01",
            "through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xA,
        (
            "It's not like there's anybody on the roads\x01",
            "these days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xA,
        (
            "If anyone comes through here, they're either\x01",
            "crazy or bracers... Er, begging your pardon!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_35A3")

    label("loc_3505")


    ChrTalk(    #161
        0xA,
        (
            "We've stepped up security here, but it's\x01",
            "kinda pointless if nobody actually comes\x01",
            "through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xA,
        (
            "It's not like there's anybody on the roads\x01",
            "these days...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A3")

    Jump("loc_3CE9")

    label("loc_35A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_373B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36ED")

    ChrTalk(    #163
        0xA,
        (
            "Since we can't shut the gate, we're being real\x01",
            "strict about stopping people and questioning\x01",
            "them before they pass through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xA,
        (
            "You bracers are free to pass whenever\x01",
            "you want, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xA,
        (
            "Word came down from the brass--we're\x01",
            "cooperating with the guild during this mess,\x01",
            "so you guys have free access.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_3738")

    label("loc_36ED")


    ChrTalk(    #166
        0xA,
        (
            "You bracers are free to pass as you wish.\x01",
            "We got word from the brass.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3738")

    Jump("loc_3CE9")

    label("loc_373B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_37BD")

    ChrTalk(    #167
        0xA,
        (
            "Looks like the dragon's calmed down.\x01",
            "Thank Aidios for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xA,
        "It better, the whole Air Force is gunning for it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CE9")

    label("loc_37BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_38DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_383A")

    ChrTalk(    #169
        0xA,
        "First it's traitors, now it's a DRAGON.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xA,
        (
            "Seriously. Can things not be crazy?\x01",
            "For one freakin' day?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D8")

    label("loc_383A")


    ChrTalk(    #171
        0xA,
        "Aaaaand once again we're on alert status.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xA,
        "First it's traitors, now it's a DRAGON.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xA,
        (
            "Seriously. Can things not be crazy?\x01",
            "For one freakin' day?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_38D8")

    Jump("loc_3CE9")

    label("loc_38DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3A79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3996")

    ChrTalk(    #174
        0xA,
        (
            "Heard Norman got elected as the\x01",
            "new mayor of Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xA,
        (
            "He's mostly all about turning Ruan into\x01",
            "a tourist spot, but he's promised to not\x01",
            "totally neglect the harbor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A76")

    label("loc_3996")


    ChrTalk(    #176
        0xA,
        (
            "Heard Norman got elected as the\x01",
            "new mayor of Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xA,
        (
            "He's mostly all about turning Ruan into\x01",
            "a tourist spot, but he's promised to not\x01",
            "totally neglect the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        "Like they say, I guess--balance is important.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3A76")

    Jump("loc_3CE9")

    label("loc_3A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_3B60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3ADB")

    ChrTalk(    #179
        0xA,
        (
            "Maaan, I wish they'd hurry up and round\x01",
            "up all those I.D. traitors already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B5D")

    label("loc_3ADB")

    OP_A2(0x1)

    ChrTalk(    #180
        0xA,
        (
            "I mean, how long are we gonna\x01",
            "have to be on alert for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xA,
        (
            "The cold really seeps into you\x01",
            "when you go on a night patrol.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B5D")

    Jump("loc_3CE9")

    label("loc_3B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_3C18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3BB8")

    ChrTalk(    #182
        0xA,
        (
            "Well, I get paid the same whether\x01",
            "or not I work, so I don't care!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C15")

    label("loc_3BB8")

    OP_A2(0x1)

    ChrTalk(    #183
        0xA,
        (
            "We don't get many travelers on foot these\x01",
            "days, so we've left the counter unstaffed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C15")

    Jump("loc_3CE9")

    label("loc_3C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_3CE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3C77")

    ChrTalk(    #184
        0xA,
        (
            "Do you guys have some kind of abnormal\x01",
            "love of walking in the mountains?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE9")

    label("loc_3C77")

    OP_A2(0x1)

    ChrTalk(    #185
        0xA,
        (
            "You guys came all the way out here\x01",
            "just by WALKING?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xA,
        "Guess there are still crazy people in the world!\x02",
    )

    CloseMessageWindow()

    label("loc_3CE9")

    TalkEnd(0xA)
    Return()

    # Function_6_33F0 end

    def Function_7_3CED(): pass

    label("Function_7_3CED")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_3D01")
    Call(1, 0)
    Jump("loc_4752")

    label("loc_3D01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_3E5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3D75")

    ChrTalk(    #187
        0xFE,
        "I'm still studying this facility.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        "I'm sorry, but could you not interrupt me?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E16")

    label("loc_3D75")


    ChrTalk(    #189
        0xFE,
        "Ah, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "Did you have some, um, business with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        "I'm still, er, studying the facility.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        "I'm sorry, but could you not interrupt me?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3E16")

    Jump("loc_3E59")

    label("loc_3E19")


    ChrTalk(    #193
        0xFE,
        "I'm going to keep observing things here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        "Excuse me...\x02",
    )

    CloseMessageWindow()

    label("loc_3E59")

    Jump("loc_4752")

    label("loc_3E5C")


    ChrTalk(    #195
        0xFE,
        "Phew! Glad I managed to get this far!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        "Oh, but I can't stay here forever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "I've got to figure out SOME way to\x01",
            "get back to Jenis, or Heimdall, or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        (
            "#1019F(Who in the...)\x02\x03",

            "#1015F(Wait, that's...)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(    #199
        0xFE,
        "Oh!\x02",
    )

    CloseMessageWindow()
    Sleep(700)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(400)

    ChrTalk(    #200
        0xFE,
        "Estelle! Estelle Bright, hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "Do you remember me?\x01",
            "I'm Felicity, from the academy!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_417F")

    ChrTalk(    #202
        0x101,
        "#1018FOh, yeah! Of course I remember!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x105,
        (
            "#040FHello, Felicity!\x02\x03",

            "I hardly imagined I'd meet you here!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #204
        0xFE,
        (
            "K-Kloe?! I could say the same!\x01",
            "Hi!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "What the heck brings you two out here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        (
            "#1006FWe've got a guild job to take care of\x01",
            "some monsters on the roads, and\x01",
            "Kloe's been helping us.\x02\x03",

            "I could sorta ask you the same, though!\x01",
            "A Royal Army guard post isn't exactly\x01",
            "the campus quad!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F0")

    label("loc_417F")


    ChrTalk(    #207
        0x101,
        (
            "#1001FOh, yeah! Of course!\x02\x03",

            "I haven't seen you since the\x01",
            "ghost mess at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "Yes, I'm honored to have the chance\x01",
            "to meet you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "Incidentally, what brings you here today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        (
            "#1006FWe've got a guild job to take care\x01",
            "of some monsters on the roads.\x02\x03",

            "I could sorta ask you the same, though!\x01",
            "A Royal Army guard post isn't exactly\x01",
            "the campus quad!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F0")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #211
        0xFE,
        "Er! Well! Umm.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #212
        0x101,
        "#1015FHuh? What is it?\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #213
        0xFE,
        "Er, nothing! Nothing at all.\x02",
    )

    CloseMessageWindow()
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #214
        0xFE,
        (
            "What am I doing here!\x01",
            "Yes, er, that is...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #215
        0xFE,
        (
            "Er, social observation! Yes!\x01",
            "I'm here to study this guard post!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "I've been thinking of writing a paper on the\x01",
            "social dynamics of a Royal Army guard post\x01",
            "for a holiday research assignment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x101,
        "#1004FOh, wow. I see, that's really clever!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_454D")

    ChrTalk(    #218
        0x105,
        (
            "#044FA holiday...?\x02\x03",

            "(Wait, I don't remember an assignment\x01",
            "like that...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_467D")

    label("loc_454D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45D5")

    ChrTalk(    #219
        0x107,
        (
            "#560FYou're doing a social studies kind of research?\x02\x03",

            "That's neat! I always wanted to\x01",
            "do research on my own, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_467D")

    label("loc_45D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_463C")

    ChrTalk(    #220
        0x103,
        (
            "#021FJust what I'd expect of a student\x01",
            "of the kingdom's most prestigious school.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_467D")

    label("loc_463C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_467D")

    ChrTalk(    #221
        0x108,
        "#070FMakes sense for a royal academy student.\x02",
    )

    CloseMessageWindow()

    label("loc_467D")


    ChrTalk(    #222
        0xFE,
        (
            "Ahem, yes, well! I was just in the middle\x01",
            "of recording my observations, so...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #223
        0x101,
        (
            "#1008FOh, sorry! Didn't mean to get in your way.\x02\x03",

            "#1006FWe'll see you later, then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        "Y-Yes. Another time.\x02",
    )

    CloseMessageWindow()
    OP_28(0x7A, 0x1, 0x4000)
    OP_A2(0x4)

    label("loc_4752")

    TalkEnd(0xC)
    Return()

    # Function_7_3CED end

    def Function_8_4756(): pass

    label("Function_8_4756")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DCB")

    ChrTalk(    #225
        0xFE,
        (
            "Hey, bracerfolks!\x01",
            "Fancy meeting you guys here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4815")
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #226
        0x107,
        (
            "#064FR-Ray?!\x02\x03",

            "Hey, hey, how did things go?\x01",
            "You know, with the ship?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)
    OP_A2(0x20B0)
    Jump("loc_4888")

    label("loc_4815")


    ChrTalk(    #227
        0x101,
        (
            "#1004FHuh? ...OH!\x01",
            "You're from the central factory, right?\x02\x03",

            "What are you doing way up in the mountains?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    label("loc_4888")


    ChrTalk(    #228
        0xFE,
        (
            "I was heading back to Zeiss after\x01",
            "working on the Arseille a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "I finished helping the old man, so it's\x01",
            "time to get back to my own experiments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x101,
        (
            "#1016FWhich means you have to walk.\x01",
            "Right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x102,
        (
            "#1035FUnfortunately, it's the only way to travel\x01",
            "right now.\x02\x03",

            "#1040FAre you sure you'll be safe traveling alone?\x01",
            "We could escort you, if you like.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #232
        0xFE,
        (
            "Heh, don't worry.\x01",
            "I'm not exactly alone, as it were.\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0xE, 255)
    TurnDirection(0xE, 0x0, 400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #233
        0xE,
        "Nya-o.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #234
        0x101,
        "#1001FAhaha! Antoine's with you, huh.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #235
        0xFE,
        "Pretty loyal for a cat, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "I've also got...you might call 'em\x01",
            "'hazardous materials' on hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "Here, let me share some with you,\x01",
            "show you what I mean.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #238
        "\x07\x00Received #486i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x1E6, 1)

    ChrTalk(    #239
        0xFE,
        "It's an attack food I invented!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "You can make it with the tools from any\x01",
            "old kitchen, so if you have the time and\x01",
            "materials, give it a try.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x45)"), scpexpr(EXPR_END)), "loc_4C10")
    Jump("loc_4C59")

    label("loc_4C10")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #241
        "\x07\x00Learned [#486i] recipe.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_4C59")

    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #242
        0x101,
        (
            "#1016FUh... Thanks!\x02\x03",

            "#1015FSo...yeah.\x02\x03",

            "I kinda think they'll make it just fine,\x01",
            "guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x102,
        (
            "#1048FQu-Quite so...\x02\x03",

            "#1040FStill, be careful on your way, Ray.\x02\x03",

            "The Kaldia Tunnel is likely to be\x01",
            "especially dangerous right now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #244
        0xFE,
        (
            "Yeah, don't worry, I'm keeping both\x01",
            "eyes open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "Anyway, see you guys back in Zeiss!\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #246
        0xE,
        "Nya～on.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 0, 400)
    OP_4B(0xE, 255)
    OP_A2(0x20AF)
    Jump("loc_4E95")

    label("loc_4DCB")


    ChrTalk(    #247
        0xFE,
        (
            "I finished helping the old man, so it's\x01",
            "time to get back to my own experiments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "After all, can't leave the greenhouse to\x01",
            "Terry forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "Anyway, safe travels, guys.\x01",
            "I'll see you in Zeiss!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E95")

    TalkEnd(0xD)
    Return()

    # Function_8_4756 end

    def Function_9_4E99(): pass

    label("Function_9_4E99")

    TalkBegin(0xE)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #250
        0xFE,
        "Nya～on.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_9_4E99 end

    def Function_10_4EB3(): pass

    label("Function_10_4EB3")

    Call(0, 4)
    Return()

    # Function_10_4EB3 end

    def Function_11_4EB8(): pass

    label("Function_11_4EB8")

    Call(0, 6)
    Return()

    # Function_11_4EB8 end

    def Function_12_4EBD(): pass

    label("Function_12_4EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50C6")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4FBC")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F4D")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #251
        0x103,
        (
            "#020FThe Bose region lies beyond here.\x02\x03",

            "We want to head for Zeiss.\x01",
            "Let's take a passenger ship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB9")

    label("loc_4F4D")

    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #252
        0x103,
        (
            "#020FThe Bose region lies beyond here.\x02\x03",

            "We want to head for Zeiss.\x01",
            "Let's take a passenger ship.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FB9")

    Jump("loc_50A8")

    label("loc_4FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_50A8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_503D")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #253
        0x106,
        (
            "#050FThis leads to the Bose region.\x02\x03",

            "It's Zeiss we're goin' to.\x01",
            "Let's hop on a passenger ship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50A8")

    label("loc_503D")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #254
        0x106,
        (
            "#050FThis leads to the Bose region.\x02\x03",

            "It's Zeiss we're goin' to.\x01",
            "Let's hop on a passenger ship.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50A8")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_535C")

    label("loc_50C6")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_51F1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5166")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #255
        0x103,
        (
            "#020FThe Bose region lies beyond here.\x02\x03",

            "We don't have time to head for other regions.\x01",
            "Let's focus on our work here in Ruan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51EE")

    label("loc_5166")

    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #256
        0x103,
        (
            "#020FThe Bose region lies beyond here.\x02\x03",

            "We don't have time to head for other regions.\x01",
            "Let's focus on our work here in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51EE")

    Jump("loc_5341")

    label("loc_51F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5341")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52A4")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #257
        0x106,
        (
            "#050FThis leads to the Bose region.\x02\x03",

            "We got enough to be gettin' on with\x01",
            "without heading to other regions.\x01",
            "Let's focus on our work here in Ruan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5341")

    label("loc_52A4")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #258
        0x106,
        (
            "#050FThis leads to the Bose region.\x02\x03",

            "We got enough to be gettin' on with\x01",
            "without heading to other regions.\x01",
            "Let's focus on our work here in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5341")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_535C")

    Return()

    # Function_12_4EBD end

    def Function_13_535D(): pass

    label("Function_13_535D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_5670")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53DD")
    TurnDirection(0x108, 0x0, 400)

    ChrTalk(    #259
        0x108,
        (
            "#070FHm? Beyond here lies Ruan, yes?\x02\x03",

            "Our business does not lie this way.\x01",
            "Let us turn back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_566D")

    label("loc_53DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_544E")
    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #260
        0x109,
        (
            "#1060FRuan's this way, right?\x02\x03",

            "We don't have much to do out there.\x01",
            "Let's turn back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_566D")

    label("loc_544E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54F3")
    TurnDirection(0x104, 0x0, 400)

    ChrTalk(    #261
        0x104,
        (
            "#030FHmm... Ruan's bountiful seas lie beyond.\x02\x03",

            "As much as the turquoise waters call to me,\x01",
            "we have no business there. Let us turn back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_566D")

    label("loc_54F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_557B")
    TurnDirection(0x105, 0x0, 400)

    ChrTalk(    #262
        0x105,
        (
            "#040FEstelle, this leads to Ruan.\x02\x03",

            "I don't believe we have any business there,\x01",
            "do we? We should turn back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_566D")

    label("loc_557B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55EC")
    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #263
        0x106,
        (
            "#050FThis way leads to Ruan.\x02\x03",

            "There's nothing we need to do there.\x01",
            "Let's turn back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_566D")

    label("loc_55EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_566D")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #264
        0x103,
        (
            "#020FRuan lies beyond here.\x02\x03",

            "We don't really have a reason to head\x01",
            "that way. How about we turn around?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_566D")

    Jump("loc_587D")

    label("loc_5670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_5769")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56F4")

    ChrTalk(    #265
        0x108,
        (
            "#070FHm? Beyond here lies Ruan, yes?\x02\x03",

            "Our priority is pursuing the dragon.\x01",
            "Let us head for Nebel Valley.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5766")

    label("loc_56F4")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #266
        0x106,
        (
            "#050FThis way leads to Ruan.\x02\x03",

            "Right now we got a dragon to chase.\x01",
            "Nebel Valley's to the east of here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5766")

    Jump("loc_587D")

    label("loc_5769")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57E6")

    ChrTalk(    #267
        0x108,
        (
            "#070FBeyond here lies Ruan, right?\x02\x03",

            "We do not really have time to visit\x01",
            "other regions. Let us turn back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_587D")

    label("loc_57E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57FC")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_5803")

    label("loc_57FC")

    TurnDirection(0x106, 0x0, 400)

    label("loc_5803")


    ChrTalk(    #268
        0x106,
        (
            "#050FThis way leads to Ruan.\x02\x03",

            "We got enough to be gettin' on with without\x01",
            "heading to other regions. Let's turn back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_587D")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_13_535D end

    def Function_14_5899(): pass

    label("Function_14_5899")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58FF")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #269
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_5ABA")

    label("loc_58FF")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #270
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A9F")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 18440, 1000, 12120, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x32)
    OP_73(0x5)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x5, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_5A9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AB9")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_5AB9")

    Return()

    label("loc_5ABA")

    Return()

    # Function_14_5899 end

    SaveToFile()

Try(main)
