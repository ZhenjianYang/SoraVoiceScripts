from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1120   ._SN',
        MapName             = 'Bose',
        Location            = 'T1120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        'Marco',                                # 9
        'Nigel',                                # 10
        'Carrie',                               # 11
        'Sein',                                 # 12
        'Nial',                                 # 13
        'Dorothy',                              # 14
        'Cornelius',                            # 15
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH01120 ._CH',             # 01
        'ED6_DT07/CH01550 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH02060 ._CH',             # 04
        'ED6_DT06/CH20063 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01120P._CP',             # 01
        'ED6_DT07/CH01550P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH02060P._CP',             # 04
        'ED6_DT06/CH20063P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
    )

    DeclNpc(
        X                   = -25890,
        Z                   = 0,
        Y                   = 1370,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -24500,
        Z                   = 0,
        Y                   = 4690,
        Direction           = 180,
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
        X                   = -28800,
        Z                   = 0,
        Y                   = 24200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = 7400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -24500,
        Z                   = 0,
        Y                   = 4690,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )


    DeclActor(
        TriggerX            = -24000,
        TriggerZ            = 0,
        TriggerY            = 3580,
        TriggerRange        = 700,
        ActorX              = -24500,
        ActorZ              = 1500,
        ActorY              = 4690,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 920,
        TriggerZ            = 0,
        TriggerY            = 6280,
        TriggerRange        = 700,
        ActorX              = 500,
        ActorZ              = 1500,
        ActorY              = 7400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_2B9",          # 01, 1
        "Function_2_2CC",          # 02, 2
        "Function_3_2E2",          # 03, 3
        "Function_4_3FB",          # 04, 4
        "Function_5_C7C",          # 05, 5
        "Function_6_1339",         # 06, 6
        "Function_7_13B6",         # 07, 7
        "Function_8_1D6C",         # 08, 8
        "Function_9_1FF9",         # 09, 9
        "Function_10_20A6",        # 0A, 10
        "Function_11_212D",        # 0B, 11
        "Function_12_240D",        # 0C, 12
        "Function_13_2453",        # 0D, 13
        "Function_14_249E",        # 0E, 14
        "Function_15_24DF",        # 0F, 15
        "Function_16_251B",        # 10, 16
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_228")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_292")

    label("loc_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_248")
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, -27920, 0, 87590, 270)
    Jump("loc_292")

    label("loc_248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_26D")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, -27920, 0, 87590, 270)
    Jump("loc_292")

    label("loc_26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_277")
    Jump("loc_292")

    label("loc_277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_281")
    Jump("loc_292")

    label("loc_281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_28B")
    Jump("loc_292")

    label("loc_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_292")

    label("loc_292")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_2A2"),
        (106, "loc_2A2"),
        (SWITCH_DEFAULT, "loc_2B8"),
    )


    label("loc_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B5")
    OP_A2(0x338)
    Event(0, 16)

    label("loc_2B5")

    Jump("loc_2B8")

    label("loc_2B8")

    Return()

    # Function_0_20A end

    def Function_1_2B9(): pass

    label("Function_1_2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CB")
    OP_10(0x7, 0x1)
    OP_10(0x3, 0x0)

    label("loc_2CB")

    Return()

    # Function_1_2B9 end

    def Function_2_2CC(): pass

    label("Function_2_2CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2CC")

    label("loc_2E1")

    Return()

    # Function_2_2CC end

    def Function_3_2E2(): pass

    label("Function_3_2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_373")
    TalkBegin(0xE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                 # 0
            "Modify/Exchange\x01",      # 1
            "Leave\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_354")
    OP_0D()
    OP_A9(0xA)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_354")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_365")
    TalkEnd(0xE)
    Return()

    label("loc_365")

    Call(0, 11)
    OP_8C(0xE, 180, 0)
    Jump("loc_3FA")

    label("loc_373")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                 # 0
            "Modify/Exchange\x01",      # 1
            "Leave\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DE")
    OP_0D()
    OP_A9(0xA)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_3DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EF")
    TalkEnd(0x9)
    Return()

    label("loc_3EF")

    Call(0, 4)
    OP_8C(0x9, 180, 0)

    label("loc_3FA")

    Return()

    # Function_3_2E2 end

    def Function_4_3FB(): pass

    label("Function_4_3FB")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_605")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_544")
    OP_A2(0x1)

    ChrTalk(    #0
        0x9,
        (
            "M-My account ledgers were\x01",
            "confiscated by the army...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        "This is bad... Really bad...\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x9,
        (
            "N-Now hold on... Maybe I'm not in\x01",
            "as much trouble as I previously\x01",
            "thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "Thankfully those sky bandits took\x01",
            "off with the one that could have\x01",
            "gotten me in the most trouble...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_602")

    label("loc_544")


    ChrTalk(    #4
        0x9,
        (
            "The army may have taken off\x01",
            "with my account ledgers, but\x01",
            "I may just be all right!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "That's because the sky bandits\x01",
            "took off with the one that could've\x01",
            "gotten me in the most trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_602")

    Jump("loc_C78")

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_7FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_782")
    OP_A2(0x1)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #6
        0x9,
        "M-My factory!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "M-My factory and all my goods!\x01",
            "They're gone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        (
            "I-I've got to report this to either the\x01",
            "army or the Bracer Guild a.s.a.p...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        "N-Now hold on just a minute...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        (
            "If either one of these groups\x01",
            "saw what was written in that\x01",
            "stolen ledger...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x9,
        (
            "Yikes...\x01",
            "I'd be in a world of hurt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FC")

    label("loc_782")


    ChrTalk(    #12
        0x9,
        (
            "If either one of these groups\x01",
            "saw what was written in that\x01",
            "stolen ledger...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        (
            "Yikes...\x01",
            "I'd be in a world of hurt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FC")

    Jump("loc_C78")

    label("loc_7FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_90D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CC")
    OP_A2(0x1)

    ChrTalk(    #14
        0x9,
        "Store sales are going rather well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "It bothers me that these craftsmen\x01",
            "aren't very serviceable, but whatever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "Hee hee... Now if I can just keep\x01",
            "making money like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90A")

    label("loc_8CC")


    ChrTalk(    #17
        0x9,
        (
            "Hee hee...Now if I can just keep\x01",
            "making money like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90A")

    Jump("loc_C78")

    label("loc_90D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_A60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EC")
    OP_A2(0x1)

    ChrTalk(    #18
        0x9,
        (
            "My boss is way too trusting\x01",
            "of others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        (
            "In any case, it's impossible to get\x01",
            "along for long in the business\x01",
            "world like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "Which is why I should be running\x01",
            "the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        "Gya ha ha ha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A5D")

    label("loc_9EC")


    ChrTalk(    #22
        0x9,
        (
            "My boss is way too trusting\x01",
            "of others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "Which is why I should be running\x01",
            "the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        "Gya ha ha ha!\x02",
    )

    CloseMessageWindow()

    label("loc_A5D")

    Jump("loc_C78")

    label("loc_A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_BF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B56")
    OP_A2(0x1)

    ChrTalk(    #25
        0x9,
        (
            "La la la...\x01",
            "Money, money, money...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        "Gya ha ha ha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        "I can't stop laughing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "Who would have thought I'd be able\x01",
            "to get my own factory this easy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "In this world it's only the smart\x01",
            "people who remain on top.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEE")

    label("loc_B56")


    ChrTalk(    #30
        0x9,
        (
            "Who would have thought I'd be able\x01",
            "to get my own factory this easy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "I can't stop laughing! Only the smart\x01",
            "people remain on top in this world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEE")

    Jump("loc_C78")

    label("loc_BF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_C78")

    ChrTalk(    #32
        0x9,
        (
            "So I'll be running the show\x01",
            "starting today, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x9,
        (
            "Excellent! Now it's time to make\x01",
            "some real money!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        "Gya ha ha!\x02",
    )

    CloseMessageWindow()

    label("loc_C78")

    TalkEnd(0x9)
    Return()

    # Function_4_3FB end

    def Function_5_C7C(): pass

    label("Function_5_C7C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_DF8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D14")

    ChrTalk(    #35
        0xFE,
        "It looks like my boss is back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "This is great. Now I can focus my\x01",
            "attention on pursuing new skills\x01",
            "without any worries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF5")

    label("loc_D14")


    ChrTalk(    #37
        0xFE,
        (
            "It looks like my boss was led\x01",
            "away by the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I only want to create things. As long\x01",
            "as there is an environment for that I\x01",
            "could care less about anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "But a shop with no boss has\x01",
            "me a little worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF5")

    Jump("loc_1335")

    label("loc_DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_FCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F40")
    OP_A2(0x2)

    ChrTalk(    #40
        0xFE,
        (
            "My boss seems to be more\x01",
            "on edge than I've ever seen\x01",
            "him before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I wonder if it's the shock from\x01",
            "being burglarized like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "I'm only interested in pursuing\x01",
            "my own creative interests...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "So as long as there's an environment\x01",
            "for me to do that, I couldn't care less\x01",
            "about anything else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCA")

    label("loc_F40")


    ChrTalk(    #44
        0xFE,
        (
            "My boss seems to be more\x01",
            "on edge than I've ever seen\x01",
            "him before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "I wonder if it's the shock from\x01",
            "being burglarized like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FCA")

    Jump("loc_1335")

    label("loc_FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_105A")

    ChrTalk(    #46
        0xFE,
        (
            "Wow, it looks like the burglars\x01",
            "made off with nearly everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I could have sworn that my boss\x01",
            "locked up last night...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1335")

    label("loc_105A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_113B")

    ChrTalk(    #48
        0xFE,
        (
            "I refuse to make anything that\x01",
            "distorts my aesthetic tastes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "But my new boss often makes\x01",
            "demands for crude products...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "And just seeing his face alone\x01",
            "makes my will to create wither\x01",
            "like a dried reed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1335")

    label("loc_113B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_11E5")

    ChrTalk(    #51
        0xFE,
        (
            "My new boss is a pain in the behind\x01",
            "about orders and all kinds of things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "In comparison, my old boss gave\x01",
            "me the freedom to do all kinds\x01",
            "of things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1335")

    label("loc_11E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_12CF")

    ChrTalk(    #53
        0xFE,
        (
            "Unfortunately, before I knew it,\x01",
            "Nigel had taken over the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "I'm only interested in pursuing\x01",
            "my own creative interests...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "So as long as there is an environment\x01",
            "to do that I could care less who my\x01",
            "boss is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1335")

    label("loc_12CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1335")

    ChrTalk(    #56
        0xFE,
        (
            "I haven't seen my boss\x01",
            "around recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "I wonder if he's gotten sick\x01",
            "or something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1335")

    TalkEnd(0xA)
    Return()

    # Function_5_C7C end

    def Function_6_1339(): pass

    label("Function_6_1339")

    TalkBegin(0xB)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1399")
    OP_0D()
    OP_A9(0xB)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_1399")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13AA")
    TalkEnd(0xB)
    Return()

    label("loc_13AA")

    Call(0, 7)
    OP_8C(0xB, 180, 0)
    Return()

    # Function_6_1339 end

    def Function_7_13B6(): pass

    label("Function_7_13B6")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_14A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_145D")
    OP_A2(0x3)

    ChrTalk(    #58
        0xB,
        (
            "The army returned my products which\x01",
            "were stolen by the sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xB,
        (
            "Now I can finally settle down and\x01",
            "get back to business as usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_149E")

    label("loc_145D")


    ChrTalk(    #60
        0xB,
        (
            "I sure hope the sky bandits will\x01",
            "get what's coming to them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149E")

    Jump("loc_1D68")

    label("loc_14A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1623")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_158B")
    OP_A2(0x3)

    ChrTalk(    #61
        0xB,
        (
            "I wonder if the army found the\x01",
            "crooks who did this to my shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        (
            "I sure hope they catch these crooks no\x01",
            "matter what they have to do to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xB,
        (
            "As it stands, I am seething with\x01",
            "anger over what happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1620")

    label("loc_158B")


    ChrTalk(    #64
        0xB,
        (
            "I wonder if the army found the\x01",
            "crooks who did this to my shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xB,
        (
            "I sure hope they catch these crooks no\x01",
            "matter what they have to do to them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1620")

    Jump("loc_1D68")

    label("loc_1623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_17D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_174E")
    OP_A2(0x3)

    ChrTalk(    #66
        0xB,
        "Damn it!\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0xB,
        (
            "My shop got ripped off by a bunch\x01",
            "of thieving criminals!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "And they took off with every last\x01",
            "one of my pricey goods, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xB,
        (
            "Why did this have to happen to me\x01",
            "at a time when there are hardly any\x01",
            "goods around to begin with...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D0")

    label("loc_174E")


    ChrTalk(    #70
        0xB,
        (
            "Damn it! I got ripped off by a\x01",
            "bunch of thieving crooks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xB,
        (
            "And they took off with every last\x01",
            "one of my pricey goods, too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D0")

    Jump("loc_1D68")

    label("loc_17D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1994")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18DB")
    OP_A2(0x3)

    ChrTalk(    #72
        0xB,
        (
            "I really struggled a lot and worked\x01",
            "hard when the market began.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xB,
        (
            "And I think it's because of that hard\x01",
            "work and experience that I have\x01",
            "my own shop now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xB,
        (
            "I think learning to start at the bottom\x01",
            "of the heap is important for anyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1991")

    label("loc_18DB")


    ChrTalk(    #75
        0xB,
        (
            "I'm sure it's because of my hard\x01",
            "work and experience at the market\x01",
            "that I own my own shop now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xB,
        (
            "I think learning to start at the bottom\x01",
            "of the heap is important for anyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1991")

    Jump("loc_1D68")

    label("loc_1994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1B92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF7")
    OP_A2(0x3)

    ChrTalk(    #77
        0xB,
        (
            "Pretty much any of the merchants\x01",
            "in Bose had their starting point in\x01",
            "the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xB,
        (
            "First you start in the market, which is subsidized\x01",
            "by the city, then after gaining experience you're\x01",
            "able to get approval to start your own store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xB,
        (
            "And it's for that reason that people\x01",
            "have come here from far and wide\x01",
            "to become merchants.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8F")

    label("loc_1AF7")


    ChrTalk(    #80
        0xB,
        (
            "First you start in the market, which is subsidized\x01",
            "by the city, then after gaining experience you're\x01",
            "able to get approval to start your own store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8F")

    Jump("loc_1D68")

    label("loc_1B92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C70")
    OP_A2(0x3)

    ChrTalk(    #81
        0xB,
        (
            "When I was a lad, I set up my\x01",
            "own store at the Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xB,
        (
            "Nowadays when I go there,\x01",
            "it all feels so nostalgic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xB,
        (
            "Now if we could just get all the young\x01",
            "bucks to work hard like that too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CFF")

    label("loc_1C70")


    ChrTalk(    #84
        0xB,
        (
            "When I was a lad, I set up my own\x01",
            "store at the Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xB,
        (
            "Now if we could just get all the young\x01",
            "bucks to work hard like that too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CFF")

    Jump("loc_1D68")

    label("loc_1D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1D68")

    ChrTalk(    #86
        0xB,
        "Good afternoon and welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xB,
        (
            "Take a look around and see if\x01",
            "there's anything you like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D68")

    TalkEnd(0xB)
    Return()

    # Function_7_13B6 end

    def Function_8_1D6C(): pass

    label("Function_8_1D6C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1EE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5E")
    OP_A2(0x0)

    ChrTalk(    #88
        0xFE,
        (
            "I came here to make a deal, but it\x01",
            "looks like the store manager has\x01",
            "changed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Well, I guess it's back to the\x01",
            "drawing board.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "I wonder when I'll be able to bring back\x01",
            "some good news to the Imperial City.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE5")

    label("loc_1E5E")


    ChrTalk(    #91
        0xFE,
        (
            "I came here to make a deal, but it\x01",
            "looks like the store manager has\x01",
            "changed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "Well, I guess it's back to the\x01",
            "drawing board.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE5")

    Jump("loc_1FF5")

    label("loc_1EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F7C")
    OP_A2(0x0)

    ChrTalk(    #93
        0xFE,
        (
            "It looks like this store was hit\x01",
            "by the burglars as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I guess this isn't the time to be\x01",
            "talking about business deals...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FF5")

    label("loc_1F7C")


    ChrTalk(    #95
        0xFE,
        (
            "Even still, when we've got reporters already\x01",
            "on the scene, why doesn't somebody\x01",
            "hurry up and call the Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF5")

    TalkEnd(0x8)
    Return()

    # Function_8_1D6C end

    def Function_9_1FF9(): pass

    label("Function_9_1FF9")

    TalkBegin(0xC)

    ChrTalk(    #96
        0xC,
        (
            "#141FThanks to your shenanigans, the pages\x01",
            "of the next issue are going to be filled\x01",
            "with some real gripping headlines.\x02\x03",

            "Let me know if you get any other\x01",
            "scoops.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_9_1FF9 end

    def Function_10_20A6(): pass

    label("Function_10_20A6")

    TalkBegin(0xD)

    ChrTalk(    #97
        0xD,
        (
            "#150FThe newest model of camera on\x01",
            "display here was stolen.\x02\x03",

            "Do you think the sky bandits have\x01",
            "an interest in photography?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_10_20A6 end

    def Function_11_212D(): pass

    label("Function_11_212D")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_234D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A4")
    OP_A2(0x4)

    ChrTalk(    #98
        0xE,
        (
            "Nigel's evil business practices\x01",
            "were finally exposed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xE,
        (
            "Now this store officially belongs\x01",
            "to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xE,
        (
            "Though I have mixed feelings, I guess\x01",
            "this is a learning experience for me\x01",
            "as a merchant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xE,
        (
            "Maybe I was too generous and trusting\x01",
            "of everyone in my previous days as a\x01",
            "merchant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xE,
        (
            "Though I hate to say it, Nigel\x01",
            "made me realize this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_234A")

    label("loc_22A4")


    ChrTalk(    #103
        0xE,
        (
            "And he was a companion who experienced\x01",
            "the joys and sorrows of business with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xE,
        (
            "I should probably drop by and take him\x01",
            "a little something sooner or later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_234A")

    Jump("loc_2409")

    label("loc_234D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2409")

    ChrTalk(    #105
        0xE,
        (
            "Nigel was arrested and taken\x01",
            "to the Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xE,
        (
            "I guess it's back to managing\x01",
            "the factory for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xE,
        (
            "It looks like old Nigel was involved\x01",
            "in some really shady business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2409")

    TalkEnd(0xE)
    Return()

    # Function_11_212D end

    def Function_12_240D(): pass

    label("Function_12_240D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2437")
    Sleep(500)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFA312, 0x0, 0x166AC, 0xBB8, 0x0)

    label("loc_2437")

    OP_8E(0xFE, 0xFFFFA61E, 0x0, 0x15E82, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xD, 400)
    Return()

    # Function_12_240D end

    def Function_13_2453(): pass

    label("Function_13_2453")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2482")
    Sleep(500)
    Sleep(500)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFA312, 0x0, 0x166AC, 0xBB8, 0x0)

    label("loc_2482")

    OP_8E(0xFE, 0xFFFFA89E, 0x0, 0x1615C, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xC, 400)
    Return()

    # Function_13_2453 end

    def Function_14_249E(): pass

    label("Function_14_249E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24C3")
    Sleep(500)
    OP_8E(0xFE, 0xFFFFA312, 0x0, 0x166AC, 0xBB8, 0x0)

    label("loc_24C3")

    OP_8E(0xFE, 0xFFFFA24A, 0x0, 0x15C16, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xC, 400)
    Return()

    # Function_14_249E end

    def Function_15_24DF(): pass

    label("Function_15_24DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24FF")
    OP_8E(0xFE, 0xFFFFA312, 0x0, 0x166AC, 0xBB8, 0x0)

    label("loc_24FF")

    OP_8E(0xFE, 0xFFFFAC5E, 0x0, 0x15E46, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xC, 400)
    Return()

    # Function_15_24DF end

    def Function_16_251B(): pass

    label("Function_16_251B")

    EventBegin(0x0)
    OP_6D(-23490, 0, 87480, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    SetChrPos(0xD, -24322, 0, 85809, 270)
    SetChrPos(0xC, -21888, 0, 88170, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E1")
    SetChrPos(0x101, -28760, -2000, 92070, 180)
    SetChrPos(0x102, -28760, -2000, 92070, 180)
    SetChrPos(0x103, -28760, -2000, 92070, 180)
    SetChrPos(0x104, -28760, -2000, 92070, 180)
    Jump("loc_2625")

    label("loc_25E1")

    SetChrPos(0x101, -21890, 0, 91590, 180)
    SetChrPos(0x102, -21160, 0, 92440, 180)
    SetChrPos(0x103, -20430, 0, 91410, 180)
    SetChrPos(0x104, -22770, 0, 92110, 180)

    label("loc_2625")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #108
        0xD,
        (
            "#151FYay! This one turned out really\x01",
            "cute.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 400)

    ChrTalk(    #109
        0xD,
        (
            "#150FNial, is this how you wanted\x01",
            "this one?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 400)

    ChrTalk(    #110
        0xC,
        (
            "#140FYeah, sure. Something like that.\x02\x03",

            "#140FHowever, we really got screwed,\x01",
            "you know that?\x02\x03",

            "#142FHmm...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2712():
        OP_8C(0xC, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2712)

    def lambda_2720():
        OP_6D(-22600, 0, 89590, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2720)
    OP_43(0x101, 0x1, 0x0, 0xC)
    OP_43(0x102, 0x1, 0x0, 0xD)
    OP_43(0x103, 0x1, 0x0, 0xF)
    OP_43(0x104, 0x1, 0x0, 0xE)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #111
        0x102,
        (
            "#010F#4PGood afternoon. Are you working\x01",
            "on another story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#000F#6PLooks like you two are on the\x01",
            "trail of a scoop again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xC,
        "#141FHey! It's you kids!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xD,
        "#153FOh! Estelle and Joshua!\x02",
    )

    CloseMessageWindow()
    OP_8E(0xD, 0xFFFFA646, 0x0, 0x15568, 0xBB8, 0x0)
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #115
        0xD,
        (
            "#151FBoy, am I glad to see that they\x01",
            "let you out of the clinker!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xC,
        (
            "#141FYeah. I heard all about you kids\x01",
            "getting arrested by the army up\x01",
            "at the old mine.\x02\x03",

            "You certainly had me worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#007F#6PWhy are you acting like you had\x01",
            "nothing to do with it?\x02\x03",

            "It was your info that led us\x01",
            "to the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xC,
        (
            "#141FHey, now! What kinda face is that?\x01",
            "Don't tell me you blame us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        (
            "#010F#4PDid you go and check out the\x01",
            "abandoned mine yourselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xD,
        (
            "#150FYeah, we did yesterday.\x02\x03",

            "#150FBut it was after you all had\x01",
            "already been hauled off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xC,
        (
            "#142FWe could have had a really great\x01",
            "shot of your arrest had we been\x01",
            "there...\x02\x03",

            "#147FIt really guts me that we missed\x01",
            "such a perfect opportunity for a\x01",
            "great shot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#009F#6PI-I swear...you people in the news\x01",
            "business...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x103,
        (
            "#020FBut anyway, I was wondering if\x01",
            "you thought this looked like the\x01",
            "handiwork of the sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xC,
        (
            "#140FIt sure looks that way to me.\x02\x03",

            "It seems that the army is sniffing\x01",
            "around for clues, too...\x02\x03",

            "But to be honest, it looks like\x01",
            "there's nothing to be found here\x01",
            "anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x103,
        (
            "#026FI see. That does make things\x01",
            "a bit more difficult...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x104,
        (
            "#030FWell, Mr. Reporter, why don't you\x01",
            "let me ask you this, then.\x02\x03",

            "Do you know from whence the\x01",
            "sky bandits entered town?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x104, 400)

    ChrTalk(    #127
        0xC,
        (
            "#140FAccording to witness statements,\x01",
            "they were seen leaving through\x01",
            "the west gate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x104,
        (
            "#030FWell that's awfully strange.\x02\x03",

            "The mayor's residence and Bose Market\x01",
            "are right through the west gate...\x02\x03",

            "And it seems like attacking those\x01",
            "two places would be far more\x01",
            "lucrative.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xC,
        (
            "#143FWhen you put it that way, that\x01",
            "makes a lot of sense.\x02\x03",

            "#142FBut if you don't mind me asking...\x01",
            "who the heck are you, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x104,
        (
            "#035FHa, I'm glad you asked.\x02\x03",

            "I'm Olivier Lenheim...a wandering\x01",
            "bard and gifted musician.\x02\x03",

            "I'm sure you've heard rumors about\x01",
            "me, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xD,
        (
            "#151FOh, right, you're the guy who drank\x01",
            "wine without paying at that classy\x01",
            "restaurant.\x02\x03",

            "It takes guts to stiff such a big\x01",
            "bill! It's an honor to meet you, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x104,
        (
            "#031FHa ha, you're making me blush.\x02\x03",

            "I'm ready for my interview any time,\x01",
            "so don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #133
        0xD,
        "#151FWow, really?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #134
        0x101,
        (
            "#007F#6PI'm getting a headache just listening\x01",
            "to this crap...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x102,
        "#019FThese two...are very much alike.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xC,
        (
            "#145FI'm not even going to ask how\x01",
            "this guy wound up with the rest\x01",
            "of you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x103,
        "#021FThat...would be for the best.\x02",
    )

    CloseMessageWindow()
    OP_28(0x37, 0x1, 0x2)
    OP_4B(0xC, 255)
    OP_4B(0xD, 255)
    EventEnd(0x0)
    Return()

    # Function_16_251B end

    SaveToFile()

Try(main)
