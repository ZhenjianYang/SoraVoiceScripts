from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4120   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Carna',                                # 9
        'Shepard',                              # 10
        'Chaeli',                               # 11
        'Zacharias',                            # 12
        'Tom',                                  # 13
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
        'ED6_DT07/CH01240 ._CH',             # 00
        'ED6_DT07/CH01680 ._CH',             # 01
        'ED6_DT07/CH01690 ._CH',             # 02
        'ED6_DT07/CH01140 ._CH',             # 03
        'ED6_DT07/CH01040 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01240P._CP',             # 00
        'ED6_DT07/CH01680P._CP',             # 01
        'ED6_DT07/CH01690P._CP',             # 02
        'ED6_DT07/CH01140P._CP',             # 03
        'ED6_DT07/CH01040P._CP',             # 04
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
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -1540,
        Z                   = 0,
        Y                   = 69240,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 1260,
        Z                   = 0,
        Y                   = -240,
        Direction           = 236,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 58580,
        Z                   = 0,
        Y                   = 360,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 120030,
        Z                   = 0,
        Y                   = -1260,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = -10,
        TriggerZ            = 0,
        TriggerY            = -1600,
        TriggerRange        = 800,
        ActorX              = 1260,
        ActorZ              = 1500,
        ActorY              = -240,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60410,
        TriggerZ            = 0,
        TriggerY            = 390,
        TriggerRange        = 800,
        ActorX              = 58580,
        ActorZ              = 1500,
        ActorY              = 360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 119960,
        TriggerZ            = 0,
        TriggerY            = 650,
        TriggerRange        = 800,
        ActorX              = 120030,
        ActorZ              = 1500,
        ActorY              = -1260,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_27D",          # 01, 1
        "Function_2_2CA",          # 02, 2
        "Function_3_2E0",          # 03, 3
        "Function_4_2E5",          # 04, 4
        "Function_5_E85",          # 05, 5
        "Function_6_E8A",          # 06, 6
        "Function_7_1C08",         # 07, 7
        "Function_8_22ED",         # 08, 8
        "Function_9_22F2",         # 09, 9
        "Function_10_352A",        # 0A, 10
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_200")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 5480, 4000, -2590, 90)

    label("loc_200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_20A")
    Jump("loc_27C")

    label("loc_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_214")
    Jump("loc_27C")

    label("loc_214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_21E")
    Jump("loc_27C")

    label("loc_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_228")
    Jump("loc_27C")

    label("loc_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_232")
    Jump("loc_27C")

    label("loc_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_23C")
    Jump("loc_27C")

    label("loc_23C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_246")
    Jump("loc_27C")

    label("loc_246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_250")
    Jump("loc_27C")

    label("loc_250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_26B")
    SetChrPos(0x9, 3310, 0, 129900, 0)
    Jump("loc_27C")

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_275")
    Jump("loc_27C")

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_27C")

    label("loc_27C")

    Return()

    # Function_0_1DE end

    def Function_1_27D(): pass

    label("Function_1_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B0")
    OP_B1("t4120_y")
    Jump("loc_2B9")

    label("loc_2B0")

    OP_B1("t4120_n")

    label("loc_2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_2C9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C9")

    Return()

    # Function_1_27D end

    def Function_2_2CA(): pass

    label("Function_2_2CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2CA")

    label("loc_2DF")

    Return()

    # Function_2_2CA end

    def Function_3_2E0(): pass

    label("Function_3_2E0")

    Call(0, 4)
    Return()

    # Function_3_2E0 end

    def Function_4_2E5(): pass

    label("Function_4_2E5")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_381")

    ChrTalk(    #0
        0xC,
        (
            "What a beautiful day. Perfect\x01",
            "weather for celebrating Her\x01",
            "Majesty's birthday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xC,
        (
            "Aaaanyway, time to get to work.\x01",
            "Got a lot to do today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E81")

    label("loc_381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3C3")

    ChrTalk(    #2
        0xC,
        "Not many customers today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xC,
        "Something going on?\x02",
    )

    CloseMessageWindow()
    Jump("loc_E81")

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_51E")

    ChrTalk(    #4
        0xC,
        (
            "It's important to listen to one's\x01",
            "customers. I mean, they pay the\x01",
            "bills, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xC,
        (
            "I've always felt that if a customer needs help\x01",
            "after hours--I mean REALLY needs help--then\x01",
            "I'll gladly stay late and do what I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xC,
        (
            "Gotta make sure Zacharias signs off\x01",
            "on it, though. And if I do it too\x01",
            "often, he'll tell me to take a hike!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E81")

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5AC")

    ChrTalk(    #7
        0xC,
        "We'll be closing soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xC,
        (
            "But I've still got to hurry up and\x01",
            "try to get these rush-jobs finished.\x01",
            "I owe it to our customers!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E81")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_64F")

    ChrTalk(    #9
        0xC,
        (
            "Today's the final match of the\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xC,
        (
            "I'll be finishing up repairs while\x01",
            "my customers are enjoying themselves\x01",
            "at the match.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E81")

    label("loc_64F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_7E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6B9")

    ChrTalk(    #11
        0xC,
        (
            "I don't know how good an idea it was\x01",
            "to let the sky bandits into the\x01",
            "competition...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E1")

    label("loc_6B9")

    OP_A2(0x3)

    ChrTalk(    #12
        0xC,
        (
            "The Martial Arts Competition seems\x01",
            "livelier than ever this year. You\x01",
            "can FEEL the energy in the air!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xC,
        (
            "All the customers who come to\x01",
            "pick up their orders just can't\x01",
            "stop talking about it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xC,
        (
            "I don't know how good an idea it was\x01",
            "to let the sky bandits into the\x01",
            "competition, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E1")

    Jump("loc_E81")

    label("loc_7E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_972")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_849")

    ChrTalk(    #15
        0xC,
        (
            "I like feeling that I've helped\x01",
            "people using my brains and my\x01",
            "own two hands...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96F")

    label("loc_849")

    OP_A2(0x3)

    ChrTalk(    #16
        0xC,
        (
            "I like feeling that I've helped\x01",
            "people using my brains and my\x01",
            "own two hands...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xC,
        (
            "From a grandfather's treasured\x01",
            "watch, to a child's favorite\x01",
            "toy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xC,
        (
            "I love seeing the smiles on their faces when\x01",
            "they get back their precious keepsakes, working\x01",
            "just as they did when they were new.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96F")

    Jump("loc_E81")

    label("loc_972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A13")

    ChrTalk(    #19
        0xC,
        (
            "I feel like I have a responsibility\x01",
            "to fix anything I've sold to a\x01",
            "customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xC,
        (
            "But I'll repair things even\x01",
            "if they weren't bought here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE2")

    label("loc_A13")

    OP_A2(0x3)

    ChrTalk(    #21
        0xC,
        (
            "I always listen to my customers.\x01",
            "I make a point of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xC,
        (
            "I feel like I have a responsibility\x01",
            "to fix anything I've sold to a\x01",
            "customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        (
            "But I'll repair things even\x01",
            "if they weren't bought here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE2")

    Jump("loc_E81")

    label("loc_AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_CA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B9A")

    ChrTalk(    #24
        0xC,
        (
            "Do I want to see the tournament? Absolutely!\x01",
            "But I have work to do here, and it would be\x01",
            "remiss of me to put all of that aside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xC,
        "The customer comes first!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA3")

    label("loc_B9A")

    OP_A2(0x3)

    ChrTalk(    #26
        0xC,
        (
            "Today marks the beginning of what\x01",
            "promises to be another spectacular\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xC,
        (
            "I'd love to go see the fighters in action,\x01",
            "but I have work to do here, and it would be\x01",
            "remiss of me to put all of that aside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xC,
        "The customer comes first!\x02",
    )

    CloseMessageWindow()

    label("loc_CA3")

    Jump("loc_E81")

    label("loc_CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_DB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D0F")

    ChrTalk(    #29
        0xC,
        (
            "I was beginning to think the\x01",
            "Martial Arts Competition would\x01",
            "be canceled this year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DAD")

    label("loc_D0F")

    OP_A2(0x3)

    ChrTalk(    #30
        0xC,
        (
            "With the queen bedridden and all\x01",
            "this coup d'etat nonsense...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xC,
        (
            "I was beginning to think the\x01",
            "Martial Arts Competition would\x01",
            "be canceled this year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAD")

    Jump("loc_E81")

    label("loc_DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_E81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E0A")

    ChrTalk(    #32
        0xC,
        (
            "The 3rd floor is where we handle\x01",
            "all repair and maintenance orders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E81")

    label("loc_E0A")

    OP_A2(0x3)

    ChrTalk(    #33
        0xC,
        "Welcome to the Wingard Orbal Factory!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xC,
        (
            "The 3rd floor is where we handle\x01",
            "all repair and maintenance orders.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E81")

    TalkEnd(0xC)
    Return()

    # Function_4_2E5 end

    def Function_5_E85(): pass

    label("Function_5_E85")

    Call(0, 6)
    Return()

    # Function_5_E85 end

    def Function_6_E8A(): pass

    label("Function_6_E8A")

    TalkBegin(0xB)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF5")
    OP_0D()
    OP_A9(0x5A)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_EF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F06")
    TalkEnd(0xB)
    Return()

    label("loc_F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1025")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F54")

    ChrTalk(    #35
        0xB,
        (
            "I'm so glad Her Majesty has\x01",
            "recovered from her illness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1022")

    label("loc_F54")

    OP_A2(0x2)

    ChrTalk(    #36
        0xB,
        (
            "With the town's spirits up, so\x01",
            "too are my customer numbers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xB,
        (
            "During the Birthday Celebration,\x01",
            "my sales increase by a factor of\x01",
            "five.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        (
            "I'm so glad Her Majesty has\x01",
            "recovered from her illness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1022")

    Jump("loc_1C04")

    label("loc_1025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_10AD")

    ChrTalk(    #39
        0xB,
        (
            "These 'anti-terror' patrols are\x01",
            "really restricting my customers'\x01",
            "freedoms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "What a fine mess this coup has\x01",
            "made, no?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C04")

    label("loc_10AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_123D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_114C")

    ChrTalk(    #41
        0xB,
        (
            "We depend on the festivities this time of year\x01",
            "to make ends meet. If we're in the red, we're\x01",
            "dead; if we're in the black, we'll be back!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123A")

    label("loc_114C")

    OP_A2(0x2)

    ChrTalk(    #42
        0xB,
        (
            "It's positively amazing how much\x01",
            "money I've made off of the Martial\x01",
            "Arts Competition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "We depend on the festivities this time of year\x01",
            "to make ends meet. If we're in the red, we're\x01",
            "dead; in we're in the black, we'll be back!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123A")

    Jump("loc_1C04")

    label("loc_123D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_12BD")

    ChrTalk(    #44
        0xB,
        "Okay, it's about closing time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xB,
        (
            "I look forward to tallying the\x01",
            "day's sales whenever I close up\x01",
            "the register.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C04")

    label("loc_12BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1497")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_138F")

    ChrTalk(    #46
        0xB,
        (
            "I'd be ecstatic if you used Wingard-\x01",
            "branded Quartz to win it all in the\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xB,
        (
            "And of course, if that WERE to\x01",
            "happen, an endorsement would be\x01",
            "appreciated as well!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1494")

    label("loc_138F")

    OP_A2(0x2)

    ChrTalk(    #48
        0xB,
        (
            "Hey, aren't you guys the bracers\x01",
            "who made it to the finals?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xB,
        (
            "I'd be ecstatic if you used Wingard-\x01",
            "branded Quartz to win it all in the\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        (
            "And of course, if that WERE to\x01",
            "happen, an endorsement would be\x01",
            "appreciated as well!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1494")

    Jump("loc_1C04")

    label("loc_1497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_15AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1500")

    ChrTalk(    #51
        0xB,
        (
            "I'm really looking forward to seeing\x01",
            "how much money I'll be able to make\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A8")

    label("loc_1500")

    OP_A2(0x2)

    ChrTalk(    #52
        0xB,
        (
            "I'm eager to see who'll win the\x01",
            "tournament, of course...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xB,
        (
            "...but what I'm really looking forward\x01",
            "to is seeing how much money I'll be able\x01",
            "to make tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A8")

    Jump("loc_1C04")

    label("loc_15AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_16B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1620")

    ChrTalk(    #54
        0xB,
        (
            "I run this store with my buddy Tom,\x01",
            "but the two of us never seem to agree\x01",
            "on much of anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AD")

    label("loc_1620")

    OP_A2(0x2)

    ChrTalk(    #55
        0xB,
        (
            "I run this store with my old\x01",
            "childhood buddy Tom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xB,
        "He's a real hard-worker.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xB,
        (
            "But we don't see eye-to-eye\x01",
            "on a lot of things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AD")

    Jump("loc_1C04")

    label("loc_16B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1839")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1754")

    ChrTalk(    #58
        0xB,
        (
            "We get a lot of orders to repair\x01",
            "and customize during the Martial\x01",
            "Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xB,
        (
            "See, we make our real money selling\x01",
            "new merchandise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1836")

    label("loc_1754")

    OP_A2(0x2)

    ChrTalk(    #60
        0xB,
        (
            "And it's nice we have so many new\x01",
            "customers this time of year...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xB,
        (
            "But we're spending all of our\x01",
            "time fixing or rebuilding items,\x01",
            "which translates into fewer sales.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        (
            "And sales are where we make our\x01",
            "REAL profit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1836")

    Jump("loc_1C04")

    label("loc_1839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_19ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_18E1")

    ChrTalk(    #63
        0xB,
        (
            "I'd be ecstatic if you used Wingard-\x01",
            "branded Quartz to win it all in the\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xB,
        (
            "It'd make for good advertising,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19EA")

    label("loc_18E1")

    OP_A2(0x2)

    ChrTalk(    #65
        0xB,
        (
            "Hey, are you guys taking part\x01",
            "in the tournament?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xB,
        (
            "I'm going to be closing up shop\x01",
            "soon, so I'll probably see you\x01",
            "there. I can't wait!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xB,
        (
            "I'd be ecstatic if you used Wingard-\x01",
            "branded Quartz to win it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "It'd make for good advertising,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19EA")

    Jump("loc_1C04")

    label("loc_19ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1A8D")

    ChrTalk(    #69
        0xB,
        (
            "After the Royal Guardsmen stopped\x01",
            "coming in here, we lost a decent\x01",
            "chunk of our sales.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xB,
        (
            "Coup d'etats aren't always so\x01",
            "good for business, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C04")

    label("loc_1A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1C04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1B57")

    ChrTalk(    #71
        0xB,
        (
            "Got some orbments that just won't work right?\x01",
            "Bring 'em on down! Here at the Wingard Orbal\x01",
            "Factory, no job is too big or small!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xB,
        (
            "We're professionals here. You\x01",
            "can count on us!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C04")

    label("loc_1B57")

    OP_A2(0x2)

    ChrTalk(    #73
        0xB,
        "You guys bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xB,
        (
            "If so, then come on in and let\x01",
            "Wingard Orbal Factory take care\x01",
            "of all your orbment needs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xB,
        (
            "We're professionals here. You\x01",
            "can count on us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C04")

    TalkEnd(0xB)
    Return()

    # Function_6_E8A end

    def Function_7_1C08(): pass

    label("Function_7_1C08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1C35")

    ChrTalk(    #76
        0xFE,
        "It's pretty hopping today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_1C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1CA0")

    ChrTalk(    #77
        0xFE,
        (
            "Did you see them too? Those royal\x01",
            "soldiers in black armor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "They're really unnerving...\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_1CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1CFC")

    ChrTalk(    #79
        0xFE,
        (
            "Don't you think it's a bit TOO\x01",
            "quiet, considering the tournament\x01",
            "just ended?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_1CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1D6B")

    ChrTalk(    #80
        0xFE,
        (
            "The shop's calmed down a bit\x01",
            "since the tournament ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "Seems like I can finally relax...\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_1D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DAB")

    ChrTalk(    #82
        0xFE,
        (
            "If only I were a bit better with\x01",
            "words...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E20")

    label("loc_1DAB")

    OP_A2(0x0)

    ChrTalk(    #83
        0xFE,
        (
            "*sigh* If only I were a bit better\x01",
            "with words...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "When I'm around people, I just\x01",
            "don't know what to say.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E20")

    Jump("loc_22E9")

    label("loc_1E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1E92")

    ChrTalk(    #85
        0xFE,
        "I'm going out with my wife tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "So that means I have to get all\x01",
            "this work done today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_1E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1FFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F42")

    ChrTalk(    #87
        0xFE,
        (
            "It looks like we have enough\x01",
            "merchandise for now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "With this much in stock, we should\x01",
            "be totally okay until after the\x01",
            "Queen's Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FF9")

    label("loc_1F42")

    OP_A2(0x0)

    ChrTalk(    #89
        0xFE,
        (
            "So the people who were in here in\x01",
            "handcuffs the other day apparently\x01",
            "participated in the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Who lets criminals take part\x01",
            "in sporting events?! I mean,\x01",
            "seriously!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF9")

    Jump("loc_22E9")

    label("loc_1FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_20CA")

    ChrTalk(    #91
        0xFE,
        (
            "When the tournament starts, a\x01",
            "lot of the participants usually\x01",
            "come through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "It's always highly unnerving ordering\x01",
            "the parts and items I'll need before\x01",
            "the flood of people arrive...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_20CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_218C")

    ChrTalk(    #93
        0xFE,
        (
            "Orbal guns and rifles and such--\x01",
            "that sort of thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Yesterday alone, practically the\x01",
            "whole store was bought out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Our selection is pretty limited\x01",
            "right now as a result.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_218C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_21EF")

    ChrTalk(    #96
        0xFE,
        (
            "Welcome! Please take your time,\x01",
            "and let me know if you need any\x01",
            "help with anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_21EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_22E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_226C")

    ChrTalk(    #97
        0xFE,
        (
            "I'm not very good at talking\x01",
            "with customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "I generally let my wife handle\x01",
            "that part of the job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_226C")

    OP_A2(0x0)

    ChrTalk(    #99
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "I'm not very good at talking\x01",
            "with customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I generally let my wife handle\x01",
            "that part of the job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E9")

    TalkEnd(0xFE)
    Return()

    # Function_7_1C08 end

    def Function_8_22ED(): pass

    label("Function_8_22ED")

    Call(0, 9)
    Return()

    # Function_8_22ED end

    def Function_9_22F2(): pass

    label("Function_9_22F2")

    TalkBegin(0xA)
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
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235E")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2353")
    OP_A9(0x60)
    Jump("loc_2355")

    label("loc_2353")

    OP_A9(0x5B)

    label("loc_2355")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_235E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_236F")
    TalkEnd(0xA)
    Return()

    label("loc_236F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_245D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_23D1")

    ChrTalk(    #102
        0xA,
        (
            "I'm glad Her Majesty has gotten\x01",
            "better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xA,
        "The kingdom can rest easy now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_245A")

    label("loc_23D1")


    ChrTalk(    #104
        0xA,
        (
            "Queen Alicia and Princess Klaudia\x01",
            "were so radiant!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xA,
        (
            "I'm glad Her Majesty has gotten\x01",
            "better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        "The kingdom can rest easy now.\x02",
    )

    CloseMessageWindow()

    label("loc_245A")

    Jump("loc_3526")

    label("loc_245D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_24C8")

    ChrTalk(    #107
        0xA,
        (
            "We haven't had many customers\x01",
            "today, and it's rather odd, since\x01",
            "the weather's quite nice...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3526")

    label("loc_24C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2606")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_253D")

    ChrTalk(    #108
        0xA,
        (
            "With Her Majesty still sick, I just\x01",
            "have no idea what will become of her\x01",
            "Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2603")

    label("loc_253D")


    ChrTalk(    #109
        0xA,
        (
            "Those black-armored soldiers\x01",
            "have been all over the town\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xA,
        "...Such a commotion...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xA,
        (
            "With Her Majesty still sick, I just\x01",
            "have no idea what will become of her\x01",
            "Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2603")

    Jump("loc_3526")

    label("loc_2606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2889")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_2787")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_269A")

    ChrTalk(    #112
        0xA,
        (
            "That was the fiercest fight\x01",
            "I've seen in many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xA,
        (
            "I was extremely impressed. You\x01",
            "may count me among your fans.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2784")

    label("loc_269A")

    OP_A2(0x1)

    ChrTalk(    #114
        0xA,
        "You did wonderful out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xA,
        (
            "Congratulations on your victory.\x01",
            "That was some incredible match!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xA,
        (
            "It was the fiercest fight I've\x01",
            "seen in many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xA,
        "I was extremely impressed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xA,
        "You may count me among your fans.\x02",
    )

    CloseMessageWindow()

    label("loc_2784")

    Jump("loc_2886")

    label("loc_2787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_27ED")

    ChrTalk(    #119
        0xA,
        (
            "Today's final match was simply\x01",
            "amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xA,
        (
            "I'm so glad I took off work to\x01",
            "go see it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2886")

    label("loc_27ED")

    OP_A2(0x1)

    ChrTalk(    #121
        0xA,
        (
            "Today's final match was simply\x01",
            "amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xA,
        (
            "That was the fiercest fight\x01",
            "I've seen in many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xA,
        (
            "I'm so glad I took off work to\x01",
            "go see it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2886")

    Jump("loc_3526")

    label("loc_2889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_29AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_293A")

    ChrTalk(    #124
        0xA,
        (
            "Oh, it's you guys. So, today's\x01",
            "the final match, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xA,
        (
            "I'm just about to close shop, and then\x01",
            "I'll be heading out to cheer for you--\x01",
            "louder than anyone!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29AC")

    label("loc_293A")


    ChrTalk(    #126
        0xA,
        (
            "The final day of the tournament\x01",
            "already? My, how time flies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xA,
        (
            "I hope I can go see some of the\x01",
            "matches!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29AC")

    Jump("loc_3526")

    label("loc_29AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2D12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A1E")

    ChrTalk(    #128
        0xA,
        (
            "If you want my advice, you should\x01",
            "turn in early tonight. Rest up real\x01",
            "good for tomorrow!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D0F")

    label("loc_2A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C8B")
    OP_A2(0x1)
    OP_A2(0x67B)

    ChrTalk(    #129
        0xA,
        "Oh, hey, it's you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xA,
        (
            "I hear you made it to the finals.\x01",
            "Congratulations!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        "#001FThanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x102,
        "#010FThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xA,
        (
            "Apparently, you were quite the\x01",
            "showstoppers, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xA,
        (
            "And I was cheering for you, of course, so\x01",
            "I can hold my nose up high for a while.\x01",
            "Chaeli's team's gonna take it all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#006FHeh heh! Now it's just a hop, skip\x01",
            "and a jump to full-on victory!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        (
            "#018F(Yeah, like it's really that\x01",
            "easy...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xA,
        (
            "Well, you've gotten this far... Don't see\x01",
            "why you WOULDN'T win the championship.\x01",
            "I mean, you guys got the GOODS, yo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xA,
        (
            "Best of luck to you--not that\x01",
            "you'll need it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D0F")

    label("loc_2C8B")

    OP_A2(0x1)

    ChrTalk(    #139
        0xA,
        (
            "Everyone is saying that today's\x01",
            "match was a real keeper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xA,
        (
            "You can FEEL their excitement\x01",
            "as they recount every detail...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D0F")

    Jump("loc_3526")

    label("loc_2D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_30D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_2D92")

    ChrTalk(    #141
        0xA,
        (
            "We're going to close the shop\x01",
            "and go watch the finals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xA,
        (
            "Best of luck to you--not that\x01",
            "you'll need it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30D6")

    label("loc_2D92")

    OP_A2(0x67A)

    ChrTalk(    #143
        0xA,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xA,
        (
            "Are you participants in the Martial\x01",
            "Arts Competition, by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x108,
        "#073FActually, yes we are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xA,
        "I knew it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xA,
        (
            "I'd heard about a team with one\x01",
            "big dude, one little dude and\x01",
            "a rough-and-tumble little lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xA,
        (
            "You guys totally have my support.\x01",
            "I'll be cheering for you louder\x01",
            "than anyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#008FReally? Wow, thanks! I'll be sure\x01",
            "to listen for you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xA,
        "Yaaay! So, can I get your autographs?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        "#004FOur a-autographs? Seriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x102,
        (
            "#019FI...don't even know what to say.\x01",
            "No one's ever asked me for my\x01",
            "autograph before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xA,
        (
            "Usually I'm working, so I can't\x01",
            "get to the arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xA,
        (
            "But we're going to close up shop\x01",
            "to go see the final match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xA,
        (
            "I sure hope it turns out you'll\x01",
            "be in it, so we can see you guys\x01",
            "in action!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#001FYou bet! It doesn't matter who we\x01",
            "face, we'll be there, for sure!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30D6")

    Jump("loc_3526")

    label("loc_30D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_31B0")

    ChrTalk(    #157
        0xA,
        (
            "Usually the military leaves everyone else\x01",
            "in the dust, but this year...it's hard to\x01",
            "say, with so many entrants!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xA,
        (
            "I can't wait to find out who\x01",
            "wins. It's going to be the best\x01",
            "tournament year EVER!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3526")

    label("loc_31B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3344")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3265")

    ChrTalk(    #159
        0xA,
        (
            "Yesterday, some people in handcuffs\x01",
            "were escorted into the shop by\x01",
            "soldiers...to buy weapons!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xA,
        (
            "Don't you usually try to take\x01",
            "weapons AWAY from criminals?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3341")

    label("loc_3265")

    OP_A2(0x1)

    ChrTalk(    #161
        0xA,
        (
            "Yesterday, some people in handcuffs\x01",
            "were escorted into the shop by\x01",
            "soldiers...to buy weapons!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xA,
        (
            "Don't you usually try to take\x01",
            "weapons AWAY from criminals?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xA,
        (
            "I'd really love to know who\x01",
            "the heck they were!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3341")

    Jump("loc_3526")

    label("loc_3344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_34D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_33EA")

    ChrTalk(    #164
        0xA,
        (
            "The sub-commander of the Royal\x01",
            "Guardsman used to come in here\x01",
            "all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xA,
        (
            "He was always concerned about Her\x01",
            "Majesty. Such a nice person!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D3")

    label("loc_33EA")

    OP_A2(0x1)

    ChrTalk(    #166
        0xA,
        (
            "Still can't believe the Royal\x01",
            "Guardsman were behind the terro-\x01",
            "rist attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xA,
        (
            "The sub-commander of the Royal\x01",
            "Guardsman used to come in here\x01",
            "all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xA,
        (
            "He was always concerned about Her\x01",
            "Majesty. Such a nice person!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D3")

    Jump("loc_3526")

    label("loc_34D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3526")

    ChrTalk(    #169
        0xA,
        "Braaaaaacers! Welcome to the shop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xA,
        "Please, have a look around!\x02",
    )

    CloseMessageWindow()

    label("loc_3526")

    TalkEnd(0xA)
    Return()

    # Function_9_22F2 end

    def Function_10_352A(): pass

    label("Function_10_352A")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38C2")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(4690, 4000, -2480, 0)
    SetChrPos(0x101, 4350, 4000, -2160, 90)
    SetChrPos(0x102, 4390, 4000, -3250, 90)
    SetChrPos(0x108, 3200, 4000, -2630, 90)
    TurnDirection(0x8, 0x108, 0)
    OP_A2(0x64B)
    OP_28(0x4B, 0x1, 0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35BD")
    OP_28(0x4B, 0x1, 0x100)

    label("loc_35BD")

    OP_0D()
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #171
        0x101,
        "#004FHi, Carna!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x8,
        (
            "#830FHey, look who it is!\x02\x03",

            "Ooh, you've got old man Zin\x01",
            "with you. What's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x108,
        "#074FWell, it's a long story...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x8,
        "#832FUh-oh. Sounds serious.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #175
        "\x07\x05Explained the situation and the queen's request to Carna.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #176
        0x8,
        (
            "#832F...Uhh...\x02\x03",

            "...You're not just pulling my\x01",
            "leg, are you?\x02\x03",

            "#833FI must admit, I did find it a bit\x01",
            "odd that all the gates and ports\x01",
            "and such have been shut down...\x02\x03",

            "#832FSooo, what did you want with me,\x01",
            "exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x102,
        (
            "#012FWell, we need to get everyone\x01",
            "together and formulate a plan.\x02\x03",

            "So if you would, please meet us\x01",
            "at the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x8,
        (
            "#832FGot'cha.\x02\x03",

            "I'm already there!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3846():

        label("loc_3846")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3846")

    QueueWorkItem2(0x101, 1, lambda_3846)

    def lambda_3857():

        label("loc_3857")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3857")

    QueueWorkItem2(0x102, 1, lambda_3857)

    def lambda_3868():

        label("loc_3868")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3868")

    QueueWorkItem2(0x108, 1, lambda_3868)
    OP_8E(0x8, 0x1522, 0xFA0, 0x276, 0xFA0, 0x0)
    OP_8E(0x8, 0xC58, 0xFA0, 0x9F6, 0xFA0, 0x0)
    OP_8E(0x8, 0xFFFFF254, 0x0, 0x9F6, 0xFA0, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    EventEnd(0x0)

    label("loc_38C2")

    TalkEnd(0x8)
    Return()

    # Function_10_352A end

    SaveToFile()

Try(main)
