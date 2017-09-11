from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2401   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2401.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60083",
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
        'Zack',                                 # 9
        'Solomon',                              # 10
        'Gull Seaside Way',                     # 11
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
        'ED6_DT07/CH01460 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT06/CH20059 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01460P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT06/CH20059P._CP',             # 02
    )

    DeclNpc(
        X                   = -7120,
        Z                   = 0,
        Y                   = 37380,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -6060,
        Z                   = 0,
        Y                   = 37610,
        Direction           = 13,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 1060,
        Z                   = 0,
        Y                   = -23220,
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


    DeclEvent(
        X                   = -2580,
        Y                   = 2000,
        Z                   = 3190,
        Range               = 2800,
        Unknown_10          = 0xFFFFF448,
        Unknown_14          = 0x578,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )


    DeclActor(
        TriggerX            = 1370,
        TriggerZ            = 0,
        TriggerY            = 30050,
        TriggerRange        = 1000,
        ActorX              = 1370,
        ActorZ              = 0,
        ActorY              = 30050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3480,
        TriggerZ            = 0,
        TriggerY            = 34330,
        TriggerRange        = 1000,
        ActorX              = 3480,
        ActorZ              = 0,
        ActorY              = 34330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6440,
        TriggerZ            = 160,
        TriggerY            = 23740,
        TriggerRange        = 1200,
        ActorX              = 6440,
        ActorZ              = 1000,
        ActorY              = 23740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12030,
        TriggerZ            = 0,
        TriggerY            = 18180,
        TriggerRange        = 1200,
        ActorX              = 12030,
        ActorZ              = 0,
        ActorY              = 18180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3580,
        TriggerZ            = 0,
        TriggerY            = 7000,
        TriggerRange        = 1000,
        ActorX              = 3580,
        ActorZ              = 0,
        ActorY              = 7000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3040,
        TriggerZ            = 0,
        TriggerY            = 8250,
        TriggerRange        = 1000,
        ActorX              = -3040,
        ActorZ              = 0,
        ActorY              = 8250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12390,
        TriggerZ            = 0,
        TriggerY            = 25680,
        TriggerRange        = 1000,
        ActorX              = 12390,
        ActorZ              = 500,
        ActorY              = 25680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7430,
        TriggerZ            = 0,
        TriggerY            = 39210,
        TriggerRange        = 1000,
        ActorX              = 7430,
        ActorZ              = 700,
        ActorY              = 39210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -8700,
        TriggerZ            = 0,
        TriggerY            = 35870,
        TriggerRange        = 1000,
        ActorX              = -8700,
        ActorZ              = 700,
        ActorY              = 35870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5150,
        TriggerZ            = -200,
        TriggerY            = 15360,
        TriggerRange        = 1000,
        ActorX              = -5150,
        ActorZ              = -200,
        ActorY              = 15360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5610,
        TriggerZ            = -280,
        TriggerY            = 16930,
        TriggerRange        = 1000,
        ActorX              = 5610,
        ActorZ              = -280,
        ActorY              = 16930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4980,
        TriggerZ            = -350,
        TriggerY            = 23150,
        TriggerRange        = 1000,
        ActorX              = -4980,
        ActorZ              = -350,
        ActorY              = 23150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2F2",          # 00, 0
        "Function_1_32C",          # 01, 1
        "Function_2_397",          # 02, 2
        "Function_3_3AD",          # 03, 3
        "Function_4_5FE",          # 04, 4
        "Function_5_905",          # 05, 5
        "Function_6_10D0",         # 06, 6
        "Function_7_122A",         # 07, 7
        "Function_8_1424",         # 08, 8
        "Function_9_148A",         # 09, 9
        "Function_10_14F2",        # 0A, 10
        "Function_11_1553",        # 0B, 11
        "Function_12_15B5",        # 0C, 12
        "Function_13_1612",        # 0D, 13
        "Function_14_1676",        # 0E, 14
        "Function_15_263F",        # 0F, 15
    )


    def Function_0_2F2(): pass

    label("Function_0_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_30D")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)

    label("loc_30D")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_319"),
        (SWITCH_DEFAULT, "loc_32B"),
    )


    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328")
    OP_A2(0x420)
    Event(0, 5)

    label("loc_328")

    Jump("loc_32B")

    label("loc_32B")

    Return()

    # Function_0_2F2 end

    def Function_1_32C(): pass

    label("Function_1_32C")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE5A20, 0x30068)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_356")
    OP_B1("t2401_y")
    Jump("loc_35F")

    label("loc_356")

    OP_B1("t2401_n")

    label("loc_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_END)), "loc_396")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_64(0x7, 0x1)
    OP_64(0x8, 0x1)
    OP_64(0x9, 0x1)
    OP_64(0xA, 0x1)
    OP_64(0xB, 0x1)

    label("loc_396")

    Return()

    # Function_1_32C end

    def Function_2_397(): pass

    label("Function_2_397")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_397")

    label("loc_3AC")

    Return()

    # Function_2_397 end

    def Function_3_3AD(): pass

    label("Function_3_3AD")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480")
    OP_A2(0x1)

    ChrTalk(    #0
        0xFE,
        "Man, I was in shock yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I mean, seeing the sky go all\x01",
            "red in the east over Manoria...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "I tried to get here as quickly\x01",
            "as I could, but everything was\x01",
            "already gone...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_533")

    label("loc_480")

    OP_A3(0x1)

    ChrTalk(    #3
        0xFE,
        (
            "By the way, why is everything\x01",
            "all scattered around like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "It was dark when I got here\x01",
            "yesterday, so I'm not sure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "But even the herb garden is\x01",
            "all torn up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_533")

    OP_A2(0x424)
    Call(0, 14)
    Jump("loc_5FA")

    label("loc_53D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_5C3")

    ChrTalk(    #6
        0xFE,
        (
            "Phew... Maybe I should take\x01",
            "a breather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I'd like to at least find some of the\x01",
            "kids' things to bring back to them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FA")

    label("loc_5C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_END)), "loc_5FA")

    ChrTalk(    #8
        0xFE,
        (
            "Hey, mighty bracer.\x01",
            "You find anything out?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FA")

    TalkEnd(0x9)
    Return()

    # Function_3_3AD end

    def Function_4_5FE(): pass

    label("Function_4_5FE")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_758")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CE")
    OP_A2(0x0)

    ChrTalk(    #9
        0xFE,
        (
            "Since the fire's burned so much,\x01",
            "I guess the only thing to do is\x01",
            "to rebuild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I don't know what Matron Theresa\x01",
            "is going to do... I mean, it's going\x01",
            "to be really expensive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74E")

    label("loc_6CE")

    OP_A3(0x0)

    ChrTalk(    #11
        0xFE,
        (
            "Maybe they can get stuff at\x01",
            "a discount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "I owe them a little, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Now'd be the perfect time to\x01",
            "pay them back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74E")

    OP_A2(0x425)
    Call(0, 14)
    Jump("loc_901")

    label("loc_758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_7CD")

    ChrTalk(    #14
        0xFE,
        (
            "I've finished doing some cleanup\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "All I can do now is wait to see\x01",
            "what you find out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_901")

    label("loc_7CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_END)), "loc_901")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_882")
    OP_A2(0x0)

    ChrTalk(    #16
        0xFE,
        (
            "I've known Matron Theresa ever\x01",
            "since I was a kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "The people who fought the fire\x01",
            "sure were dedicated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I just can't understand why\x01",
            "this happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_901")

    label("loc_882")


    ChrTalk(    #19
        0xFE,
        (
            "I've known Matron Theresa ever\x01",
            "since I was a kid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Fighting the fire took some\x01",
            "serious dedication, let me\x01",
            "tell you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_901")

    TalkEnd(0x8)
    Return()

    # Function_4_5FE end

    def Function_5_905(): pass

    label("Function_5_905")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_28(0x3B, 0x1, 0x1)
    OP_28(0x3B, 0x1, 0x2)
    OP_28(0x3B, 0x1, 0x4)
    OP_6D(-490, 8000, 30040, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, 850, 0, 15900, 0)
    SetChrPos(0x102, -290, 0, 15900, 0)
    FadeToBright(2000, 0)

    def lambda_969():
        OP_6C(0, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_969)
    OP_67(0, 17000, -10000, 0)
    OP_67(0, 9500, -10000, 5000)

    def lambda_99B():
        OP_8E(0xFE, 0x352, 0x0, 0x60E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_99B)
    Sleep(500)

    def lambda_9BB():
        OP_8E(0xFE, 0xFFFFFEDE, 0x14, 0x5E88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9BB)
    OP_6D(190, 0, 25000, 4000)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #21
        0x101,
        "#003FThis is terrible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        "#013FIt's just...gone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "#4PWell, who do we have here?\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)

    def lambda_A53():

        label("loc_A53")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_A53")

    QueueWorkItem2(0x101, 1, lambda_A53)

    def lambda_A64():

        label("loc_A64")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_A64")

    QueueWorkItem2(0x102, 1, lambda_A64)

    def lambda_A75():
        OP_6D(-450, 40, 26930, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A75)

    def lambda_A8D():
        OP_8E(0xFE, 0xFFFFEC00, 0x78, 0x78E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A8D)
    Sleep(600)

    def lambda_AAD():
        OP_8E(0xFE, 0xFFFFEC00, 0x78, 0x78E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_AAD)
    WaitChrThread(0x8, 0x1)

    def lambda_ACD():
        OP_8E(0xFE, 0x276, 0x0, 0x6A36, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_ACD)
    WaitChrThread(0x9, 0x1)

    def lambda_AED():
        OP_8E(0xFE, 0xFFFFFE5C, 0x1E, 0x6A36, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_AED)
    WaitChrThread(0x8, 0x2)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x9, 0x2)
    OP_8C(0x9, 180, 400)

    ChrTalk(    #24
        0x9,
        (
            "#1PAre you here from the\x01",
            "Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#002FY-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#012FYou're all from Manoria, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#2PYeah... We came to help pick\x01",
            "up the pieces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#2PWe were here last night around\x01",
            "midnight, trying to fight the\x01",
            "fire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#2PAs you can see...it could\x01",
            "have gone better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#005FSo, then...what about Matron\x01",
            "Theresa and the kids?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        "#1PThey're all fine. Don't worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "#1PRight now, they're sleeping\x01",
            "at Manoria's inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x9,
        (
            "#1PGiven the size of the fire,\x01",
            "it's a miracle that no one\x01",
            "was badly hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#007FThank goodness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#011FYes, at least that's something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "#2PWe're here now to clean up\x01",
            "what we can. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        "#2PHow about you two?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#501FWe really ought to check up\x01",
            "on everyone at the inn...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0x1)
    OP_8C(0x102, 45, 400)

    ChrTalk(    #39
        0x102,
        "#015FSorry, but that'll have to wait.\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_8C(0x101, 225, 400)

    ChrTalk(    #40
        0x101,
        "#004FHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        (
            "#012FNow that we're here at the scene\x01",
            "of the crime, there's a lot that\x01",
            "strikes me as weird.\x02\x03",

            "We need to find what clues\x01",
            "we can, before the trail goes\x01",
            "cold, so to speak.\x02\x03",

            "...I know how you feel, but this\x01",
            "HAS to take precedence right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#003F...\x02\x03",

            "#500FRight...\x01",
            "We're bracers, after all...\x02\x03",

            "#002FWe have to find out what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        (
            "#010FRight...so let's see what we\x01",
            "can find.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "#1PLooks like you'll have your\x01",
            "hands full.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        "#2PGood luck!\x02",
    )

    CloseMessageWindow()

    def lambda_1014():

        label("loc_1014")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1014")

    QueueWorkItem2(0x101, 1, lambda_1014)

    def lambda_1025():

        label("loc_1025")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1025")

    QueueWorkItem2(0x102, 1, lambda_1025)

    def lambda_1036():
        OP_6D(190, 0, 24500, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1036)
    OP_8C(0x9, 315, 400)

    def lambda_1055():
        OP_8E(0xFE, 0xFFFFE67E, 0x0, 0x812E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1055)
    Sleep(300)
    OP_8C(0x8, 315, 400)

    def lambda_107C():
        OP_8E(0xFE, 0xFFFFE67E, 0x0, 0x812E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_107C)
    WaitChrThread(0x9, 0x1)
    SetChrPos(0x9, -6060, 0, 37610, 13)
    WaitChrThread(0x8, 0x1)
    SetChrPos(0x8, -7120, 0, 37380, 315)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_5_905 end

    def Function_6_10D0(): pass

    label("Function_6_10D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B2")
    EventBegin(0x0)
    OP_6D(3480, 0, 34330, 1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #46
        "\x07\x05What was once a wall is now rubble.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #47
        0x101,
        (
            "#002FWow... This place is ruined.\x02\x03",

            "Hey... Do you smell something\x01",
            "strange?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        "#012FYes...and I think I know why...\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_1219")

    label("loc_11B2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #49
        (
            "\x07\x05The strange smell is strongest\x01",
            "where the walls have collapsed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_1219")

    OP_A2(0x8)
    OP_A2(0x422)
    OP_28(0x3B, 0x1, 0x10)
    Call(0, 14)
    Return()

    # Function_6_10D0 end

    def Function_7_122A(): pass

    label("Function_7_122A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A6")
    EventBegin(0x0)
    OP_6D(1240, 0, 30880, 1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x05The door has been completely wrecked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #51
        0x101,
        (
            "#004FUgh... It's all pitch black.\x02\x03",

            "#002FHuh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        "#014FWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#002FMaybe this is just me...\x02\x03",

            "...but does the hinge there look\x01",
            "weird to you? Like it's been torn\x01",
            "off or something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        (
            "#012FIt does, actually.\x02\x03",

            "As if it happened before the\x01",
            "fire started.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_1413")

    label("loc_13A6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x05The hinge of the broken door appears to have been forcibly torn off.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_1413")

    OP_A2(0x9)
    OP_A2(0x423)
    OP_28(0x3B, 0x1, 0x8)
    Call(0, 14)
    Return()

    # Function_7_122A end

    def Function_8_1424(): pass

    label("Function_8_1424")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #56
        "\x07\x05The herbs have been uprooted and strewn about the garden.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x3)
    TalkEnd(0xFF)
    Return()

    # Function_8_1424 end

    def Function_9_148A(): pass

    label("Function_9_148A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #57
        "\x07\x05The stump seats around the table have been scattered about.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x2)
    TalkEnd(0xFF)
    Return()

    # Function_9_148A end

    def Function_10_14F2(): pass

    label("Function_10_14F2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #58
        "\x07\x05The soil from the flower bed is all over the ground.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x4)
    TalkEnd(0xFF)
    Return()

    # Function_10_14F2 end

    def Function_11_1553(): pass

    label("Function_11_1553")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #59
        "\x07\x05The firewood for the stove has been scattered around.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x5)
    TalkEnd(0xFF)
    Return()

    # Function_11_1553 end

    def Function_12_15B5(): pass

    label("Function_12_15B5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #60
        "\x07\x05A milk tank has fallen on its side and is empty.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x6)
    TalkEnd(0xFF)
    Return()

    # Function_12_15B5 end

    def Function_13_1612(): pass

    label("Function_13_1612")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #61
        "\x07\x05The barrels with food in them have been scorched black.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x7)
    TalkEnd(0xFF)
    Return()

    # Function_13_1612 end

    def Function_14_1676(): pass

    label("Function_14_1676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_263E")
    OP_A2(0x427)
    OP_28(0x3B, 0x1, 0x20)
    OP_28(0x3B, 0x1, 0x40)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(1740, 0, 29000, 0)
    OP_6C(0, 0)
    AddParty(0x35, 0xFF)
    SetChrPos(0x101, 1070, 0, 28010, 90)
    SetChrPos(0x102, 2840, 0, 27990, 270)
    SetChrPos(0x136, 1810, 0, 26160, 45)
    SetChrFlags(0x136, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #62
        0x102,
        (
            "#012F#2PAll right... We've taken a good\x01",
            "look around.\x02\x03",

            "#012FWhat do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#002F#1PI'm not sure, to be honest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x102,
        (
            "#013F#2PFirst off, the fire doesn't appear\x01",
            "to have started in the building.\x02\x03",

            "It most likely started outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#004F#1POutside...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x102,
        "#012F#2POver here.\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_1840():
        OP_6D(3590, 0, 34040, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1840)

    def lambda_1858():
        OP_6C(315000, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1858)

    def lambda_1868():
        OP_8E(0xFE, 0x105E, 0x0, 0x82E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1868)
    Sleep(500)
    OP_8E(0x101, 0xC08, 0x0, 0x712A, 0xBB8, 0x0)

    def lambda_189C():
        OP_8E(0xFE, 0x10D6, 0x0, 0x7DC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_189C)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 315, 400)

    ChrTalk(    #67
        0x102,
        (
            "#012F#4PIt looks like this area is the\x01",
            "point of origin.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #68
        0x101,
        (
            "#004FAhh... Where the wall collapsed.\x02\x03",

            "#002FBut how can you tell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        (
            "#013F#4PBecause the fire damage is worse\x01",
            "here than anywhere else.\x02\x03",

            "Compare it to the areas nearby\x01",
            "and you'll see.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(200)
    OP_8C(0x101, 90, 400)
    Sleep(200)
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #70
        0x101,
        "#002FOh, you're right...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #71
        0x102,
        (
            "#012F#4PSo it started here,\x01",
            "and then spread.\x02\x03",

            "You know what this means?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #72
        0x101,
        "#002FUh, well...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[It got caught in a forest fire.]\x01",            # 0
            "[Someone set the fire on purpose.]\x01",           # 1
            "[There was an accident with a lantern.]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B32"),
        (1, "loc_1C8F"),
        (2, "loc_1D42"),
        (SWITCH_DEFAULT, "loc_1EC2"),
    )


    label("loc_1B32")


    ChrTalk(    #73
        0x102,
        (
            "#013F#4PIt's true that the trees behind\x01",
            "the house were burned black...\x02\x03",

            "But I think that's just because the\x01",
            "fire from the building had spread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#004FSo, maybe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#015F#4PIt had to be arson.\x02\x03",

            "#012FThat smell everywhere? It's\x01",
            "some highly flammable oil.\x02\x03",

            "It's everywhere around here,\x01",
            "so this had to be the fire's\x01",
            "point of origin.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x3B, 0x1)
    Jump("loc_1EC2")

    label("loc_1C8F")


    ChrTalk(    #76
        0x102,
        (
            "#015F#4PMy thoughts exactly.\x02\x03",

            "#012FThat smell everywhere? It's\x01",
            "some highly flammable oil.\x02\x03",

            "It's everywhere around here,\x01",
            "so this had to be the fire's\x01",
            "point of origin.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x3B, 0x2)
    Jump("loc_1EC2")

    label("loc_1D42")


    ChrTalk(    #77
        0x102,
        (
            "#013F#4PWell, some kind of accelerant\x01",
            "was certainly used to start it.\x02\x03",

            "But if memory serves, this area\x01",
            "wasn't lit with lanterns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#004FThat's a pretty good memory\x01",
            "you've got there...\x02\x03",

            "#004FSo, maybe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        (
            "#015F#4PIt had to be arson.\x02\x03",

            "#012FThat smell everywhere? It's\x01",
            "some highly flammable oil.\x02\x03",

            "It's everywhere around here,\x01",
            "so this had to be the fire's\x01",
            "point of origin.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC2")

    label("loc_1EC2")


    ChrTalk(    #80
        0x101,
        "#003FNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        (
            "#013F#4PPlus, don't you think it's weird\x01",
            "how everything outside is\x01",
            "scattered around?\x02\x03",

            "Even the people fighting the\x01",
            "fire wouldn't have done that\x01",
            "to the herb garden.\x02\x03",

            "It's not a coincidence.\x01",
            "Someone did this.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #82
        0x136,
        "Girl's Voice",
        "#2PIs...that true...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x136, 0x80)

    def lambda_2010():
        OP_6D(4110, 0, 29630, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2010)

    def lambda_2028():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2028)
    OP_8C(0x101, 225, 400)
    TurnDirection(0x102, 0x136, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #83
        0x101,
        "#004F#4PKloe?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x102,
        "#014FI didn't know you were here...\x02",
    )

    CloseMessageWindow()

    def lambda_2088():
        OP_6D(2000, 0, 27550, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2088)

    def lambda_20A0():
        OP_8E(0xFE, 0xA50, 0x0, 0x691E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20A0)
    Sleep(300)

    def lambda_20C0():
        OP_8E(0xFE, 0xDCA, 0x0, 0x6978, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20C0)
    WaitChrThread(0x101, 0x1)

    def lambda_20E0():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20E0)
    WaitChrThread(0x102, 0x1)

    def lambda_20F3():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_20F3)

    ChrTalk(    #85
        0x136,
        (
            "#049FBut...why? Why would anyone\x01",
            "do this...?\x02\x03",

            "I have so many irreplaceable\x01",
            "memories of this place...\x02\x03",

            "#046FWhy...? How? How could someone\x01",
            "do anything so cruel...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        "#003F#2PKloe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        "#013F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x136,
        (
            "#049F...\x02\x03",

            "I'm sorry...\x01",
            "I'm just...so confused...\x02\x03",

            "I... I...\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0x136, 0x258, 0x3E8, 0x0)
    Fade(500)
    SetChrPos(0x136, 2060, 0, 26360, 45)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x136, 0x2)
    ClearChrFlags(0x136, 0x1)
    SetChrChipByIndex(0x136, 2)
    SetChrSubChip(0x136, 1)
    OP_0D()

    ChrTalk(    #89
        0x101,
        (
            "#003F#2PYou're not alone in that feeling.\x02\x03",

            "I barely know the place, and\x01",
            "this bothers the heck out of\x01",
            "me, too...\x02\x03",

            "It's hard to believe that anyone\x01",
            "could be capable of something\x01",
            "this awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x136,
        "#043FEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#006F#2PBut the matron and the kids\x01",
            "are all okay...\x02\x03",

            "...so we can be thankful for\x01",
            "that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x136,
        (
            "#049F...\x02\x03",

            "#047FThank you... That does help.\x02\x03",

            "I'd just started morning classes\x01",
            "when the dean came to see me...\x02\x03",

            "He said that he'd heard that\x01",
            "the orphanage was in flames...\x02\x03",

            "And while I was on my way here...all I could\x01",
            "think about was, they're fine. They're alive.\x01",
            "Aidios was watching over them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#000F#2P...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0x136, 1810, 0, 26160, 45)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x136, 0x2)
    SetChrFlags(0x136, 0x1)
    SetChrChipByIndex(0x136, 65535)
    SetChrSubChip(0x136, 0)
    OP_0D()
    OP_94(0x1, 0x101, 0xB4, 0x1F4, 0x3E8, 0x0)

    ChrTalk(    #94
        0x102,
        (
            "#010F#2PWell, we heard that they're all\x01",
            "at the inn in Manoria, safe and\x01",
            "sound.\x02\x03",

            "We just finished up here, so\x01",
            "we're planning to go see them.\x01",
            "Do you want to come with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x136,
        (
            "#048FY-Yes... I would like that\x01",
            "very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#006F#2PAll right, then.\x01",
            "To Manoria we go.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_64(0x7, 0x1)
    OP_64(0x8, 0x1)
    OP_64(0x9, 0x1)
    OP_64(0xA, 0x1)
    OP_64(0xB, 0x1)
    EventEnd(0x0)

    label("loc_263E")

    Return()

    # Function_14_1676 end

    def Function_15_263F(): pass

    label("Function_15_263F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2727")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26C1")

    ChrTalk(    #97
        0x102,
        (
            "#013FI do understand, but we'll\x01",
            "have to go and visit later.\x02\x03",

            "If we don't find out how this\x01",
            "happened...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_270C")

    ChrTalk(    #98
        0x102,
        (
            "#012F(For now, we can just search\x01",
            "here, on the premises.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_270C")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_2727")

    Return()

    # Function_15_263F end

    SaveToFile()

Try(main)
