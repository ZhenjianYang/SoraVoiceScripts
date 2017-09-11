from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4313   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4313.x',
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
        'Chamberlain Fate',                     # 9
        'Special Ops Soldier',                  # 10
        'Special Ops Soldier',                  # 11
        'Special Ops Soldier',                  # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
        'Kloe',                                 # 15
        'Olivier',                              # 16
        'Scherazard',                           # 17
        '1st Lieutenant Schwarz',               # 18
        'Sieg',                                 # 19
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
        'ED6_DT07/CH00100 ._CH',             # 00
        'ED6_DT07/CH00101 ._CH',             # 01
        'ED6_DT07/CH00110 ._CH',             # 02
        'ED6_DT07/CH00111 ._CH',             # 03
        'ED6_DT07/CH00170 ._CH',             # 04
        'ED6_DT07/CH00171 ._CH',             # 05
        'ED6_DT07/CH01570 ._CH',             # 06
        'ED6_DT07/CH01330 ._CH',             # 07
        'ED6_DT07/CH02340 ._CH',             # 08
        'ED6_DT07/CH00030 ._CH',             # 09
        'ED6_DT07/CH00020 ._CH',             # 0A
        'ED6_DT07/CH02090 ._CH',             # 0B
        'ED6_DT07/CH02320 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH00100P._CP',             # 00
        'ED6_DT07/CH00101P._CP',             # 01
        'ED6_DT07/CH00110P._CP',             # 02
        'ED6_DT07/CH00111P._CP',             # 03
        'ED6_DT07/CH00170P._CP',             # 04
        'ED6_DT07/CH00171P._CP',             # 05
        'ED6_DT07/CH01570P._CP',             # 06
        'ED6_DT07/CH01330P._CP',             # 07
        'ED6_DT07/CH02340P._CP',             # 08
        'ED6_DT07/CH00030P._CP',             # 09
        'ED6_DT07/CH00020P._CP',             # 0A
        'ED6_DT07/CH02090P._CP',             # 0B
        'ED6_DT07/CH02320P._CP',             # 0C
    )

    DeclNpc(
        X                   = -11780,
        Z                   = 0,
        Y                   = 20150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 25980,
        TriggerZ            = 0,
        TriggerY            = 50580,
        TriggerRange        = 800,
        ActorX              = 25690,
        ActorZ              = 1000,
        ActorY              = 51500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22140,
        TriggerZ            = 0,
        TriggerY            = 50600,
        TriggerRange        = 800,
        ActorX              = 21830,
        ActorZ              = 890,
        ActorY              = 51760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2BA",          # 00, 0
        "Function_1_2EB",          # 01, 1
        "Function_2_2EC",          # 02, 2
        "Function_3_67F",          # 03, 3
        "Function_4_1444",         # 04, 4
        "Function_5_1598",         # 05, 5
        "Function_6_163C",         # 06, 6
    )


    def Function_0_2BA(): pass

    label("Function_0_2BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2C8")
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_2C8")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_2D4"),
        (SWITCH_DEFAULT, "loc_2EA"),
    )


    label("loc_2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E7")
    OP_A2(0x656)
    Event(0, 3)

    label("loc_2E7")

    Jump("loc_2EA")

    label("loc_2EA")

    Return()

    # Function_0_2BA end

    def Function_1_2EB(): pass

    label("Function_1_2EB")

    Return()

    # Function_1_2EB end

    def Function_2_2EC(): pass

    label("Function_2_2EC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54A")
    OP_A2(0x679)
    OP_28(0x4C, 0x1, 0x10)
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #0
        (
            "\x07\x05Explained that the beautiful\x01",
            "door inside was locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #1
        0x8,
        "Locked, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "I'm pretty sure the head of the\x01",
            "Special Ops had the key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "He's gone, though. Said something\x01",
            "about terrorists and left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#000FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#010FThat means they're headed toward\x01",
            "where Julia and the others are\x01",
            "waiting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x108,
        (
            "#070FThis is bad. We haven't got\x01",
            "any time to lose here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        "One moment!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "There should be a spare of that\x01",
            "key, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "I believe it was hidden somewhere \x01",
            "in the Gallery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#000FThe Gallery, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        "#010FLet's go check.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_67B")

    label("loc_54A")


    ChrTalk(    #12
        0xFE,
        (
            "You should find them all gathered\x01",
            "together in the Crest Room--all\x01",
            "the way back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "It's a very historical room,\x01",
            "actually. Used for the treaty\x01",
            "signing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#000FIn the back, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "There should be a spare of that\x01",
            "key lurking around here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "I believe it was hidden in the\x01",
            "Gallery.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67B")

    TalkEnd(0x8)
    Return()

    # Function_2_2EC end

    def Function_3_67F(): pass

    label("Function_3_67F")

    EventBegin(0x0)
    OP_6D(-14960, 0, 17380, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, -11780, 0, 20150, 225)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -16850, 0, 13660, 45)
    SetChrPos(0x108, -18160, 0, 13760, 45)
    SetChrPos(0x102, -16690, 0, 12820, 45)
    SetChrPos(0x9, -10960, 0, 18200, 352)
    SetChrPos(0xA, -12000, 0, 18190, 61)
    SetChrPos(0xB, -15540, 0, 19130, 135)
    SetChrPos(0xC, -14400, 0, 18870, 285)
    SetChrPos(0xD, -18830, 0, 18070, 82)

    ChrTalk(    #17
        0x8,
        "Who...who are you people...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#000FCrap... We totally picked\x01",
            "the wrong room!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7B4():
        TurnDirection(0xFE, 0x101, 150)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7B4)
    TurnDirection(0xB, 0x101, 200)

    ChrTalk(    #19
        0xB,
        (
            "Hmm...\x01",
            "What are you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xC,
        (
            "*hic*...\x01",
            "Ain't seen you before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#010FGood evening.\x01",
            "We're with the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_84A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_84A)

    def lambda_858():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_858)
    OP_96(0xD, 0xFFFFBA00, 0x0, 0x465A, 0x12C, 0xBB8)
    TurnDirection(0xD, 0x101, 200)

    ChrTalk(    #22
        0xD,
        "Huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x108,
        (
            "#070FNo need to get up. Just enjoy\x01",
            "yourselves and rest well.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8D2():
        OP_8E(0xFE, 0xFFFFC7AC, 0x0, 0x7210, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_8D2)

    def lambda_8ED():
        OP_8E(0xFE, 0xFFFFC3C4, 0x0, 0x481C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8ED)

    def lambda_908():
        OP_8E(0xFE, 0x550, 0x0, 0x8642, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_908)
    OP_6D(-14540, 0, 19000, 500)
    OP_44(0x101, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)
    Battle(0x3AF, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_953"),
        (SWITCH_DEFAULT, "loc_956"),
    )


    label("loc_953")

    OP_B4(0x0)
    Return()

    label("loc_956")

    EventBegin(0x0)
    OP_6D(-14300, 0, 17270, 0)
    SetChrPos(0x9, -10570, 0, 16410, 121)
    SetChrPos(0xA, -11440, 0, 14650, 198)
    SetChrPos(0xB, -11940, 0, 15850, 225)
    SetChrPos(0xC, -18230, 0, 18530, 225)
    SetChrPos(0xD, -19110, 0, 14890, 135)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, -14770, 0, 16800, 45)
    SetChrPos(0x108, -17220, 0, 15660, 350)
    SetChrPos(0x102, -15540, 0, 15160, 45)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -12550, -10, 19850, 225)

    ChrTalk(    #24
        0x101,
        (
            "#000FWhew...\x01",
            "Well, that's taken care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x108,
        (
            "#070FThey're too drunk to really\x01",
            "know what's going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#010FIt's like some kind of bar,\x01",
            "same as the one in the castle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        "P-Please...don't kill me...!\x02",
    )

    CloseMessageWindow()

    def lambda_AEF():
        OP_8F(0xFE, 0xFFFFD0EE, 0x0, 0x4F92, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AEF)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)

    def lambda_B19():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_B19)

    def lambda_B27():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B27)

    def lambda_B35():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B35)
    OP_6D(-12590, 0, 19790, 2000)

    def lambda_B54():

        label("loc_B54")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_B54")

    QueueWorkItem2(0x108, 1, lambda_B54)

    def lambda_B65():

        label("loc_B65")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_B65")

    QueueWorkItem2(0x101, 1, lambda_B65)

    def lambda_B76():

        label("loc_B76")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_B76")

    QueueWorkItem2(0x102, 1, lambda_B76)

    ChrTalk(    #28
        0x8,
        "I-I-I'm not with them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#000FWe know that. You work\x01",
            "at the villa, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#010FWe've come to help, at the request\x01",
            "of Her Majesty the Queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        "Wha... R-Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        "You're honestly here to save us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#000FYes, so would you calm down,\x01",
            "already?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C8D():
        OP_6D(-15830, 0, 17600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C8D)
    OP_8E(0x8, 0xFFFFCD7E, 0x0, 0x538E, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFC22A, 0x0, 0x51EA, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFC054, 0x0, 0x46BE, 0xBB8, 0x0)

    ChrTalk(    #34
        0x8,
        "Whew... Aidios be praised...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "I thought I was done for\x01",
            "when my reporter friend\x01",
            "was taken away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        "I hope he's all right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#000FReporter friend...?\x02\x03",

            "You must mean Nial!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        "...You know him?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #39
        "\x07\x05Estelle explained that Nial had gone missing and was still unaccounted for.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #40
        0x8,
        (
            "Ahh, I see. Yes, I'm the\x01",
            "one who contacted him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "He came to get an interview\x01",
            "with the princess, who is being\x01",
            "guarded here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "His passion for his work is hard to\x01",
            "argue with, so I wound up sneaking\x01",
            "him in and showing him the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x108,
        (
            "#070FBut he was spotted, and\x01",
            "taken prisoner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "Yes...and much to my shame, it\x01",
            "was only then that I realized\x01",
            "the severity of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "The princess was not being\x01",
            "guarded...but kept prisoner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "I was so glad that she was \x01",
            "coming that it simply had \x01",
            "never occurred to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#000FCome on...\x01",
            "No need to be so depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        (
            "#010FWould you happen to have any\x01",
            "idea where the prisoners are\x01",
            "being held?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "Yes... They've all been gathered\x01",
            "in the Crest Room, which is the\x01",
            "innermost chamber.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "It's a large banquet hall,\x01",
            "used for events like the\x01",
            "formal signing of treaties.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4C, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AC")

    ChrTalk(    #51
        0x101,
        "#000FGot it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x108,
        "#070FAll right, let's go check it out.\x02",
    )

    CloseMessageWindow()
    OP_28(0x4C, 0x1, 0x4)
    Jump("loc_1441")

    label("loc_11AC")

    OP_A2(0x679)
    OP_28(0x4C, 0x1, 0x10)

    ChrTalk(    #53
        0x101,
        (
            "#000FA big hall inside...\x01",
            "Maybe over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x108,
        (
            "#070FYes... the room behind the big,\x01",
            "ostentatious, LOCKED door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        "Ahh...so it is locked, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "The key is usually in the\x01",
            "possession of the Special\x01",
            "Ops commander...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "I believe he left when the\x01",
            "terrorists showed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#000FHuh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        (
            "#010FWhich means that it was taken\x01",
            "by the ones who ambushed Lt.\x01",
            "Schwarz and her men...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x108,
        (
            "#070FNot good.\x01",
            "There's no time to go back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        "Just a moment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "There's a spare key to that\x01",
            "door. It's here somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "If memory serves, I believe\x01",
            "it's hidden somewhere in the\x01",
            "Gallery...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#000FRoger that. Gallery!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        "#010FLet's hurry.\x02",
    )

    CloseMessageWindow()

    label("loc_1441")

    EventEnd(0x0)
    Return()

    # Function_3_67F end

    def Function_4_1444(): pass

    label("Function_4_1444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156B")
    EventBegin(0x0)
    OP_A2(0x657)
    OP_28(0x4C, 0x1, 0x20)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #66
        "\x07\x05There's an extravagant scarlet vase here.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #67
        "\x07\x05Estelle and company found something attached to its underside.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #68
        "\x07\x00Found \x07\x02Spare Key\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x36F, 1)

    ChrTalk(    #69
        0x101,
        "#000FThis is it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        (
            "#010FNow, we should be able to\x01",
            "open that inner door.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_1597")

    label("loc_156B")


    ChrTalk(    #71
        0x101,
        "#000F…いい仕事してる。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "（仮）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_1597")

    Return()

    # Function_4_1444 end

    def Function_5_1598(): pass

    label("Function_5_1598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_160F")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #73
        "\x07\x05○○○○○○○がある。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #74
        (
            "\x07\x05エステルたちが調べても\x01",
            "特に何も見つからなかった。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_1638")

    label("loc_160F")


    ChrTalk(    #75
        0x101,
        "#000F…いい仕事してる。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "（仮）\x02",
    )

    CloseMessageWindow()

    label("loc_1638")

    TalkEnd(0xFF)
    Return()

    # Function_5_1598 end

    def Function_6_163C(): pass

    label("Function_6_163C")

    EventBegin(0x0)
    OP_6D(11600, 0, -11080, 0)
    SetChrFlags(0x12, 0x80)
    SetChrPos(0xE, 11330, 0, -10500, 135)
    SetChrPos(0x11, 12980, 0, -9840, 233)
    SetChrPos(0x12, 9810, 700, -10140, 315)
    SetChrPos(0x101, 10700, 0, -11900, 66)
    SetChrPos(0x102, 11920, 0, -12750, 353)
    SetChrPos(0x108, 11030, 0, -13350, 31)
    SetChrPos(0x10, 13240, 0, -12800, 311)
    SetChrPos(0xF, 14330, 0, -11910, 252)
    TurnDirection(0xE, 0x11, 0)
    TurnDirection(0x12, 0x11, 0)
    TurnDirection(0x101, 0x11, 0)
    TurnDirection(0x102, 0x11, 0)
    TurnDirection(0x108, 0x11, 0)
    TurnDirection(0x10, 0x11, 0)
    TurnDirection(0xF, 0x11, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x108, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)

    ChrTalk(    #77
        0x11,
        (
            "#170FWords cannot express my shame.\x02\x03",

            "If not for my ineptitude, none of\x01",
            "this would have come to pass...\x02\x03",

            "I am so ashamed I could take my own life,\x01",
            "were it something to be permitted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xE,
        "Please do not say such things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xE,
        (
            "I'm just happy to see\x01",
            "you alive and unharmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xE,
        "Thank you for coming to save me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x11,
        "#170FYour Highness...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12, 400)

    ChrTalk(    #82
        0x101,
        (
            "#000FNot that I'm not moved by all\x01",
            "this, but I have to ask...\x02\x03",

            "Why is Sieg still here?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18F0():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_18F0)

    def lambda_18FE():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18FE)

    def lambda_190C():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_190C)

    def lambda_191A():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_191A)

    def lambda_1928():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1928)

    def lambda_1936():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1936)
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(    #83
        0x12,
        "Scree?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #84
        0x11,
        (
            "#170FHa ha. He is Her Highness's\x01",
            "escort, as well as a messenger\x01",
            "for the Royal Guardsmen.\x02\x03",

            "After all, did he not deliver\x01",
            "the letter to your hotel?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_19F5():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_19F5)

    def lambda_1A03():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A03)

    def lambda_1A11():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A11)

    def lambda_1A1F():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1A1F)

    def lambda_1A2D():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1A2D)

    def lambda_1A3B():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1A3B)

    ChrTalk(    #85
        0x101,
        "#000FOH! Th-That night!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x102,
        (
            "#010FI thought it might've been him.\x02\x03",

            "That must also be how you learned\x01",
            "of Her Majesty's request...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x11,
        (
            "#170FYes, I heard of it from Sieg.\x01",
            "Her Majesty sent word through\x01",
            "him from the Royal Keep.\x02\x03",

            "But the Crest Room in which Princess\x01",
            "Klaudia was held had no windows for\x01",
            "Sieg to use...\x02\x03",

            "I was very worried when I was\x01",
            "unable to make contact.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #88
        0xE,
        "Ha ha... Yes, I recall.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12, 400)

    ChrTalk(    #89
        0x101,
        (
            "#000FYou just about gave me a heart\x01",
            "attack, though, when you sent\x01",
            "that message to us.\x02\x03",

            "Sieg, that was just plain mean\x01",
            "of you to leave that letter and\x01",
            "not let us know it was you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x12,
        "Scree...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xE,
        (
            "#040FHa ha...\x01",
            "He says he's sorry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 400)

    ChrTalk(    #92
        0x101,
        (
            "#000FHa ha ha... It's okay.\x02\x03",

            "By the way, have all the Special\x01",
            "Ops troops been dealt with?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D3B():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D3B)

    ChrTalk(    #93
        0x11,
        (
            "#170FAlmost all of the soldiers in\x01",
            "the villa have been restrained.\x02\x03",

            "However, there are quite a\x01",
            "few left in Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1DC9():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1DC9)

    ChrTalk(    #94
        0x10,
        (
            "#020FMuch of the Royal Army is under \x01",
            "Intelligence Division control,\x01",
            "even outside of Grancel.\x02\x03",

            "If we're not careful, we run the risk of them\x01",
            "seizing control of this building and branding\x01",
            "us all as rebels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#000FWhoa... I hadn't even thought\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        (
            "#010FIndeed...\x02\x03",

            "I think it would be best if we were to get Kloe\x01",
            "to a safer location, at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xF,
        (
            "#030FPerhaps we could seek asylum at the Erebonian\x01",
            "or Republic embassies?\x02\x03",

            "Since they're considered foreign territory,\x01",
            "it would make it very difficult for them to\x01",
            "lay a hand on her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x108,
        (
            "#070FThere's also that Special Ops ship that we\x01",
            "seized nearby. We could use that to allow her\x01",
            "to flee the country for the time being.\x02\x03",

            "It wouldn't solve the whole problem, but it\x01",
            "would buy us some time to find a better\x01",
            "solution, at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x11,
        (
            "#170FI agree... Regardless, we need to find some way\x01",
            "to get her to safety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xE,
        "Umm...everyone...?\x02",
    )

    CloseMessageWindow()

    def lambda_217C():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_217C)

    def lambda_218A():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_218A)

    def lambda_2198():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2198)

    def lambda_21A6():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_21A6)

    def lambda_21B4():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_21B4)
    OP_8C(0xE, 135, 400)

    ChrTalk(    #103
        0xE,
        (
            "I understand the difficulties of the current\x01",
            "situation, but would it be possible to\x01",
            "make an official request of the bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#000FWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#010FThe hostages have been rescued,\x01",
            "so I think it'll be all right.\x02\x03",

            "Of course, it depends on what\x01",
            "the contents of the request are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xE,
        (
            "If so...I must ask you to\x01",
            "do the impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xE,
        (
            "Will you help in retaking the royal\x01",
            "castle and rescuing Her Majesty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x11,
        "#170FY-Your Highness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#000FI see... That's right.\x02\x03",

            "This time we have to help\x01",
            "the queen!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x108,
        (
            "#070FTo be honest, I consider the\x01",
            "question to be ridiculous,\x01",
            "because the answer is obvious.\x02\x03",

            "But, Your Highness...this is no\x01",
            "small thing you're asking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x10,
        (
            "#020FQuite right...\x02\x03",

            "There's no chance that a frontal\x01",
            "assault would work, even with the\x01",
            "capabilities of everyone here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#010FI think that captured Special\x01",
            "Ops ship has potential...\x02\x03",

            "But we're going to need some\x01",
            "kind of seriously clever trick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xE,
        "...I have an idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xE,
        "If everyone will please look at this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#000FHmm... What's this map of?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xE,
        (
            "It's an ancient diagram of the\x01",
            "sewers below Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xE,
        (
            "One of the things it lays out\x01",
            "is the path that leads to the\x01",
            "Castle Cellar.\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x357, 1)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_163C end

    SaveToFile()

Try(main)
