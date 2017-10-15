from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3119   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3119.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T3119   ._SN',
            'ED6_DT21/T3119_1 ._SN',
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
        'Professor Russell',                    # 9
        'Factory Chief Murdock',                # 10
        'Supervisor Travis',                    # 11
        'Hazel',                                # 12
        'Wilmont',                              # 13
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
        'ED6_DT07/CH02020 ._CH',             # 00
        'ED6_DT07/CH02620 ._CH',             # 01
        'ED6_DT07/CH01190 ._CH',             # 02
        'ED6_DT07/CH01540 ._CH',             # 03
        'ED6_DT07/CH01450 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT07/CH02620P._CP',             # 01
        'ED6_DT07/CH01190P._CP',             # 02
        'ED6_DT07/CH01540P._CP',             # 03
        'ED6_DT07/CH01450P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -440,
        Z                   = 0,
        Y                   = 10490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4650,
        Z                   = 1000,
        Y                   = 6180,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclEvent(
        X                   = -106990,
        Y                   = 0,
        Z                   = -550,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 17,
    )


    DeclActor(
        TriggerX            = -540,
        TriggerZ            = 0,
        TriggerY            = 6300,
        TriggerRange        = 800,
        ActorX              = -540,
        ActorZ              = 900,
        ActorY              = 6300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1B6",          # 00, 0
        "Function_1_243",          # 01, 1
        "Function_2_374",          # 02, 2
        "Function_3_41B",          # 03, 3
        "Function_4_FBD",          # 04, 4
        "Function_5_11D0",         # 05, 5
        "Function_6_1CBD",         # 06, 6
        "Function_7_39B1",         # 07, 7
        "Function_8_3A00",         # 08, 8
        "Function_9_3A4F",         # 09, 9
        "Function_10_3A9E",        # 0A, 10
        "Function_11_3AED",        # 0B, 11
        "Function_12_546B",        # 0C, 12
        "Function_13_54F1",        # 0D, 13
        "Function_14_553D",        # 0E, 14
        "Function_15_756E",        # 0F, 15
        "Function_16_7606",        # 10, 16
        "Function_17_766C",        # 11, 17
    )


    def Function_0_1B6(): pass

    label("Function_0_1B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C0")
    Jump("loc_204")

    label("loc_1C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_204")
    SetChrPos(0x8, -480, 0, 10270, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xA, 4650, 1000, 6340, 90)
    SetChrPos(0xC, 2300, 0, 7700, 90)

    label("loc_204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_21E")
    OP_A3(0x10F0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)
    Jump("loc_242")

    label("loc_21E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_242")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_242")
    Event(0, 6)

    label("loc_242")

    Return()

    # Function_0_1B6 end

    def Function_1_243(): pass

    label("Function_1_243")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EC")
    OP_6F(0x8, 0)
    OP_72(0x8, 0x10)
    OP_6F(0x5, 29)
    OP_72(0x5, 0x10)
    OP_6F(0x6, 29)
    OP_72(0x6, 0x10)
    OP_6F(0x7, 29)
    OP_72(0x7, 0x10)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x11, 0x4)
    OP_79(0xFF, 0x2)
    OP_7A(0x1F, 0x2)
    OP_7B()
    OP_72(0x13, 0x4)
    OP_72(0x14, 0x4)
    OP_10(0x0, 0x0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x4, 0x4)
    OP_64(0x0, 0x1)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_71(0x12, 0x4)
    OP_71(0x12, 0x4)
    Jump("loc_373")

    label("loc_2EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_30F")
    OP_72(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_71(0x12, 0x4)
    Jump("loc_373")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_332")
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x12, 0x4)
    Jump("loc_373")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35A")
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x12, 0x4)
    Jump("loc_373")

    label("loc_35A")

    OP_72(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_71(0x12, 0x4)

    label("loc_373")

    Return()

    # Function_1_243 end

    def Function_2_374(): pass

    label("Function_2_374")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3A5"),
        (1, "loc_3B1"),
        (2, "loc_3BD"),
        (3, "loc_3C9"),
        (4, "loc_3D5"),
        (5, "loc_3E1"),
        (6, "loc_3ED"),
        (SWITCH_DEFAULT, "loc_3F9"),
    )


    label("loc_3A5")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_405")

    label("loc_3B1")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_405")

    label("loc_3BD")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_405")

    label("loc_3C9")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_405")

    label("loc_3D5")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_405")

    label("loc_3E1")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_405")

    label("loc_3ED")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_405")

    label("loc_3F9")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_405")

    label("loc_405")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_405")

    label("loc_41A")

    Return()

    # Function_2_374 end

    def Function_3_41B(): pass

    label("Function_3_41B")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_5BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53D")

    ChrTalk(    #0
        0xFE,
        (
            "The professor's out, and I don't know\x01",
            "where he went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I'm sure at this point he's all worked\x01",
            "up and researching this phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Yeah, I'd better do my best too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I may not hold a candle to the professor,\x01",
            "but there should still be plenty I can do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5B8")

    label("loc_53D")


    ChrTalk(    #4
        0xFE,
        (
            "I'm sure the professor's all geared up\x01",
            "up and researching this phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "I'd better do the best I can as well.\x02",
    )

    CloseMessageWindow()

    label("loc_5B8")

    Jump("loc_FB9")

    label("loc_5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_72B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68B")

    ChrTalk(    #6
        0xFE,
        "Aidios... What's going on here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "It's like the Factory Chief said. None\x01",
            "of the machines are working at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "If only Professor Russell was here\x01",
            "for us at a time like this...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_728")

    label("loc_68B")


    ChrTalk(    #9
        0xFE,
        (
            "It's like the Factory Chief said. None\x01",
            "of the machines are working at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "*sigh* If only Professor Russell was\x01",
            "here for us at a time like this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_728")

    Jump("loc_FB9")

    label("loc_72B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_877")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_79A")

    ChrTalk(    #11
        0xFE,
        "Tech that can control septium veins...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "I can hardly imagine it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_874")

    label("loc_79A")


    ChrTalk(    #13
        0xFE,
        "Hey, everyone good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Seems like investigating the source\x01",
            "of the earthquakes was a hard job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Still, to control septium veins...\x01",
            "What crazy tech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "It's unimaginable with our level of knowledge.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_874")

    Jump("loc_C40")

    label("loc_877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_8EB")

    ChrTalk(    #17
        0xFE,
        (
            "The septium veins haven't settled down yet,\x01",
            "it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "But, just what's causing this phenomenon?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C40")

    label("loc_8EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_A87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9C7")

    ChrTalk(    #19
        0xFE,
        "The problem seems to be a delivery of the data.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "A-Anyway, I need to hurry and do a test...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "As expected of Professor Russell. He just comes\x01",
            "out of nowhere with a tough problem like this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A84")

    label("loc_9C7")


    ChrTalk(    #22
        0xFE,
        (
            "Receive data from external sources\x01",
            "and process it in real time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "It's not impossible, but it'll be pretty\x01",
            "tough to coordinate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "A-Anyway, I need to hurry and do a test...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_A84")

    Jump("loc_C40")

    label("loc_A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_BAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B23")

    ChrTalk(    #25
        0xFE,
        (
            "Professor Russell...\x01",
            "Just what does he plan to do this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I'm half fascinated, half horrified...\x01",
            "That's how I feel right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA7")

    label("loc_B23")


    ChrTalk(    #27
        0xFE,
        (
            "That reminds me, it seems like Professor\x01",
            "Russell is really busy right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "I'm starting to get a really bad feeling...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_BA7")

    Jump("loc_C40")

    label("loc_BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_C40")

    ChrTalk(    #29
        0xFE,
        (
            "There was an earthquake a bit ago, but\x01",
            "it didn't have any effect on the Capel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "If needed, you can use it any\x01",
            "time to look up things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C40")

    Jump("loc_D40")

    label("loc_C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_CAA")

    ChrTalk(    #31
        0xFE,
        "Capel's doing great, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "If needed, you can use it any\x01",
            "time to look up things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D40")

    label("loc_CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_D40")

    ChrTalk(    #33
        0xFE,
        (
            "There was an earthquake a bit ago,\x01",
            "but it didn't have any effect on the Capel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "If needed, you can use it\x01",
            "any time to look up things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D40")

    Jump("loc_FB9")

    label("loc_D43")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D9E")

    ChrTalk(    #35
        0xFE,
        "Hey, it's you guys. Maaan, it's been a while!\x02",
    )

    CloseMessageWindow()
    Jump("loc_DCC")

    label("loc_D9E")


    ChrTalk(    #36
        0xFE,
        "Hey, it's you. Maaan, it's been a while!\x02",
    )

    CloseMessageWindow()

    label("loc_DCC")


    ChrTalk(    #37
        0x101,
        (
            "#1001FAhaha, yeah, it has.\x02\x03",

            "#1000FHow's Capel doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Oh, thanks for asking. It's doing great.\x01",
            "There's no sign of any real damage\x01",
            "from the earthquake at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "If needed, you can use it\x01",
            "any time to look up things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "After all, we owe you a lot\x01",
            "when it comes to the Capel.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F1F")

    ChrTalk(    #41
        0x107,
        "#061FAh, that's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F4F")

    label("loc_F1F")


    ChrTalk(    #42
        0xFE,
        "I'd say you've more than earned the right.\x02",
    )

    CloseMessageWindow()

    label("loc_F4F")


    ChrTalk(    #43
        0x101,
        (
            "#1017FTh-Thanks.\x02\x03",

            "Well, if needed, we'll be sure to\x01",
            "make use of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "Sure thing. Any time.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x142F)
    OP_A2(0x0)

    label("loc_FB9")

    TalkEnd(0xA)
    Return()

    # Function_3_41B end

    def Function_4_FBD(): pass

    label("Function_4_FBD")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_10C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1045")

    ChrTalk(    #45
        0x8,
        (
            "#100FYou all should hurry to Elmo.\x02\x03",

            "I'll continue analysis here. If I find\x01",
            "anything out, I'll contact the inn.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10BD")

    label("loc_1045")


    ChrTalk(    #46
        0x8,
        (
            "#100FYou all should hurry to Elmo.\x02\x03",

            "I'll continue analysis here.\x02\x03",

            "If I find anything out, I'll contact the inn.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_10BD")

    Jump("loc_11CC")

    label("loc_10C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_11CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1150")

    ChrTalk(    #47
        0x8,
        (
            "#100FI'm going to get things ready\x01",
            "here to receive the data.\x02\x03",

            "I'm counting on you all to place\x01",
            "the measuring instruments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CC")

    label("loc_1150")


    ChrTalk(    #48
        0x8,
        (
            "#100FOhh, how's it going?\x01",
            "The placement going well?\x02\x03",

            "Capel's in a good mood today.\x01",
            "Our preparations are going fine.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_11CC")

    TalkEnd(0x8)
    Return()

    # Function_4_FBD end

    def Function_5_11D0(): pass

    label("Function_5_11D0")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1395")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133B")

    ChrTalk(    #49
        0xFE,
        (
            "Perhaps the professor's involved in\x01",
            "these weird events.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Like, one of his secret experiments failed,\x01",
            "and now orbal power throughout the\x01",
            "kingdom's gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "Haha... N-No way, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Even he of all people wouldn't do\x01",
            "an experiment that dangerous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "...Th-The fact that I can't say that\x01",
            "for sure makes it all the scarier.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1392")

    label("loc_133B")


    ChrTalk(    #54
        0xFE,
        (
            "Pr-Professor Russell couldn't possibly be\x01",
            "involved, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "Haha... N-No way.\x02",
    )

    CloseMessageWindow()

    label("loc_1392")

    Jump("loc_1CB9")

    label("loc_1395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1546")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_149D")

    ChrTalk(    #56
        0xFE,
        "This phenomenon that's going on...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "It's that thing that Professor Russell\x01",
            "caused a while back...isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "In other words, anything we do while this\x01",
            "is going on is basically pointless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "*sigh* Maybe I'll go home early today.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1543")

    label("loc_149D")


    ChrTalk(    #60
        0xFE,
        (
            "This phenomenon's that thing Professor\x01",
            "Russell caused a while back, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "In other words, anything we do while this\x01",
            "is going on is basically pointless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1543")

    Jump("loc_1CB9")

    label("loc_1546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_168D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_15F6")

    ChrTalk(    #62
        0xFE,
        "Seems like the earthquakes are over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "Aidios, all I ask is that the earth stays\x01",
            "right where it is and stops moving about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "For Capel's sake, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_168A")

    label("loc_15F6")


    ChrTalk(    #65
        0xFE,
        (
            "According to the Factory Chief's\x01",
            "announcement, it seems like the\x01",
            "earthquakes are over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Heh, guess those measurements\x01",
            "were useful, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_168A")

    Jump("loc_1CB9")

    label("loc_168D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_17BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1713")

    ChrTalk(    #67
        0xFE,
        (
            "Phew! Managed to get things tidied back\x01",
            "up somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "All right, now to leave the rest to\x01",
            "Supervisor Travis.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BA")

    label("loc_1713")


    ChrTalk(    #69
        0xFE,
        (
            "All right. Looks like the processing is\x01",
            "flowing smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "Still, the professor's incredible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "To construct a system like this in\x01",
            "such a short time...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_17BA")

    Jump("loc_1CB9")

    label("loc_17BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_18D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1886")

    ChrTalk(    #72
        0xFE,
        (
            "Geez, the professor can never just do things\x01",
            "like a normal person. He's always in and out\x01",
            "like whirlwind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "If he'd said something a bit earlier,\x01",
            "this would be a lot easier...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D6")

    label("loc_1886")


    ChrTalk(    #74
        0xFE,
        "Sorry, kinda busy right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "If you want to talk, how about later.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_18D6")

    Jump("loc_1CB9")

    label("loc_18D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1C14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1ADF")

    ChrTalk(    #76
        0xFE,
        (
            "The Capel, unlike other machines, needs\x01",
            "to rest sometimes, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "This is just my thought, but I think the\x01",
            "difference between it and other machines\x01",
            "relates to the presence of 'memory.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "While Capel's running, it's constantly\x01",
            "updating its own memory...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "So while it's operating, it doesn't really\x01",
            "have time to rebuild and store any of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "In which case, to arrange its memory,\x01",
            "it needs time spent offline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "That's the theory I'm trying to write\x01",
            "up as my thesis, anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C11")

    label("loc_1ADF")


    ChrTalk(    #82
        0xFE,
        "Capel's running smoothly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Lately we've been trying to avoid constant\x01",
            "operation and give it periodic breaks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "The Capel, unlike other machines, needs\x01",
            "to rest sometimes, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "Stopping it periodically helps it run smoothly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "It's interesting, huh?\x01",
            "Almost like a living thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1C11")

    Jump("loc_1CB9")

    label("loc_1C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1CB9")

    ChrTalk(    #87
        0xFE,
        (
            "This room's up on the fifth floor, so we got\x01",
            "shaken up quite a bit from that earthquake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Hopefully the Capel doesn't throw\x01",
            "another fit over this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB9")

    TalkEnd(0xC)
    Return()

    # Function_5_11D0 end

    def Function_6_1CBD(): pass

    label("Function_6_1CBD")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CD4")
    Call(0, 15)
    Call(0, 16)

    label("loc_1CD4")

    OP_4A(0x8, 255)
    OP_72(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_72(0x12, 0x4)
    OP_76(0x12, 0x0, 0x2, 0x4, 0x8, 0x64, 0x3, 0x3)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(2120, 0, 13780, 0)
    OP_67(0, 7040, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, -510, 0, 10500, 0)
    SetChrPos(0xA, 4420, 1000, 4220, 90)
    SetChrPos(0x9, 460, 0, 7640, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)

    def lambda_1DA1():
        OP_6D(1900, 0, 8220, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1DA1)

    def lambda_1DB9():
        OP_67(0, 7040, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DB9)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Fade(250)
    OP_76(0x12, 0x0, 0x2, 0x4, 0x8, 0x64, 0x4, 0x7)
    OP_0D()
    Sleep(500)
    OP_4A(0xA, 255)
    Sleep(500)
    OP_8C(0xA, 270, 400)

    ChrTalk(    #89
        0xA,
        (
            "Professor Russell, we're connected to the\x01",
            "first unit and are receiving telemetry now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "#100F#6PYes, I see.\x01",
            "Good, the connection is perfect.\x02\x03",

            "#104FHmm... And even better, it looks\x01",
            "like things are rock-solid.\x02\x03",

            "#102FSecure our connections to the\x01",
            "other two units at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        "Understood, Professor.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)
    OP_4B(0xA, 255)

    def lambda_1F58():
        OP_6D(710, 0, 3390, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1F58)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x7)
    Sleep(500)
    OP_43(0x107, 0x1, 0x0, 0x8)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0xA)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #92
        0x101,
        (
            "#1006F#5PI think they know we\x01",
            "succeeded already!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2040")

    ChrTalk(    #93
        0x106,
        (
            "#552F#2PI guess. Man...this room is\x01",
            "still the weirdest damn thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_209F")

    label("loc_2040")


    ChrTalk(    #94
        0x103,
        (
            "#023F#2PIt seems so... Goodness, but this entire\x01",
            "room never fails to take my breath away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_209F")

    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_20C1():
        OP_6D(710, 0, 5300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20C1)
    TurnDirection(0x9, 0x101, 400)
    WaitChrThread(0x101, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2174")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as Met Murdock Again\x01",              # 0
            "Set as Haven't Met Murdock Again\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_215F"),
        (1, "loc_2165"),
        (SWITCH_DEFAULT, "loc_216B"),
    )


    label("loc_215F")

    OP_A2(0x1481)
    Jump("loc_216B")

    label("loc_2165")

    OP_A3(0x1481)
    Jump("loc_216B")

    label("loc_216B")

    FadeToBright(300, 0)

    label("loc_2174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E2")

    ChrTalk(    #95
        0x9,
        "#802F#6PHmm? Oh, Estelle, hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1004F#2POh, Mr. Murdock!\x02",
    )

    CloseMessageWindow()

    def lambda_21C7():
        OP_6D(710, 0, 6300, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_21C7)

    def lambda_21DF():
        OP_8E(0xFE, 0xFFFFFEDE, 0x0, 0x10CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_21DF)
    Sleep(200)
    SetChrFlags(0x9, 0x4)

    def lambda_2204():
        OP_8E(0xFE, 0x1F4, 0x0, 0x19E6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2204)

    def lambda_221F():
        OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x10EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_221F)
    Sleep(100)

    def lambda_223F():
        OP_8E(0xFE, 0xFFFFFE84, 0x0, 0xB9A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_223F)
    Sleep(200)

    def lambda_225F():
        OP_8E(0xFE, 0xFFFFFA42, 0x0, 0xBCC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_225F)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0x9, 0x1)
    ClearChrFlags(0x9, 0x4)

    ChrTalk(    #97
        0x101,
        (
            "#1025F#2PUm, hi! It's been a while!\x01",
            "We last met at the birthday\x01",
            "celebrations, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "#803F#6PYes. It certainly has been a while...\x02\x03",

            "#800FFrom what I hear, you've been through\x01",
            "a lot. I'm glad to see you're well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1016F#2PHaha! Well, thanks, Mr. Murdock.\x02\x03",

            "#1011FAnyway, we've got the measuring devices\x01",
            "set up like the professor asked.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2534")

    label("loc_23E2")


    ChrTalk(    #100
        0x9,
        "#802F#6POh, hello, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1011F#2PHi, Mr. Murdock.\x02",
    )

    CloseMessageWindow()

    def lambda_2429():
        OP_6D(710, 0, 6300, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2429)

    def lambda_2441():
        OP_8E(0xFE, 0xFFFFFEDE, 0x0, 0x10CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2441)
    Sleep(200)
    SetChrFlags(0x9, 0x4)

    def lambda_2466():
        OP_8E(0xFE, 0x1F4, 0x0, 0x19E6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2466)

    def lambda_2481():
        OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x10EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2481)
    Sleep(100)

    def lambda_24A1():
        OP_8E(0xFE, 0xFFFFFE84, 0x0, 0xB9A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_24A1)
    Sleep(200)

    def lambda_24C1():
        OP_8E(0xFE, 0xFFFFFA42, 0x0, 0xBCC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_24C1)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0x9, 0x1)
    ClearChrFlags(0x9, 0x4)

    ChrTalk(    #102
        0x101,
        (
            "#1011F#2PWe've got the measuring devices\x01",
            "set up like the professor asked.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2534")


    ChrTalk(    #103
        0x9,
        (
            "#800F#6PYes, we saw.\x02\x03",

            "We've got data pouring in\x01",
            "from them already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x107,
        "#064F#5PSo the Capel is already running?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x107, 400)

    ChrTalk(    #105
        0x9,
        (
            "#801F#6PAye! Professor Russell's running some sort of\x01",
            "program to sort the data now. In fact...\x02",
        )
    )

    CloseMessageWindow()
    OP_76(0x12, 0x0, 0x2, 0x4, 0x8, 0x64, 0x8, 0xB)
    OP_4A(0xA, 255)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xA, 270, 400)

    ChrTalk(    #106
        0xA,
        (
            "#4PConnections to second and\x01",
            "third units...stable.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2691():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2691)
    Sleep(50)

    def lambda_26A4():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_26A4)
    Sleep(50)

    def lambda_26B7():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26B7)
    Sleep(50)

    def lambda_26CA():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_26CA)
    Sleep(50)

    def lambda_26DD():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_26DD)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #107
        0x8,
        (
            "#100FExcellent, that's all three, then.\x01",
            "Now let me see...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)
    OP_4B(0xA, 255)

    ChrTalk(    #108
        0x8,
        (
            "#101FGood, good! Both of them are\x01",
            "still as a pond.\x02\x03",

            "And we have links to all three\x01",
            "units. Excellent!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_27C0():
        OP_6D(710, 0, 7300, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_27C0)
    TurnDirection(0x8, 0x101, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #109
        0x8,
        (
            "#103FAhh, everyone! Wasn't expecting\x01",
            "you back this quickly.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2825():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2825)
    Sleep(50)

    def lambda_2838():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2838)
    Sleep(50)

    def lambda_284B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_284B)
    Sleep(50)

    def lambda_285E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_285E)
    Sleep(50)

    def lambda_2871():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2871)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #110
        0x8,
        (
            "#101FAs you can see, thanks to you we're\x01",
            "getting all the data we need.\x02\x03",

            "Good work, you four.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1016F#2PHaha! Well, really, all we did\x01",
            "was carry the instrument bits.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_29D0")

    ChrTalk(    #112
        0x106,
        (
            "#051F'Sides, we're the ones getting\x01",
            "a favor off of you.\x02\x03",

            "You should be thankin' shortstuff\x01",
            "over here. She's the one who put\x01",
            "'em together like a pro.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7D")

    label("loc_29D0")


    ChrTalk(    #113
        0x103,
        (
            "#027FBesides, Professor. You're the one\x01",
            "doing us a favor. You don't need to\x01",
            "thank us.\x02\x03",

            "If you want to thank anyone, thank\x01",
            "Tita. We couldn't have done this\x01",
            "without her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A7D")

    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_8C(0x107, 90, 400)

    ChrTalk(    #114
        0x107,
        (
            "#560F#5PWha...? No, no! I d-didn't do anything\x01",
            "special...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "#101FNo, no. You did very well.\x02\x03",

            "Even the transmitters are perfect.\x01",
            "The signal we're receiving is marvelous.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 400)

    ChrTalk(    #116
        0x107,
        (
            "#067F#2PHeehee! Well, yay!\x02\x03",

            "#560FSo we're all set up now, right,\x01",
            "Grandpa?\x02\x03",

            "Can I do anything else to help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "#104FNo, we're as prepared as we can be,\x01",
            "I think.\x02\x03",

            "#100FI've programmed the Capel to begin\x01",
            "analysis automatically if a disturbance\x01",
            "is detected in the septium veins.\x02\x03",

            "Now we just wait for an earthquake\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1007F#2PSo we've...pretty much hurried up to wait.\x01",
            "*sigh*\x02\x03",

            "#1015FI dunno if I can stay calm just waiting\x01",
            "for an earthquake to strike Zeiss again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DA4")

    ChrTalk(    #119
        0x104,
        (
            "#035F#2PHeh, indeed.\x02\x03",

            "#030FAn earthquake hitting the city directly\x01",
            "is a discomforting thought.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E0C")

    label("loc_2DA4")


    ChrTalk(    #120
        0x105,
        (
            "#043F#2PI know what you mean...\x02\x03",

            "What if another earthquake hits\x01",
            "the city directly? It's chilling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2E53")

    ChrTalk(    #121
        0x106,
        (
            "#050FDon't suppose we have a plan\x01",
            "in case that happens?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E85")

    label("loc_2E53")


    ChrTalk(    #122
        0x103,
        (
            "#020FDo we have a plan in case\x01",
            "that happens?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E85")

    OP_8C(0x9, 225, 400)

    ChrTalk(    #123
        0x9,
        (
            "#800F#6PWe've secured and locked down\x01",
            "the factory for an earthquake.\x02\x03",

            "#803FEven so, if the next earthquake is\x01",
            "much stronger, it will be hard on us.\x02\x03",

            "At the very least, I can't imagine\x01",
            "we'll avoid property damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x8,
        (
            "#100FUnfortunately, the Capel here is the same.\x02\x03",

            "Strong enough vibrations could damage it,\x01",
            "causing errors and making our experiment\x01",
            "fail...\x02\x03",

            "#101F...so a prayer or three to the Goddess\x01",
            "wouldn't go amiss, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        "#1007F#2PI thought I was nervous before...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30D9")

    ChrTalk(    #126
        0x104,
        (
            "#035F#2PEven with cutting-edge technology,\x01",
            "we still need the favor of the Goddess?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3136")

    label("loc_30D9")


    ChrTalk(    #127
        0x105,
        (
            "#045F#2PHaha. So, even the most advanced\x01",
            "technology still needs the blessing\x01",
            "of Aidios?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3136")

    OP_8C(0x107, 180, 400)

    ChrTalk(    #128
        0x107,
        (
            "#560F#5PHeehee! Engineers can be really\x01",
            "faithful, you know!\x02\x03",

            "I pray to the Goddess a lot when I'm\x01",
            "working really hard on something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x9,
        (
            "#806F#6PShe does have a point.\x02\x03",

            "I remember when Professor Russell was developing\x01",
            "the first orbal airship. I was going to\x01",
            "church three times a day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        (
            "#102FYou could've had a little faith in something\x01",
            "OTHER than the Goddess, Chief Murdock.\x01",
            "Hmph!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x9,
        (
            "#803F#6PAfter thirty-nine failed experiments,\x01",
            "could you blame me?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #132
        0x101,
        (
            "#1016F#2PHeehee. They've always been like this,\x01",
            "haven't they?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 400)

    ChrTalk(    #133
        0x107,
        "#067F#5PI think they have, yeah!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3402")

    ChrTalk(    #134
        0x106,
        (
            "#051FAnyway. Looks like we got some\x01",
            "time to kill.\x02\x03",

            "Wouldn't hurt to pop back over\x01",
            "to the guildhouse and report in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3490")

    label("loc_3402")


    ChrTalk(    #135
        0x103,
        (
            "#027FEither way, it seems we have quite\x01",
            "a bit of time on our hands.\x02\x03",

            "It wouldn't hurt to return to the\x01",
            "guildhouse briefly and report in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3490")


    ChrTalk(    #136
        0x8,
        (
            "#101FYes, go on ahead.\x02\x03",

            "We'll contact the guild\x01",
            "should anything hap--\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x9D, 0x0, 0x64)
    OP_76(0x12, 0x0, 0x2, 0x4, 0x8, 0x64, 0xC, 0xF)
    Sleep(1500)
    OP_20(0x7D0)
    OP_22(0x9E, 0x0, 0x64)
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_76(0x12, 0x0, 0x2, 0x4, 0x8, 0x64, 0x10, 0x17)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x9, 0, 600)
    OP_8C(0x8, 0, 600)
    OP_8C(0x101, 0, 600)
    OP_8C(0x107, 0, 600)

    ChrTalk(    #137
        0x101,
        "#1020F#2PWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x107,
        "#065F#5PEeek! Earthquake!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x8,
        (
            "#104FSeems we don't have that much\x01",
            "time to kill after all!\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0xA, 255)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xA, 270, 600)

    ChrTalk(    #140
        0xA,
        "#4PAll three instruments are reporting changes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xA,
        "#4PThe septium veins appear to be active!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x8,
        (
            "#102FContinue monitoring! Don't take\x01",
            "your eyes off them for a second!\x02\x03",

            "If the signals are interrupted,\x01",
            "report immediately!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xA,
        "#4PYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 600)
    OP_4B(0xA, 255)
    OP_8C(0x8, 225, 600)

    def lambda_3757():

        label("loc_3757")

        TurnDirection(0x9, 0x8, 400)
        OP_48()
        Jump("loc_3757")

    QueueWorkItem2(0x9, 1, lambda_3757)

    def lambda_3768():
        OP_6D(-590, 0, 6000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3768)
    OP_8E(0x8, 0xFFFFF95C, 0x0, 0x25B2, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFF95C, 0x0, 0x169E, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFFE20, 0x0, 0x169E, 0xBB8, 0x0)
    OP_8C(0x8, 0, 400)
    OP_44(0x9, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #144
        0x8,
        (
            "#102F#6PNow, let's see... Data still coming\x01",
            "in from all three instruments...\x02\x03",

            "Given the direction the seismic waves are\x01",
            "headed, the origin point of the temblor...\x02\x03",

            "#104FCoordinates are... 12.73, 378.02...\x01",
            "Oh-ho... Very interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        "#1026F#4PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x8,
        (
            "#102F#6PWe know where that earthquake's\x01",
            "epicenter is.\x02\x03",

            "It's...Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1020F#4P#3SWHAT?! DAD!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_396D")

    ChrTalk(    #148
        0x106,
        "#055FAw, hell!\x02",
    )

    CloseMessageWindow()
    Jump("loc_398D")

    label("loc_396D")


    ChrTalk(    #149
        0x103,
        "#024FWhat?! Are you sure?!\x02",
    )

    CloseMessageWindow()

    label("loc_398D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0xA, 255)
    OP_4B(0x8, 255)
    OP_4B(0xC, 255)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C3101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1CBD end

    def Function_7_39B1(): pass

    label("Function_7_39B1")

    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -1120, 0, -1250, 0)
    ClearChrFlags(0x101, 0x80)

    def lambda_39D8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_39D8)
    OP_8E(0x101, 0xFFFFFE98, 0x0, 0x92E, 0x7D0, 0x0)
    OP_8C(0x101, 0, 400)
    Return()

    # Function_7_39B1 end

    def Function_8_3A00(): pass

    label("Function_8_3A00")

    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x107, -1120, 0, -1250, 0)
    ClearChrFlags(0x107, 0x80)

    def lambda_3A27():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_3A27)
    OP_8E(0x107, 0xFFFFF9C0, 0x0, 0x852, 0x7D0, 0x0)
    OP_8C(0x107, 0, 400)
    Return()

    # Function_8_3A00 end

    def Function_9_3A4F(): pass

    label("Function_9_3A4F")

    OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xF7, -1120, 0, -1250, 0)
    ClearChrFlags(0xF7, 0x80)

    def lambda_3A76():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_3A76)
    OP_8E(0xF7, 0xFFFFFE02, 0x0, 0x38E, 0x7D0, 0x0)
    OP_8C(0xF7, 0, 400)
    Return()

    # Function_9_3A4F end

    def Function_10_3A9E(): pass

    label("Function_10_3A9E")

    OP_9F(0xF9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xF9, -1120, 0, -1250, 0)
    ClearChrFlags(0xF9, 0x80)

    def lambda_3AC5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_3AC5)
    OP_8E(0xF9, 0xFFFFF952, 0x0, 0x2E4, 0x7D0, 0x0)
    OP_8C(0xF9, 0, 400)
    Return()

    # Function_10_3A9E end

    def Function_11_3AED(): pass

    label("Function_11_3AED")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B04")
    Call(0, 15)
    Call(0, 16)

    label("loc_3B04")

    OP_22(0x9E, 0x0, 0x64)
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_72(0x12, 0x4)
    OP_76(0x12, 0x0, 0x2, 0x4, 0x8, 0x64, 0x10, 0x17)
    OP_4A(0x8, 255)
    OP_6D(-840, 0, 2850, 0)
    OP_67(0, 7040, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -290, 0, 4300, 0)
    SetChrPos(0x107, -1430, 0, 4330, 0)
    SetChrPos(0xF7, -380, 0, 2970, 0)
    SetChrPos(0xF9, -1470, 0, 3020, 0)
    SetChrPos(0x8, -480, 0, 5780, 0)
    SetChrPos(0xA, 4420, 1000, 4220, 90)
    SetChrPos(0x9, 500, 0, 6630, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_3C23():
        OP_6D(-800, 0, 5130, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3C23)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, -1080, 0, -1380, 0)
    ClearChrFlags(0xB, 0x80)

    def lambda_3C5C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3C5C)
    OP_8E(0xB, 0xFFFFFC4A, 0x0, 0x5AA, 0xBB8, 0x0)
    OP_0D()

    ChrTalk(    #150
        0xB,
        (
            "#2PChief! We've received word from\x01",
            "Leiston Fortress!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xB,
        "#2PThey've suffered a fairly large earthquake!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 400)

    ChrTalk(    #152
        0x9,
        "#805F#6PWe were right...\x02",
    )

    CloseMessageWindow()

    def lambda_3D16():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D16)
    Sleep(100)

    def lambda_3D29():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3D29)
    Sleep(50)

    def lambda_3D3C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3D3C)
    Sleep(50)

    def lambda_3D4F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3D4F)
    Sleep(50)

    def lambda_3D62():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D62)
    WaitChrThread(0x107, 0x1)

    ChrTalk(    #153
        0x101,
        "#1020F#6PWh-What happened?! Is anyone hurt?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xB,
        (
            "#2PThankfully, there don't seem to\x01",
            "be any injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xB,
        (
            "#2PI think they mentioned they\x01",
            "prepared in advance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        "#1007F#6PThank the Goddess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x8,
        (
            "#101F#6PHah! That's Cassius, all right.\x01",
            "The man has the danger sense\x01",
            "of a fox.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x9D, 0x46)
    OP_22(0x9D, 0x0, 0x64)
    OP_23(0x9E)
    OP_76(0x12, 0x0, 0x2, 0x4, 0x8, 0x64, 0x18, 0x1B)

    def lambda_3EB3():
        OP_6D(-800, 0, 6500, 800)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3EB3)
    OP_8C(0x8, 0, 500)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #158
        0x8,
        (
            "#102F#6PNow then. The Capel should\x01",
            "have the results for us.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F18():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3F18)
    Sleep(50)

    def lambda_3F2B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F2B)
    Sleep(100)

    def lambda_3F3E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3F3E)
    Sleep(50)

    def lambda_3F51():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3F51)
    WaitChrThread(0xF9, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #159
        "\x07\x05Professor Russell checked the displayed analysis results.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #160
        0x8,
        (
            "#102F#6PSo, let's see.\x02\x03",

            "#103F...Ohhhh. This is interesting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        (
            "#1002F#2PWhat is it, Professor?\x01",
            "Did we learn something?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #162
        0x8,
        (
            "#100F#6PI do believe we have.\x02\x03",

            "According to this, the flows along the\x01",
            "septium veins were altered significantly\x01",
            "prior to the earthquake.\x02\x03",

            "The unusual flows gathered beneath\x01",
            "a single location, apparently.\x02\x03",

            "Since it occurred quite close to the\x01",
            "surface, it had little effect beyond\x01",
            "the immediate area.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_41AD")

    ChrTalk(    #163
        0x106,
        "#057FSo that'd mean... Aw, hell.\x02",
    )

    CloseMessageWindow()
    Jump("loc_41CE")

    label("loc_41AD")


    ChrTalk(    #164
        0x103,
        "#022FThat would mean... Oh.\x02",
    )

    CloseMessageWindow()

    label("loc_41CE")


    ChrTalk(    #165
        0x101,
        (
            "#1020F#4PH-Hang on a second.\x02\x03",

            "You're saying someone's controlling\x01",
            "SEPTIUM VEINS in order to generate\x01",
            "earthquakes on purpose?!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42A7")

    ChrTalk(    #166
        0x104,
        (
            "#032F#2PLiterally an 'earthquake weapon,' then.\x01",
            "Sweet Goddess...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42EF")

    label("loc_42A7")


    ChrTalk(    #167
        0x105,
        (
            "#042F#2PSo it's literally an earthquake weapon?\x01",
            "That's horrific...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42EF")


    ChrTalk(    #168
        0x8,
        (
            "#102F#6PYou have the right of it.\x01",
            "A weapon that can cause earthquakes\x01",
            "anywhere with septium veins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x107,
        (
            "#065F#2PB-B-But, Grandpa!\x02\x03",

            "Controlling septium veins?\x01",
            "Is that even possible?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x9,
        (
            "#805F#6PIt's well beyond the capabilities of any\x01",
            "earth-moving technology I'm aware of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        (
            "#104F#6PI agree.\x02\x03",

            "#102FHowever, we cannot deny the\x01",
            "evidence in front of us. Someone\x01",
            "has made it possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        (
            "#1022F#4PWell, tough for them!\x02\x03",

            "#1005FProfessor, can you use the data to\x01",
            "figure out where the weapon is?!\x02\x03",

            "If you can, we'll go stop it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x107,
        "#560F#2PYeah!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4539")

    ChrTalk(    #174
        0x106,
        "#051FDamn straight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4556")

    label("loc_4539")


    ChrTalk(    #175
        0x103,
        "#021FThat's the spirit!\x02",
    )

    CloseMessageWindow()

    label("loc_4556")


    ChrTalk(    #176
        0x8,
        "#103F#6PHmm. Perhaps I can!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 600)
    OP_8C(0x9, 225, 400)

    ChrTalk(    #177
        0x8,
        (
            "#102F#6PRight, pull back to the data at\x01",
            "the start of the disturbance...\x02\x03",

            "Now, in what direction does\x01",
            "the flow disturbance begin...\x02\x03",

            "...I have it. 165.88 by -228.35...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #178
        0x107,
        "#065F#2PHuh...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #179
        0x101,
        "#1002F#2PTita, do you know where that is?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 400)

    ChrTalk(    #180
        0x107,
        "#065F#5PI think so...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #181
        "\x07\x05Tita pulled out the map.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS134._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS207._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS208._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS209._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #182
        (
            "\x07\x00#062FThe coordinates are selge from\x01",
            "Zeiss' center, so...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #183
        "\x07\x00#062FIf east 12 selge, north 378 is Leiston Fortress...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #184
        "\x07\x00#062FEast 165 selge, south -228 selge would be...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #185
        (
            "\x18\x07\x05What location is 165 selge east\x01",
            "and 228 selge south from Zeiss?\x02",
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "Kaldia Tunnel\x01",       # 0
            "Carnelia Tower\x01",      # 1
            "Elmo Village\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_49C5"),
        (1, "loc_4A0C"),
        (2, "loc_4A53"),
        (SWITCH_DEFAULT, "loc_4A99"),
    )


    label("loc_49C5")

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #186
        (
            "\x07\x00#063FUm, no...\x02\x03",

            "I think it'd be about here...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4A99")

    label("loc_4A0C")

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #187
        (
            "\x07\x00#063FUm, no...\x02\x03",

            "I think it'd be about here...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4A99")

    label("loc_4A53")

    OP_2B(0x88, 0x2)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #188
        (
            "\x07\x00#063FYeah.\x02\x03",

            "I think it'd be about here.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4A99")

    label("loc_4A99")

    OP_AE(0x1F4)
    Sleep(500)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(300, 50, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #189
        "\x07\x00#1020FWhat?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4B33")
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #190
        "\x07\x00#555FHell of a place to hide.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4B81")

    label("loc_4B33")

    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #191
        (
            "\x07\x00#025FWell, it's hiding in plain sight,\x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_4B81")

    TurnDirection(0x8, 0x101, 0)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_C6(0x3, 0x6, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C86")

    ChrTalk(    #192
        0x104,
        (
            "#035F#2PElmo Village.\x02\x03",

            "#030FThe tunnels which house the source\x01",
            "of their springs hide our culprit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CF2")

    label("loc_4C86")


    ChrTalk(    #193
        0x105,
        (
            "#047F#2PElmo Village?\x02\x03",

            "#042FSo the origin of the disturbances is\x01",
            "somewhere near the hot springs, then?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CF2")


    ChrTalk(    #194
        0x8,
        (
            "#102F#6PI can't say for certain, but it\x01",
            "seems likely.\x02\x03",

            "So, what do you plan to do?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x107, 0, 400)

    ChrTalk(    #195
        0x101,
        (
            "#1005F#4PIsn't it obvious?! We're gonna\x01",
            "go check it out right now!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4DD5")

    ChrTalk(    #196
        0x106,
        (
            "#057FYeah, we need to move,\x01",
            "and fast.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_4DD5")


    ChrTalk(    #197
        0x103,
        "#022FYes, we need to hurry.\x02",
    )

    CloseMessageWindow()

    label("loc_4DF6")


    ChrTalk(    #198
        0x8,
        (
            "#104F#6PIndeed. So...\x02\x03",

            "#102FTita, go with them.\x02\x03",

            "They will need your knowledge and\x01",
            "technical skill in their investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 400)

    ChrTalk(    #199
        0x107,
        "#560F#2POh! Umm...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 400)

    ChrTalk(    #200
        0x107,
        (
            "#062F#5POkay! I'll do everything I can to help,\x01",
            "I promise!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #201
        0x101,
        (
            "#1007F#2PWell, uh. This might be kind\x01",
            "of dangerous.\x02\x03",

            "#1006FOn the other hand, Tita WILL\x01",
            "be a big help, so I sure can't\x01",
            "say no!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4FC7")

    ChrTalk(    #202
        0x106,
        (
            "#053FFor the love of... Fine, whatever.\x02\x03",

            "#050FYou just be careful, okay, squirt?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF8")

    label("loc_4FC7")


    ChrTalk(    #203
        0x103,
        (
            "#026FI agree.\x02\x03",

            "#020FTita, be careful, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FF8")

    OP_8C(0x107, 180, 400)

    ChrTalk(    #204
        0x107,
        "#062F#5PI will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x9,
        (
            "#800F#6PI'll contact Elmo ahead of you.\x02\x03",

            "I'm sure Mrs. Mao will be glad\x01",
            "to help your investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x107, 0, 400)

    ChrTalk(    #206
        0x101,
        "#1006F#4PThanks, Mr. Murdock.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x9,
        (
            "#800F#6PHazel, get Mrs. Mao at the Elmo\x01",
            "inn on the line at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xB,
        "Yes, sir!\x02",
    )

    CloseMessageWindow()

    def lambda_5109():
        OP_6D(-840, 0, 2850, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_5109)

    def lambda_5121():

        label("loc_5121")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5121")

    QueueWorkItem2(0x101, 2, lambda_5121)

    def lambda_5132():

        label("loc_5132")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5132")

    QueueWorkItem2(0x107, 2, lambda_5132)

    def lambda_5143():

        label("loc_5143")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5143")

    QueueWorkItem2(0xF7, 2, lambda_5143)

    def lambda_5154():

        label("loc_5154")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5154")

    QueueWorkItem2(0xF9, 2, lambda_5154)
    OP_43(0x9, 0x1, 0x0, 0xC)
    Sleep(200)
    OP_43(0xB, 0x1, 0x0, 0xD)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x9, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x107, 0x2)
    OP_44(0xF7, 0x2)
    OP_44(0xF9, 0x2)

    def lambda_5192():
        OP_6D(-840, 0, 5130, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_5192)

    def lambda_51AA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_51AA)
    Sleep(50)

    def lambda_51BD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51BD)
    Sleep(50)

    def lambda_51D0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_51D0)
    Sleep(50)

    def lambda_51E3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_51E3)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #209
        0x8,
        (
            "#102F#6PI'll remain here and continue to\x01",
            "analyze the data we're getting\x01",
            "using the Capel.\x02\x03",

            "If I discover anything, I'll contact\x01",
            "Elmo at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        (
            "#1002F#4PThanks, Professor.\x02\x03",

            "If we find anything, we'll call\x01",
            "you right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x8,
        "#102F#6PExcellent. Good luck, everyone.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5338")

    ChrTalk(    #212
        0x106,
        "#054FAll right! Let's get to Elmo!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5363")

    label("loc_5338")


    ChrTalk(    #213
        0x103,
        "#024FLet's get to Elmo at once, then!\x02",
    )

    CloseMessageWindow()

    label("loc_5363")

    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-1230, 0, 3450, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -1230, 0, 3450, 17)
    SetChrPos(0x1, -1230, 0, 3450, 17)
    SetChrPos(0x2, -1230, 0, 3450, 17)
    SetChrPos(0x3, -1230, 0, 3450, 17)
    SetChrPos(0x8, -480, 0, 10270, 0)
    OP_0D()
    OP_8C(0x8, 0, 0)
    OP_4B(0x8, 255)
    OP_4B(0xA, 255)
    OP_4B(0xC, 255)
    OP_72(0x2, 0x4)
    OP_71(0x12, 0x4)
    OP_A2(0x1420)
    OP_28(0x88, 0x4, 0x2)
    OP_28(0x88, 0x4, 0x8)
    OP_28(0x88, 0x1, 0x1)
    OP_28(0x85, 0x4, 0x10)
    OP_28(0x86, 0x4, 0x10)
    OP_28(0x87, 0x4, 0x10)
    OP_28(0x70, 0x4, 0x40)
    Sleep(500)
    OP_1D(0xD)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x2000000)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_11_3AED end

    def Function_12_546B(): pass

    label("Function_12_546B")

    OP_8E(0x9, 0x3B6, 0x0, 0x17CA, 0x9C4, 0x0)
    OP_8E(0x9, 0x258, 0x0, 0xA5A, 0x9C4, 0x0)
    OP_8E(0x9, 0xFFFFFBBE, 0x0, 0x2E4, 0x9C4, 0x0)
    OP_8E(0x9, 0xFFFFFB32, 0x0, 0xFFFFFE8E, 0x9C4, 0x0)
    OP_20(0xBB8)

    def lambda_54C6():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_54C6)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0x9, 0xFFFFFB50, 0x0, 0xFFFFF8DA, 0x9C4, 0x0)
    SetChrFlags(0x9, 0x80)
    Return()

    # Function_12_546B end

    def Function_13_54F1(): pass

    label("Function_13_54F1")

    OP_8C(0xFE, 180, 500)
    OP_8E(0xFE, 0xFFFFFB32, 0x0, 0xFFFFFE8E, 0x9C4, 0x0)

    def lambda_5512():
        OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5512)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFB50, 0x0, 0xFFFFF8DA, 0x9C4, 0x0)
    SetChrFlags(0xB, 0x80)
    Return()

    # Function_13_54F1 end

    def Function_14_553D(): pass

    label("Function_14_553D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-200, 0, 7100, 1000)
    FadeToDark(300, 0, 100)
    OP_22(0x9D, 0x0, 0x64)
    SetChrName("CAPEL")
    SetMessageWindowPos(250, 78, 36, 12)

    AnonymousTalk(    #214
        (
            "\x07\x02#1SThe Orbal Calculator\x01",
            "CAPEL SYSTEM Ver.7.0\x01",
            "Copyright(C) Z.C.F. 1197-1202\x01",
            "MODE:Information Retrieval\x01",
            "#200W　#20W\x01",
            "MEMORY_CHECK#100W........#20WOK!\x01",
            "#200W　#20W\x01",
            "#1SDatabase accessed.\x01",
            "Please input search term.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5652")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_753D")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        6,
        28,
        1,
        "[Central Factory]\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_569D"),
        (SWITCH_DEFAULT, "loc_752D"),
    )


    label("loc_569D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_751D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        6,
        116,
        1,
        (
            "[Establishment]\x01",       # 0
            "[Universal Tech]\x01",      # 1
            "[Related Topics]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5707"),
        (1, "loc_5FEF"),
        (2, "loc_711E"),
        (SWITCH_DEFAULT, "loc_750D"),
    )


    label("loc_5707")


    AnonymousTalk(    #215
        (
            "\x07\x02#1S[S1154] (S: Septian Calendar) - Death of Prof.\x01",
            "C. Epstein in the sovereign state of Leman.\x01",
            "[S1155] Professor A. Russell returns to the Liberl\x01",
            "Kingdom. He proposes the spread of orbment\x01",
            "technology, to a chilly reception.\x01",
            "[S1157] Prof. Russell forms a partnership with\x01",
            "the Zeiss Clockmaker's Union. Together, they\x01",
            "establish the Zeiss Engineering Factory (later\x01",
            "renamed the Central Factory).\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #216
        (
            "\x07\x02#1S[S1160] Edgar III, after an inspection of the\x01",
            "factory, donates a large amount of money to\x01",
            "further its research. Prof. Russell becomes the\x01",
            "first Factory Chief.\x01",
            "[S1162] Edgar III dies, and Alicia II assumes the\x01",
            "throne.\x01",
            "[S1164] Construction is completed on the\x01",
            "Langland Bridge.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #217
        (
            "\x07\x02#1S[S1168] The first orbal-powered airship, the\x01",
            "Calatrava, is completed. (39 failed test flights\x01",
            "before success was achieved.)\x01",
            "[S1173] The Zeiss Engineering Factory is renamed\x01",
            "Zeiss Central Factory and begins sharing\x01",
            "technology with the Verne Company and Reinford\x01",
            "Company.\x01",
            "[S1175] The Liberl Orbalship Corporation is\x01",
            "established, and the transit commuter airship,\x01",
            "the Linde, is commissioned.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #218
        (
            "\x07\x02#1S[S1177] Transit commuter airship, the Cecilia,\x01",
            "is commissioned.\x01",
            "[S1178] Factory airship, the Leibnitz, is\x01",
            "completed.\x01",
            "[S1180] The Zeiss Central Factory is dismantled\x01",
            "and reconstructed at its current site. The\x01",
            "partially-underground factory in the Kaldia\x01",
            "Hills is completed.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #219
        (
            "\x07\x02#1S[S1182] Professor Russell resigns from his\x01",
            "position as Factory Chief and is succeeded by\x01",
            "Murdock.\x01",
            "[S1185] Natural Science and Medical Research\x01",
            "divisions are founded.\x01",
            "[S1187] The passenger ship, Eterna, sinks in\x01",
            "Calvard waters. Crown prince Judis dies.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #220
        (
            "\x07\x02#1S[S1190] The Orbal Network, a joint venture with\x01",
            "the Epstein Foundation, is publicly announced.\x01",
            "[S1192] Outbreak of the Hundred Days War. The\x01",
            "Central Factory is taken by the Erebonian Army.\x01",
            "Prof. Russell develops patrol airships at Leiston\x01",
            "Fortress, which are used to mount a highly\x01",
            "effective counteroffensive, and soon become\x01",
            "central to the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #221
        (
            "\x07\x02#1S[S1193] Liberl and Erebonia sign a peace accord.\x01",
            "Orbment exports to the Erebonian Empire resume.\x01",
            "[S1197] Version 1.0 of the Capel orbal computer\x01",
            "is completed.\x01",
            "[S1199] Development commences on the high-speed\x01",
            "cruiser, the Arseille.\x01",
            "[S1202] The Arseille is completed and flight\x01",
            "tests commence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_751A")

    label("loc_5FEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_710E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60B2")

    Menu(
        2,
        6,
        116,
        1,
        (
            "[Orbments]\x01",                # 0
            "[Crystal Circuits]\x01",        # 1
            "[Septium]\x01",                 # 2
            "[Airships]\x01",                # 3
            "[Orbal Weaponry]\x01",          # 4
            "[Tactical Orbments]\x01",       # 5
            "[New Model Orbments]\x01",      # 6
            "[Bracer Guild Sign]\x01",       # 7
        )
    )

    Jump("loc_6128")

    label("loc_60B2")


    Menu(
        2,
        6,
        116,
        1,
        (
            "[Orbments]\x01",                # 0
            "[Crystal Circuits]\x01",        # 1
            "[Septium]\x01",                 # 2
            "[Airships]\x01",                # 3
            "[Orbal Weaponry]\x01",          # 4
            "[Tactical Orbments]\x01",       # 5
            "[New Model Orbments]\x01",      # 6
        )
    )


    label("loc_6128")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6154"),
        (1, "loc_6331"),
        (2, "loc_643B"),
        (3, "loc_65C5"),
        (4, "loc_67C3"),
        (5, "loc_6A37"),
        (6, "loc_6CC6"),
        (7, "loc_6ECD"),
        (SWITCH_DEFAULT, "loc_70FE"),
    )


    label("loc_6154")


    AnonymousTalk(    #222
        (
            "\x07\x02#1SEntry: Orbment\x01",
            "General term for devices that draw orbal energy\x01",
            "from septium, invented 50 years ago by Prof. C.\x01",
            "Epstein. The clockwork mechanism inside causes a\x01",
            "reaction between quartz, which in turn produces\x01",
            "a variety of different phenomena. Their greatest\x01",
            "advantages over combustion engines is that the\x01",
            "orbal energy within them is gradually restored\x01",
            "over time and the variety of different phenomena\x01",
            "they can produce. They are also much more\x01",
            "economically efficient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_710B")

    label("loc_6331")


    AnonymousTalk(    #223
        (
            "\x07\x02#1SEntry: Crystal Circuit (Quartz)\x01",
            "An electrical circuit with a crystalline structure\x01",
            "made from processed septium fragments (sepith).\x01",
            "They serve as an energy source but also cause\x01",
            "varied phenomena, which are only seen when they\x01",
            "are placed inside an orbment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_710B")

    label("loc_643B")


    AnonymousTalk(    #224
        (
            "\x07\x02#1SEntry: Septium\x01",
            "A grouping of seven gemstones found throughout\x01",
            "the continent. Prized as jewels for eons, it was\x01",
            "also regarded as a symbol of mystery. The invention\x01",
            "of technology to refine and process septium\x01",
            "fragments too small to use as jewels, called\x01",
            "sepith, and make them into quartz, resulted in a\x01",
            "massive increase in the importance of septium as\x01",
            "a resource across the continent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_710B")

    label("loc_65C5")


    AnonymousTalk(    #225
        (
            "\x07\x02#1SEntry: Orbal Airships/'Orbalships'\x01",
            "Commonly regarded as the crowning achievement\x01",
            "of orbment technology. Enables the power of\x01",
            "flight by combining a flight engine to control\x01",
            "gravity and an orbal engine to provide vast\x01",
            "amounts of energy. Because of the need for\x01",
            "high-efficiency orbal energy transfer and the\x01",
            "complexity of controlling the airship, many\x01",
            "modern orbalships are equipped with highly capable\x01",
            "orbal arithmetic logic units. Orbalships less than\x01",
            "20 arge in length are simply called 'airships.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_710B")

    label("loc_67C3")


    AnonymousTalk(    #226
        (
            "\x07\x02#1SEntry: Orbal Weaponry\x01",
            "Any firearm or cannon powered with orbment tech-\x01",
            "nology. Currently the most common form of military\x01",
            "weaponry among many nations. With orbal firearms,\x01",
            "energy is focused in a helical path along the\x01",
            "barrel, down to a tiny point, which then forces a\x01",
            "large metal projectile outward at high velocity.\x01",
            "These guns can fire more rounds than traditional\x01",
            "gunpowder arms, and at adjustable levels of force.\x01",
            "Orbal Cannons, meanwhile, fire shells containing\x01",
            "energy which explode on impact. Similar to orbal\x01",
            "guns, these have less recoil than gunpowder-using\x01",
            "cannons, and their power can be similarly adjusted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_710B")

    label("loc_6A37")


    AnonymousTalk(    #227
        (
            "\x07\x02#1SEntry: Tactical Orbments\x01",
            "Orbments used to manipulate orbal magics.\x01",
            "Usually no larger than a pocket watch, so its\x01",
            "internal workings are extremely minute and\x01",
            "elegantly constructed. When quartz designed\x01",
            "for tactical orbment use is installed, it improves\x01",
            "the abilities of its bearer.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #228
        (
            "\x07\x02#1SWhen this quartz synchronizes with the bearer\x01",
            "(a.k.a. the 'Resonance Phenomenon'), the\x01",
            "internal mechanisms take over the otherwise\x01",
            "complex process that would be required to use\x01",
            "magic, allowing just about anyone to use it in\x01",
            "the form of orbal arts. Furthermore, the arts\x01",
            "the user is able to use can be changed depending\x01",
            "on the combination of quartz inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_710B")

    label("loc_6CC6")


    AnonymousTalk(    #229
        (
            "\x07\x02#1SEntry: New Model Orbments\x01",
            "A new class of tactical orbments massively\x01",
            "upgraded from the preceding models developed by\x01",
            "the Epstein Foundation. In comparison to the old\x01",
            "model's six quartz slots, the new model has seven\x01",
            "slots.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #230
        (
            "\x07\x02#1SThis new model allows for more flexible quartz\x01",
            "arrangements, new combinations of usable orbal\x01",
            "magic, and even drastic increases in power.\x01",
            "However, as the architecture is drastically\x01",
            "different from the predecessor model, there is\x01",
            "no interchangeability in quartz between models.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_710B")

    label("loc_6ECD")

    OP_A2(0x4)
    OP_28(0x6C, 0x1, 0x8)

    AnonymousTalk(    #231
        (
            "\x07\x02#1SEntry: Bracer Guild Sign\x01",
            "A metal sign removed from the Zeiss branch of the\x01",
            "incompetent Bracer Guild by the genius and dashing\x01",
            "Phantom Thief Bleublanc. While its financial value\x01",
            "is insignificant, the shock to guild members is\x01",
            "likely considerable, and reading this now must\x01",
            "fill you with shame. Ah, I have probably said\x01",
            "enough. I need to provide the next key.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #232
        (
            "\x07\x02#1S---The third key is in the city. Gaze up at\x01",
            "the [Three Hatted Brothers].---\x01",
            "Note: this entry will self-delete. You are\x01",
            "recommended to commit this entry to a memo\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_710B")

    label("loc_70FE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_710B")

    label("loc_710B")

    Jump("loc_5FEF")

    label("loc_710E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_751A")

    label("loc_711E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74FD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        6,
        264,
        1,
        (
            "[Combustion Engine]\x01",      # 0
            "[Gasoline]\x01",               # 1
            "[Haulage Vehicle]\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7187"),
        (1, "loc_7294"),
        (2, "loc_73D6"),
        (SWITCH_DEFAULT, "loc_74ED"),
    )


    label("loc_7187")


    AnonymousTalk(    #233
        (
            "\x07\x02#1SEntry: Combustion Engine\x01",
            "A machine which generates usable energy by\x01",
            "burning fuel within. Less efficient than its\x01",
            "orbal counterpart, due to issues with gaseous\x01",
            "exhaust and noise pollution.\x01\x01",
            "[Combustion Engine] \x01",
            "Number Owned: 1\x01",
            "Owner: Maintenance Chief Gustav\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74FA")

    label("loc_7294")


    AnonymousTalk(    #234
        (
            "\x07\x02#1SEntry: Gasoline\x01",
            "A liquid derived from the purification of the\x01",
            "naturally-occurring hydrocarbon compound known as\x01",
            "petroleum. Used primarily as fuel for combustion\x01",
            "engines and as an industrial solvent.\x01",
            "[Republic-Manufactured Gasoline]\x01",
            "Emergency Stores: 20 mid-sized tanks\x01",
            "Repository: Orbment Manufacturing Factory\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74FA")

    label("loc_73D6")

    OP_28(0x29, 0x1, 0x8000)

    AnonymousTalk(    #235
        (
            "\x07\x02#1SEntry: Orbal Haulage Vehicle\x01",
            "Any wheeled vehicle powered by orbal energy.\x01",
            "Widely considered uncomfortable to ride and\x01",
            "very limited in speed. Primarily used for\x01",
            "transporting cargo.\x01",
            "[Orbment-Powered Vehicle]\x01",
            "Owner: No Data\x01",
            "Repository: Underground Factory Entrance\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74FA")

    label("loc_74ED")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_74FA")

    label("loc_74FA")

    Jump("loc_711E")

    label("loc_74FD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_751A")

    label("loc_750D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_751A")

    label("loc_751A")

    Jump("loc_569D")

    label("loc_751D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    Jump("loc_753A")

    label("loc_752D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_753A")

    label("loc_753A")

    Jump("loc_5652")

    label("loc_753D")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_756B")
    Call(1, 0)
    OP_A3(0x4)

    label("loc_756B")

    EventEnd(0x1)
    Return()

    # Function_14_553D end

    def Function_15_756E(): pass

    label("Function_15_756E")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_75E7"),
        (1, "loc_75ED"),
        (SWITCH_DEFAULT, "loc_75F3"),
    )


    label("loc_75E7")

    OP_A2(0x1200)
    Jump("loc_75F3")

    label("loc_75ED")

    OP_A2(0x1201)
    Jump("loc_75F3")

    label("loc_75F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_7601")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_7605")

    label("loc_7601")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_7605")

    Return()

    # Function_15_756E end

    def Function_16_7606(): pass

    label("Function_16_7606")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_7640")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_765A")

    label("loc_7640")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_765A")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_16_7606 end

    def Function_17_766C(): pass

    label("Function_17_766C")

    SetPlaceName(0x9A)
    Return()

    # Function_17_766C end

    SaveToFile()

Try(main)
