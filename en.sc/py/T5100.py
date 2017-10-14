from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T5100   ._SN',
        MapName             = 'Other',
        Location            = 'T5100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60025",
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
        'Anelace',                              # 9
        'Phyllis',                              # 10
        'Kurt',                                 # 11
        'Estelle',                              # 12
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
        'ED6_DT27/CH03090 ._CH',             # 00
        'ED6_DT27/CH03900 ._CH',             # 01
        'ED6_DT07/CH01620 ._CH',             # 02
        'ED6_DT27/CH04000 ._CH',             # 03
        'ED6_DT27/CH04001 ._CH',             # 04
        'ED6_DT27/CH04002 ._CH',             # 05
        'ED6_DT27/CH04008 ._CH',             # 06
        'ED6_DT27/CH04009 ._CH',             # 07
        'ED6_DT27/CH0400B ._CH',             # 08
        'ED6_DT07/CH00420 ._CH',             # 09
        'ED6_DT07/CH00421 ._CH',             # 0A
        'ED6_DT07/CH00422 ._CH',             # 0B
        'ED6_DT07/CH00423 ._CH',             # 0C
        'ED6_DT07/CH00424 ._CH',             # 0D
        'ED6_DT07/CH00425 ._CH',             # 0E
        'ED6_DT07/CH00426 ._CH',             # 0F
        'ED6_DT27/CH04007 ._CH',             # 10
        'ED6_DT27/CH0400A ._CH',             # 11
        'ED6_DT27/CH0400C ._CH',             # 12
        'ED6_DT27/CH03000 ._CH',             # 13
        'ED6_DT27/CH03001 ._CH',             # 14
        'ED6_DT27/CH03005 ._CH',             # 15
    )

    AddCharChipPat(
        'ED6_DT27/CH03090P._CP',             # 00
        'ED6_DT27/CH03900P._CP',             # 01
        'ED6_DT07/CH01620P._CP',             # 02
        'ED6_DT27/CH04000P._CP',             # 03
        'ED6_DT27/CH04001P._CP',             # 04
        'ED6_DT27/CH04002P._CP',             # 05
        'ED6_DT27/CH04008P._CP',             # 06
        'ED6_DT27/CH04009P._CP',             # 07
        'ED6_DT27/CH0400BP._CP',             # 08
        'ED6_DT07/CH00420P._CP',             # 09
        'ED6_DT07/CH00421P._CP',             # 0A
        'ED6_DT07/CH00422P._CP',             # 0B
        'ED6_DT07/CH00423P._CP',             # 0C
        'ED6_DT07/CH00424P._CP',             # 0D
        'ED6_DT07/CH00425P._CP',             # 0E
        'ED6_DT07/CH00426P._CP',             # 0F
        'ED6_DT27/CH04007P._CP',             # 10
        'ED6_DT27/CH0400AP._CP',             # 11
        'ED6_DT27/CH0400CP._CP',             # 12
        'ED6_DT27/CH03000P._CP',             # 13
        'ED6_DT27/CH03001P._CP',             # 14
        'ED6_DT27/CH03005P._CP',             # 15
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
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


    DeclEvent(
        X                   = -4320,
        Y                   = 0,
        Z                   = -36940,
        Range               = 3430,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF7338,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = -6800,
        Y                   = -200,
        Z                   = -51800,
        Range               = 700,
        Unknown_10          = 0x1CE8,
        Unknown_14          = 0xFFFF52F4,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )


    DeclActor(
        TriggerX            = -3550,
        TriggerZ            = 0,
        TriggerY            = -3000,
        TriggerRange        = 800,
        ActorX              = -4250,
        ActorZ              = 1000,
        ActorY              = -3000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_23E",          # 00, 0
        "Function_1_28F",          # 01, 1
        "Function_2_2EC",          # 02, 2
        "Function_3_393",          # 03, 3
        "Function_4_68F",          # 04, 4
        "Function_5_2172",         # 05, 5
        "Function_6_2338",         # 06, 6
        "Function_7_258E",         # 07, 7
        "Function_8_2AE9",         # 08, 8
        "Function_9_2B84",         # 09, 9
        "Function_10_2C2D",        # 0A, 10
        "Function_11_2CC4",        # 0B, 11
        "Function_12_2EB5",        # 0C, 12
        "Function_13_305F",        # 0D, 13
        "Function_14_3255",        # 0E, 14
        "Function_15_374F",        # 0F, 15
        "Function_16_3906",        # 10, 16
        "Function_17_3AD0",        # 11, 17
    )


    def Function_0_23E(): pass

    label("Function_0_23E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_260")
    SetChrPos(0xA, -2780, 0, -30790, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_275")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)

    label("loc_28E")

    Return()

    # Function_0_23E end

    def Function_1_28F(): pass

    label("Function_1_28F")

    OP_16(0x2, 0xFA0, 0xFFFE13D0, 0xFFFDE4F0, 0x23006F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_END)), "loc_2B6")
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C3, 0x0, 0x64)

    label("loc_2B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_2C0")
    OP_10(0x0, 0x0)

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 2)), scpexpr(EXPR_END)), "loc_2D0")
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_2D6")

    label("loc_2D0")

    OP_10(0x3, 0x0)
    OP_10(0x2, 0x1)

    label("loc_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_END)), "loc_2EB")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EB")

    Return()

    # Function_1_28F end

    def Function_2_2EC(): pass

    label("Function_2_2EC")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_31D"),
        (1, "loc_329"),
        (2, "loc_335"),
        (3, "loc_341"),
        (4, "loc_34D"),
        (5, "loc_359"),
        (6, "loc_365"),
        (SWITCH_DEFAULT, "loc_371"),
    )


    label("loc_31D")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_37D")

    label("loc_329")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_37D")

    label("loc_335")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_37D")

    label("loc_341")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_37D")

    label("loc_34D")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_37D")

    label("loc_359")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_37D")

    label("loc_365")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_37D")

    label("loc_371")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_37D")

    label("loc_37D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_392")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_37D")

    label("loc_392")

    Return()

    # Function_2_2EC end

    def Function_3_393(): pass

    label("Function_3_393")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 0)), scpexpr(EXPR_END)), "loc_3A4")
    Call(0, 10)
    Jump("loc_68B")

    label("loc_3A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC5, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_487")

    ChrTalk(    #0
        0xA,
        (
            "#842FI thought you two were going\x01",
            "to make sure you had adequate\x01",
            "provisions.\x02\x03",

            "If you go into a mission without\x01",
            "properly preparing beforehand,\x01",
            "you WILL get hurt.\x02\x03",

            "Make absolutely sure you speak\x01",
            "with Phyllis.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    label("loc_487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x261, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x258, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x25E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x26D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x2C1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x273, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x2C8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x26A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x2C1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4CE")
    OP_A2(0x1026)
    Jump("loc_57E")

    label("loc_4CE")


    ChrTalk(    #1
        0xA,
        (
            "#842FYou said yourself that you'll need\x01",
            "new quartz for those orbments.\x02\x03",

            "The exercise I have planned will\x01",
            "be too dangerous to undertake\x01",
            "without at least recovery arts.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    label("loc_57E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x6E)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_59F")
    OP_A2(0x1008)
    Call(0, 11)
    Jump("loc_68B")

    label("loc_59F")


    ChrTalk(    #2
        0xA,
        (
            "#843FGood, you've made some new quartz.\x02\x03",

            "#842FHowever, it's still far too dangerous for\x01",
            "you to take part in the training I have\x01",
            "planned without recovery arts.\x02\x03",

            "Make some quartz from water sepith\x01",
            "and equip them to your orbment.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    label("loc_68B")

    TalkEnd(0xA)
    Return()

    # Function_3_393 end

    def Function_4_68F(): pass

    label("Function_4_68F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_23(0x1C3)
    OP_BB(0x0, 0x0, 0x200032)
    OP_BB(0x0, 0x1, 0x0)
    OP_BD()
    LoadEffect(0x0, "Scraft\\sc000_00.eff")
    LoadEffect(0x1, "Scraft\\sc000_10.eff")
    LoadEffect(0x2, "Craft\\cr011_00.eff")
    LoadEffect(0x3, "monster\\ms10005.eff")
    LoadEffect(0x4, "map\\\\mp009_00.eff")
    OP_6D(7190, 0, 54070, 0)
    OP_67(0, 10560, -10000, 0)
    OP_6B(5770, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x40)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        "\x07\x05Two months later...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #4
        "\x07\x05Midwest Zemuria, Leman State\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #5
        "\x07\x05Le Locle Canyon, Bracer Training Grounds\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_DB()
    OP_43(0xA, 0x1, 0x0, 0x6)

    def lambda_801():
        OP_6D(4130, 0, 23930, 8000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_801)
    OP_C8(0x200, 0x46, "C_PLAC01._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)
    OP_22(0x1C3, 0x0, 0x64)
    WaitChrThread(0xA, 0x1)
    OP_1D(0x2C)
    Fade(1000)
    OP_6D(4120, 0, 24030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(305000, 0)
    OP_6E(262, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrPos(0xB, 510, 0, 22930, 90)
    SetChrPos(0x8, 7610, 0, 24760, 270)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0xB, 0x20)

    def lambda_8BA():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8BA)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)

    def lambda_8DC():
        OP_6D(200, 0, 23150, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8DC)

    def lambda_8F4():
        OP_6B(3200, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F4)

    def lambda_904():
        OP_67(0, 6800, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_904)

    def lambda_91C():
        OP_6E(224, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_91C)
    ClearChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 10)

    def lambda_936():
        OP_8E(0xFE, 0xB4A, 0x0, 0x5C94, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_936)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 15)
    SetChrChipByIndex(0xB, 8)

    def lambda_965():
        OP_8F(0xFE, 0x7B2, 0x0, 0x5C76, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_965)
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0xB, 0)
    Sleep(100)
    SetChrSubChip(0x8, 1)
    SetChrSubChip(0xB, 1)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    Sleep(200)
    SetChrSubChip(0x8, 0)
    Sleep(200)

    def lambda_9E7():
        OP_8F(0xFE, 0x5B4, 0x0, 0x5AF0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9E7)
    Sleep(50)

    def lambda_A07():
        OP_8F(0xFE, 0xFFFFFEF2, 0x0, 0x582A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A07)
    Sleep(50)
    SetChrSubChip(0x8, 1)
    SetChrSubChip(0xB, 0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    Sleep(200)
    SetChrSubChip(0x8, 0)
    Sleep(200)

    def lambda_A7F():
        OP_8F(0xFE, 0x30C, 0x0, 0x5A32, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A7F)

    def lambda_A9A():

        label("loc_A9A")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_A9A")

    QueueWorkItem2(0xB, 2, lambda_A9A)

    def lambda_AAB():
        OP_96(0xFE, 0xAC8, 0x0, 0x5014, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AAB)

    def lambda_AC9():
        OP_6D(4180, 0, 23500, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AC9)

    def lambda_AE1():
        OP_6C(206000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE1)
    SetChrSubChip(0x8, 0)
    Sleep(100)
    SetChrSubChip(0x8, 1)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_B0F():
        OP_96(0xFE, 0x18BA, 0x0, 0x5B4A, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B0F)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_44(0xB, 0x2)
    WaitChrThread(0x101, 0x0)

    def lambda_B40():
        OP_6D(1220, 0, 23560, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B40)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 5)

    def lambda_B62():
        OP_96(0xFE, 0x9C4, 0x0, 0x5ADC, 0x898, 0xFA0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B62)

    def lambda_B80():
        OP_99(0xFE, 0x5, 0x9, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_B80)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(200)
    SetChrChipByIndex(0x8, 9)

    def lambda_B9F():
        TurnDirection(0xFE, 0xB, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B9F)
    WaitChrThread(0xB, 0x1)
    OP_44(0xB, 0x2)
    SetChrChipByIndex(0x8, 14)
    SetChrSubChip(0x8, 0)
    PlayEffect(0x4, 0xFF, 0x8, 0, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_BFA():
        OP_8F(0xFE, 0xFFFFFAC4, 0x0, 0x5960, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BFA)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    def lambda_C24():
        OP_6D(2180, 0, 22700, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C24)

    def lambda_C3C():
        OP_6C(206000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C3C)

    def lambda_C4C():
        OP_6E(250, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C4C)
    SetChrChipByIndex(0xB, 8)
    SetChrSubChip(0xB, 0)

    def lambda_C66():
        OP_96(0xFE, 0x17F2, 0x0, 0x5C94, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C66)
    Sleep(200)
    SetChrChipByIndex(0x8, 9)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(200)

    def lambda_CAC():
        OP_6D(6330, 0, 23100, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CAC)

    def lambda_CC4():
        OP_67(0, 8100, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CC4)
    ClearChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 10)

    def lambda_CE6():
        OP_8E(0xFE, 0xCDA, 0x0, 0x5974, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CE6)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x20)

    def lambda_D0B():
        OP_6C(164000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D0B)

    def lambda_D1B():
        OP_96(0xFE, 0x1ACC, 0x0, 0x50AA, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D1B)

    def lambda_D39():

        label("loc_D39")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_D39")

    QueueWorkItem2(0x8, 2, lambda_D39)

    def lambda_D4A():
        OP_8C(0xFE, 184, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_D4A)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x2)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_D6B():
        OP_96(0xFE, 0x14C8, 0x0, 0x682E, 0x960, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D6B)
    OP_8C(0x8, 90, 800)
    OP_8C(0x8, 180, 800)
    OP_8C(0x8, 270, 800)
    OP_8C(0x8, 0, 800)
    OP_8C(0x8, 90, 800)
    OP_8C(0x8, 164, 800)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)

    def lambda_DC2():
        OP_6E(210, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_DC2)
    SetChrChipByIndex(0x8, 11)

    def lambda_DD7():
        OP_8F(0xFE, 0x175C, 0x0, 0x5F3C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DD7)

    def lambda_DF2():
        OP_99(0xFE, 0x0, 0x4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_DF2)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 16)
    SetChrSubChip(0xB, 11)

    def lambda_E11():
        OP_8F(0xFE, 0x15CC, 0x0, 0x5924, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E11)

    def lambda_E2C():
        OP_99(0xFE, 0xB, 0xC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_E2C)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    Sleep(400)
    SetChrFlags(0xB, 0x800)

    def lambda_E50():
        OP_6D(5340, 0, 24640, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E50)

    def lambda_E68():
        OP_67(0, 5980, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E68)

    def lambda_E80():
        OP_6C(158000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E80)

    def lambda_E90():
        OP_6E(258, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E90)
    ClearChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 5)
    TurnDirection(0xB, 0x8, 0)

    def lambda_EB1():
        OP_99(0xFE, 0x0, 0x9, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_EB1)
    Sleep(200)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 6)

    def lambda_ED0():
        OP_96(0xFE, 0x10D6, 0x0, 0x6BBC, 0x258, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_ED0)

    def lambda_EEE():

        label("loc_EEE")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_EEE")

    QueueWorkItem2(0x8, 2, lambda_EEE)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x2)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 0)
    Sleep(500)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 6)
    SetChrSubChip(0xB, 72)
    Sleep(100)

    def lambda_F3F():
        OP_6D(4620, 0, 27120, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F3F)

    def lambda_F57():
        OP_6C(182000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F57)

    def lambda_F67():
        OP_6E(280, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F67)

    def lambda_F77():
        OP_67(0, 5340, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F77)
    ClearChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 2)

    def lambda_F9E():
        OP_96(0xFE, 0x11B2, 0x0, 0x6B12, 0xBB8, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F9E)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(200)

    def lambda_FC6():
        OP_99(0xFE, 0x2, 0x9, 0x9C4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_FC6)
    OP_22(0x84, 0x0, 0x64)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 6)
    SetChrFlags(0x8, 0x4)

    def lambda_FEA():
        OP_96(0xFE, 0x1054, 0x80C, 0x7FBC, 0x9C4, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FEA)
    OP_22(0xA3, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1017():
        OP_96(0xFE, 0x1BEE, 0x0, 0x6EAA, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1017)

    def lambda_1035():

        label("loc_1035")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1035")

    QueueWorkItem2(0x8, 2, lambda_1035)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x2)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1054():
        OP_6D(4530, 0, 27250, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1054)

    def lambda_106C():
        OP_67(0, 6360, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_106C)

    def lambda_1084():
        OP_6E(256, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1084)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)

    def lambda_109E():
        OP_8F(0xFE, 0x1608, 0x0, 0x6D1A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_109E)
    Sleep(100)
    SetChrSubChip(0x8, 1)
    OP_22(0x84, 0x0, 0x64)
    SetChrChipByIndex(0xB, 8)
    SetChrSubChip(0xB, 0)
    OP_8C(0xB, 25, 0)

    def lambda_10D9():
        OP_8F(0xFE, 0xF82, 0x0, 0x68C4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_10D9)
    WaitChrThread(0xB, 0x1)
    Sleep(400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    def lambda_110D():
        OP_6D(3930, 0, 23850, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_110D)

    def lambda_1125():
        OP_6C(162000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1125)

    def lambda_1135():
        OP_67(0, 6360, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1135)

    def lambda_114D():
        OP_6E(280, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_114D)

    def lambda_115D():

        label("loc_115D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_115D")

    QueueWorkItem2(0xB, 2, lambda_115D)

    def lambda_116E():
        OP_96(0xFE, 0x398, 0x0, 0x63BA, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_116E)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)

    def lambda_119B():
        OP_96(0xFE, 0x6B8, 0x0, 0x56C2, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_119B)
    Sleep(100)
    SetChrChipByIndex(0x8, 9)

    def lambda_11C3():

        label("loc_11C3")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_11C3")

    QueueWorkItem2(0x8, 2, lambda_11C3)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_44(0xB, 0x2)
    OP_44(0x8, 0x2)
    SetChrChipByIndex(0xB, 3)
    ClearChrFlags(0xB, 0x800)
    SetChrChipByIndex(0xB, 17)
    Sleep(500)
    OP_DC()

    ChrTalk(    #6
        0xB,
        "#1006FHere I come, Anelace!\x02",
    )

    CloseMessageWindow()
    OP_99(0xB, 0x0, 0x4, 0x3E8)
    Sleep(500)

    ChrTalk(    #7
        0xB,
        "#1005F#4SBLAZIIIIING BAAAR-RAAAAAAGE!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 4)

    def lambda_1270():
        OP_8E(0xFE, 0x1054, 0x0, 0x625C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1270)
    WaitChrThread(0xB, 0x1)

    def lambda_1290():
        OP_6D(5450, 0, 26870, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1290)

    def lambda_12A8():
        OP_6C(130000, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12A8)

    def lambda_12B8():
        OP_6E(215, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12B8)

    def lambda_12C8():
        OP_67(0, 7460, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_12C8)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 18)
    SetChrSubChip(0xB, 1)

    def lambda_12F4():
        OP_8F(0xFE, 0x12A2, 0x0, 0x684C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12F4)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0x8, 14)
    SetChrChipByIndex(0xB, 7)
    SetChrSubChip(0xB, 0)

    def lambda_1323():
        OP_9E(0xFE, 0x1E, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1323)
    PlayEffect(0x0, 0x0, 0xB, 1000, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xB, 0x0, 0x3, 0x7D0)
    PlayEffect(0x0, 0x0, 0xB, 1000, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xB, 0x0, 0x3, 0x7D0)
    PlayEffect(0x0, 0x0, 0xB, 1000, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xB, 0x0, 0x3, 0x7D0)
    PlayEffect(0x0, 0x0, 0xB, 1000, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xB, 0x0, 0x3, 0x7D0)
    ClearChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 0)
    Sleep(100)

    def lambda_1449():
        OP_99(0xFE, 0x0, 0xC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1449)
    Sleep(400)
    PlayEffect(0x1, 0x1, 0xB, 1000, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1493():
        OP_6D(6410, 0, 28130, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1493)

    def lambda_14AB():
        OP_6C(156000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14AB)

    def lambda_14BB():
        OP_6E(226, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14BB)

    def lambda_14CB():
        OP_67(0, 6540, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_14CB)

    def lambda_14E3():
        OP_96(0xFE, 0x1ACC, 0x0, 0x7418, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14E3)
    WaitChrThread(0x8, 0x1)

    def lambda_1506():
        OP_96(0xFE, 0x1D4C, 0x0, 0x7710, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1506)
    WaitChrThread(0x8, 0x1)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)

    ChrTalk(    #8
        0x8,
        (
            "#814F#6PYow! That IS pretty hot!\x02\x03",

            "#816FBut...now it's MY turn!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    OP_8C(0x8, 293, 1000)
    OP_8C(0x8, 23, 1000)
    OP_8C(0x8, 113, 1000)
    OP_8C(0x8, 203, 1000)

    def lambda_15A3():
        OP_96(0xFE, 0xE56, 0x0, 0x646E, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_15A3)
    Sleep(500)

    ChrTalk(    #9
        0x8,
        "#815F#6P#4SEIIIGHT LEEEAF BLIIIIIIIITZ!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0xB, 8)
    SetChrSubChip(0xB, 1)
    Sleep(100)
    Fade(500)
    OP_6D(6130, 0, 28370, 0)
    OP_6C(68000, 0)

    def lambda_1641():
        OP_8E(0xFE, 0x1234, 0x0, 0x6824, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1641)

    def lambda_165C():
        OP_6D(4730, 0, 26490, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_165C)

    def lambda_1674():
        OP_6C(50000, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1674)
    WaitChrThread(0x8, 0x1)
    OP_43(0xA, 0x1, 0x0, 0x7)
    WaitChrThread(0xA, 0x1)
    OP_82(0x3, 0x0)

    ChrTalk(    #10
        0xB,
        "#2P#1021FGah...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "#815F#6POh, I'm not done YET!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 0)

    def lambda_16DB():
        OP_8E(0xFE, 0xF78, 0x0, 0x652C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_16DB)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 11)
    SetChrSubChip(0x8, 0)
    OP_43(0xA, 0x1, 0x0, 0x9)

    ChrTalk(    #12
        0xB,
        (
            "#2P#1003F(Ngh! Can't keep this up...)\x02\x03",

            "#1002F(So...!)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_82(0x3, 0x0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0xB, 17)
    SetChrSubChip(0xB, 7)
    OP_7D(0x0, 0xB, 0x32, 0x1F4)

    def lambda_1764():
        OP_8F(0xFE, 0x14E6, 0x0, 0x5FD2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1764)

    def lambda_177F():
        OP_99(0xFE, 0x7, 0xE, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_177F)

    def lambda_178F():
        OP_6D(4400, 0, 26560, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_178F)

    def lambda_17A7():
        OP_6C(0, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17A7)

    def lambda_17B7():
        OP_67(0, 6660, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_17B7)
    WaitChrThread(0xB, 0x2)
    SetChrChipByIndex(0xB, 8)
    SetChrSubChip(0xB, 1)
    TurnDirection(0xB, 0x8, 0)
    OP_7D(0x1, 0xB, 0x0, 0x0)

    ChrTalk(    #13 op#A
        0x8,
        "#814F#3P#10AWhat the--?!\x02",
    )

    Sleep(1000)
    OP_56(0x0)

    ChrTalk(    #14 op#A
        0xB,
        "#1005F#3S#10AYou're MINE!\x02",
    )

    Sleep(500)
    OP_56(0x0)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 0)

    def lambda_1840():
        OP_99(0xFE, 0x0, 0xC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1840)
    Sleep(400)
    TurnDirection(0x8, 0xB, 0)
    SetChrChipByIndex(0x8, 14)
    SetChrSubChip(0x8, 0)

    def lambda_1866():
        OP_8F(0xFE, 0xC1C, 0x0, 0x682E, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1866)

    def lambda_1881():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1881)
    PlayEffect(0x1, 0x1, 0x8, 500, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_20(0x5DC)

    ChrTalk(    #15 op#A
        0x8,
        "#1312F#3P#10AAieee!\x02",
    )

    Sleep(1000)
    OP_56(0x0)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x2)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 0)
    OP_99(0x8, 0x0, 0x3, 0x3E8)
    Sleep(500)

    ChrTalk(    #16
        0x8,
        "#1312F#3POwwwowowowwww...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    ClearChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 19)
    SetChrSubChip(0xB, 0)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0xB, 20)
    SetChrSubChip(0xB, 0)

    def lambda_1997():
        OP_6D(3820, 0, 27610, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1997)
    OP_92(0xB, 0x8, 0x5DC, 0xFA0, 0x0)
    OP_62(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0xB, 21)
    SetChrSubChip(0xB, 0)
    Sleep(500)

    ChrTalk(    #17
        0xB,
        (
            "#2P#1004FYikes, are you okay, Anelace?!\x01",
            "I didn't mean to hit THAT hard!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x19)
    Sleep(600)

    ChrTalk(    #18
        0x8,
        (
            "#819F#3PHaha... No, I'm okay. I blocked it...\x01",
            "uh, mostly...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Fade(500)
    SetChrChipByIndex(0xB, 19)
    SetChrSubChip(0xB, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #19
        0x8,
        (
            "#1316F#3PPhew! You sure got me good\x01",
            "with that one, though...\x02\x03",

            "#1314FGuess I can't rely on that one move\x01",
            "as my 'win button' anymore, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        (
            "#4P#1016FHeheh... It was just luck, really.\x02\x03",

            "#1006FBesides, I gotta give back a LITTLE\x01",
            "of what I've been taking!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#816F#3PYou've really been throwing yourself\x01",
            "into this, Estelle.\x02\x03",

            "#1310FIf you've got enough energy left for\x01",
            "smack talk, let's do one more set!\x01",
            "C'mon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        "#4P#1006FYou're on!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, 3820, 0, 12520, 0)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #23
        0x9,
        "Woman's Voice",
        (
            "#5PWell, you two certainly have a\x01",
            "lot of energy this morning!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_6D(4150, 0, 23370, 0)
    OP_67(0, 7660, -10000, 0)
    OP_6B(3090, 0)
    OP_6C(122000, 0)
    OP_6E(270, 0)

    def lambda_1D28():
        OP_8E(0x9, 0xEEC, 0x0, 0x5672, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D28)
    Sleep(100)
    TurnDirection(0xB, 0x9, 400)
    Sleep(100)
    TurnDirection(0x8, 0x9, 400)
    Sleep(200)
    Sleep(1000)

    ChrTalk(    #24
        0x8,
        "#811F#1POh, Phyllis! G'morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xB,
        "#1018F#6PMorning, Phyllis!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #26
        0x9,
        (
            "#4PGood morning, Estelle, Anelace.\x02\x03",

            "I WAS going to call you two\x01",
            "to breakfast, but...\x02\x03",

            "I suppose you'd rather beat the\x01",
            "stuffing out of each other instead\x01",
            "of getting stuffed, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        "#1004F#6POh, breakfast! Right!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 400)
    Sleep(300)

    ChrTalk(    #28
        0xB,
        (
            "#1015F#5PWhat do you think, Anelace?\x01",
            "Beat stuffing, or get stuffing?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 400)
    Sleep(300)

    ChrTalk(    #29
        0x8,
        (
            "#817F#1PHmmm...\x01",
            "That IS a choice, isn't it?\x02\x03",

            "#810FWe'd be wasting a perfectly good\x01",
            "breakfast if we didn't eat, so...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F66():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1F66)
    Sleep(50)

    def lambda_1F79():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1F79)
    Sleep(300)

    ChrTalk(    #30
        0x8,
        (
            "#1310F#1PPhyllis, you wouldn't happen to\x01",
            "know where Kurt is, would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "#4PKurt said he had to prepare some things\x01",
            "for today's training, so he went on ahead.\x02\x03",

            "He made it sound like he had some pretty\x01",
            "hard things lined up for you two today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        "#1019F#6POh, great...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        "#1317F#1PH-He really said that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "#4PMm-hmm! And he told me to make\x01",
            "sure you both ate a good breakfast.\x02\x03",

            "Come in and eat, you two. Something\x01",
            "tells me you'll be wanting it later!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x1C3)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T5110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_68F end

    def Function_5_2172(): pass

    label("Function_5_2172")

    SetChrPos(0xB, 510, 0, 22930, 90)
    SetChrPos(0x8, 7610, 0, 24760, 270)

    def lambda_219A():
        OP_8E(0xFE, 0x104A, 0x0, 0x5CBC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_219A)
    Sleep(300)

    def lambda_21BA():
        OP_8E(0xFE, 0x15CC, 0x0, 0x5C80, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_21BA)
    Sleep(300)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 5)

    def lambda_21E9():
        OP_99(0xFE, 0x5, 0xC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_21E9)
    WaitChrThread(0x8, 0x1)

    def lambda_21FE():
        OP_96(0xFE, 0x13BA, 0x0, 0x532A, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_21FE)
    Sleep(200)

    def lambda_2221():
        TurnDirection(0x8, 0xB, 0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2221)
    Sleep(200)
    OP_44(0xB, 0x0)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    TurnDirection(0x8, 0xB, 1000)

    def lambda_2249():
        OP_8E(0xFE, 0x10FE, 0x0, 0x5AAA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2249)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)

    def lambda_2273():
        OP_96(0xFE, 0x10B8, 0x0, 0x6504, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2273)
    SetChrSubChip(0x8, 1)
    WaitChrThread(0xB, 0x0)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 0)

    def lambda_22A5():
        OP_8F(0xFE, 0x1054, 0x0, 0x5F14, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22A5)
    WaitChrThread(0x8, 0x1)

    def lambda_22C5():
        OP_8F(0xFE, 0xF78, 0x0, 0x6C66, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_22C5)
    TurnDirection(0x8, 0xB, 1000)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 1)
    Sleep(200)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 0)

    def lambda_2300():
        OP_8F(0xFE, 0x102C, 0x0, 0x5D8E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2300)
    SetChrPos(0xB, 3960, 0, 27750, 180)
    SetChrPos(0x8, 4140, 0, 23950, 0)
    Return()

    # Function_5_2172 end

    def Function_6_2338(): pass

    label("Function_6_2338")

    SetChrPos(0xB, 3900, 0, 23500, 180)
    SetChrPos(0x8, 3900, 0, 20400, 0)
    Sleep(200)
    OP_22(0xD6, 0x0, 0x14)
    Sleep(300)
    OP_22(0xD6, 0x0, 0x14)
    Sleep(1000)
    OP_22(0x84, 0x0, 0x28)
    Sleep(300)
    OP_22(0x84, 0x0, 0x28)
    Sleep(300)
    OP_22(0xD6, 0x0, 0x28)
    SetChrChipByIndex(0xB, 8)
    SetChrSubChip(0xB, 0)
    SetChrFlags(0xB, 0x20)

    def lambda_23A1():
        OP_8F(0xFE, 0xF3C, 0x0, 0x6950, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_23A1)
    WaitChrThread(0xB, 0x1)
    Sleep(200)
    ClearChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 4)
    SetChrSubChip(0xB, 0)

    def lambda_23D5():
        OP_8E(0xFE, 0xF3C, 0x0, 0x5A8C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_23D5)
    Sleep(200)

    def lambda_23F5():
        OP_96(0xFE, 0xF3C, 0x0, 0x613A, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23F5)
    OP_22(0xA3, 0x0, 0x3C)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 5)

    def lambda_242C():
        OP_8F(0xFE, 0xF3C, 0x0, 0x5550, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_242C)

    def lambda_2447():
        OP_99(0xFE, 0x5, 0x9, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2447)
    OP_22(0x84, 0x0, 0x3C)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x3C)

    def lambda_2466():
        OP_96(0xFE, 0xF3C, 0x0, 0x6950, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2466)

    def lambda_2484():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2484)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x3C)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 0)
    OP_22(0xA3, 0x0, 0x3C)

    def lambda_24AB():
        OP_96(0xFE, 0xF3C, 0x0, 0x6306, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_24AB)

    def lambda_24C9():
        OP_99(0xFE, 0x0, 0x9, 0x9C4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_24C9)

    def lambda_24D9():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_24D9)
    Sleep(300)

    def lambda_24EC():
        OP_96(0xFE, 0x1DBA, 0x0, 0x60B8, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_24EC)

    def lambda_250A():

        label("loc_250A")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_250A")

    QueueWorkItem2(0x8, 2, lambda_250A)
    Sleep(100)
    OP_22(0x84, 0x0, 0x50)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x50)
    Sleep(400)
    SetChrChipByIndex(0xB, 8)
    SetChrSubChip(0xB, 0)

    def lambda_253E():
        OP_96(0xFE, 0x1FE, 0x0, 0x5992, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_253E)

    def lambda_255C():

        label("loc_255C")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_255C")

    QueueWorkItem2(0xB, 2, lambda_255C)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x50)
    OP_44(0x8, 0x2)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x50)
    OP_44(0xB, 0x2)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    Return()

    # Function_6_2338 end

    def Function_7_258E(): pass

    label("Function_7_258E")

    SetChrChipByIndex(0x8, 11)
    SetChrSubChip(0x8, 0)
    OP_99(0x8, 0x0, 0x7, 0xFA0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_25E1():
        OP_9E(0xFE, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_25E1)
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2630():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2630)

    def lambda_264B():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_264B)
    OP_99(0x8, 0x0, 0x7, 0xFA0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_26DE():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_26DE)

    def lambda_26F9():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_26F9)
    OP_99(0x8, 0x0, 0x7, 0xFA0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_278C():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_278C)

    def lambda_27A7():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27A7)
    OP_99(0x8, 0x0, 0x7, 0xFA0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_283A():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_283A)

    def lambda_2855():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2855)
    OP_99(0x8, 0x0, 0x7, 0xFA0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_28E8():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_28E8)

    def lambda_2903():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2903)
    OP_99(0x8, 0x0, 0x7, 0xFA0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2996():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2996)

    def lambda_29B1():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29B1)
    SetChrSubChip(0x8, 0)

    def lambda_29D1():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0xBB8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_29D1)
    Sleep(500)

    def lambda_29F4():
        OP_99(0x8, 0x0, 0x5, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_29F4)

    def lambda_2A04():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2A04)
    Sleep(300)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0x12C, 0x64)
    WaitChrThread(0x8, 0x0)
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2AA9():
        OP_96(0xFE, 0x1928, 0x0, 0x6F68, 0x9C4, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2AA9)
    OP_43(0xA, 0x2, 0x0, 0x8)
    WaitChrThread(0xA, 0x2)
    WaitChrThread(0x8, 0x3)
    OP_22(0xA4, 0x0, 0x64)
    TurnDirection(0x8, 0xB, 1000)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 0)
    Return()

    # Function_7_258E end

    def Function_8_2AE9(): pass

    label("Function_8_2AE9")

    OP_8C(0x8, 0, 2000)
    OP_8C(0x8, 45, 2000)
    OP_8C(0x8, 90, 2000)
    OP_8C(0x8, 135, 2000)
    OP_8C(0x8, 180, 2000)
    OP_8C(0x8, 225, 2000)
    OP_8C(0x8, 270, 2000)
    OP_8C(0x8, 315, 2000)
    OP_8C(0x8, 0, 2000)
    OP_8C(0x8, 45, 2000)
    OP_8C(0x8, 90, 2000)
    OP_8C(0x8, 135, 2000)
    OP_8C(0x8, 180, 2000)
    OP_8C(0x8, 225, 2000)
    OP_8C(0x8, 270, 2000)
    OP_8C(0x8, 315, 2000)
    OP_8C(0x8, 0, 2000)
    OP_8C(0x8, 45, 2000)
    OP_8C(0x8, 90, 2000)
    OP_8C(0x8, 135, 2000)
    OP_8C(0x8, 180, 2000)
    OP_8C(0x8, 203, 2000)
    Return()

    # Function_8_2AE9 end

    def Function_9_2B84(): pass

    label("Function_9_2B84")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C2C")
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x8, 0x0, 0x7, 0xFA0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_2C0B():
        OP_9E(0xB, 0x1E, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2C0B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2C29")
    Jump("loc_2C2C")

    label("loc_2C29")

    Jump("Function_9_2B84")

    label("loc_2C2C")

    Return()

    # Function_9_2B84 end

    def Function_10_2C2D(): pass

    label("Function_10_2C2D")

    EventBegin(0x0)
    Fade(1000)
    OP_8C(0xA, 0, 0)
    SetChrSubChip(0xA, 0)
    SetChrPos(0x101, -3720, 0, -28700, 180)
    SetChrPos(0x10A, -2700, 0, -28850, 180)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(    #35
        0xA,
        "#840F#6PAre you two prepared?\x02",
    )

    CloseMessageWindow()
    Call(0, 12)
    Return()

    # Function_10_2C2D end

    def Function_11_2CC4(): pass

    label("Function_11_2CC4")

    EventBegin(0x0)
    Fade(1000)
    OP_8C(0xA, 0, 0)
    SetChrSubChip(0xA, 0)
    SetChrPos(0x101, -3720, 0, -28700, 180)
    SetChrPos(0x10A, -2700, 0, -28850, 180)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(500)

    ChrTalk(    #36
        0xA,
        (
            "#840F#6PSo you've had your new quartz\x01",
            "manufactured and prepared healing arts?\x02\x03",

            "Very good. Now we can set off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1007F#6PFinally...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10A,
        (
            "#818FSo we're heading for that\x01",
            "sewer-like thingy in the western\x01",
            "part of the canyon, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xA,
        (
            "#843F#6PIndeed, the Balstar Channel.\x02\x03",

            "#842FAs I said before, the monsters\x01",
            "within are dangerous.\x02\x03",

            "Are you two prepared?\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC5, 0x1, 0x40)
    OP_28(0xC5, 0x4, 0x10)
    OP_28(0xC5, 0x4, 0x20)
    Call(0, 12)
    Return()

    # Function_11_2CC4 end

    def Function_12_2EB5(): pass

    label("Function_12_2EB5")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "We're Ready\x01",                 # 0
            "Sweet Goddess, Not Yet\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F5B")

    ChrTalk(    #40
        0xA,
        (
            "#840F#6PVery well.\x01",
            "Make whatever preparations you need.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_2F5B")


    ChrTalk(    #41
        0xA,
        (
            "#840F#6PVery well! Let's get going.\x02\x03",

            "Follow me, you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#1018F#6POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10A,
        "#1310FRight behind you, boss!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x40)
    OP_8C(0xA, 180, 500)

    def lambda_2FE2():
        OP_8E(0xA, 0xFFFFF484, 0x0, 0xFFFF5FC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2FE2)
    Sleep(300)

    def lambda_3002():
        OP_8E(0x10A, 0xFFFFF484, 0x0, 0xFFFF5FC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3002)
    Sleep(500)

    def lambda_3022():
        OP_8E(0x101, 0xFFFFF484, 0x0, 0xFFFF5FC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3022)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    ClearChrFlags(0x101, 0x40)
    Call(0, 13)
    NewScene("ED6_DT21/C5503   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2EB5 end

    def Function_13_305F(): pass

    label("Function_13_305F")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS137._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_320B")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",          # 0
            "[Balstar Channel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3121"),
        (1, "loc_318B"),
        (SWITCH_DEFAULT, "loc_3208"),
    )


    label("loc_3121")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Kurt")

    AnonymousTalk(    #44
        (
            "\x07\x00#840FOur destination is the Balstar Channel\x01",
            "in the west.\x02\x03",

            "Lead the way, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_3208")

    label("loc_318B")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #45
        "\x07\x05Move to [Balstar Channel]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31F5"),
        (1, "loc_3202"),
        (SWITCH_DEFAULT, "loc_3205"),
    )


    label("loc_31F5")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3205")

    label("loc_3202")

    Jump("loc_3205")

    label("loc_3205")

    Jump("loc_3208")

    label("loc_3208")

    Jump("loc_30C0")

    label("loc_320B")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_13_305F end

    def Function_14_3255(): pass

    label("Function_14_3255")

    ClearMapFlags(0x2000000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_3278")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3289")

    label("loc_3278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 2)), scpexpr(EXPR_END)), "loc_3289")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3289")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS137._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3607")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3325"),
        (1, "loc_3351"),
        (2, "loc_3392"),
        (SWITCH_DEFAULT, "loc_33E6"),
    )


    label("loc_3325")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",          # 0
            "[Balstar Channel]\x01",      # 1
        )
    )

    Jump("loc_33E6")

    label("loc_3351")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",             # 0
            "[Balstar Channel]\x01",         # 1
            "[Saint-Croix Forest]\x01",      # 2
        )
    )

    Jump("loc_33E6")

    label("loc_3392")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",             # 0
            "[Balstar Channel]\x01",         # 1
            "[Saint-Croix Forest]\x01",      # 2
            "[Grimsel Fortress]\x01",        # 3
        )
    )

    Jump("loc_33E6")

    label("loc_33E6")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3410"),
        (1, "loc_3489"),
        (2, "loc_3506"),
        (3, "loc_3586"),
        (SWITCH_DEFAULT, "loc_3604"),
    )


    label("loc_3410")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #46
        "\x07\x05Move to [Guild Lodge]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3476"),
        (1, "loc_3483"),
        (SWITCH_DEFAULT, "loc_3486"),
    )


    label("loc_3476")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3486")

    label("loc_3483")

    Jump("loc_3486")

    label("loc_3486")

    Jump("loc_3604")

    label("loc_3489")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #47
        "\x07\x05Move to [Balstar Channel]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_34F3"),
        (1, "loc_3500"),
        (SWITCH_DEFAULT, "loc_3503"),
    )


    label("loc_34F3")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3503")

    label("loc_3500")

    Jump("loc_3503")

    label("loc_3503")

    Jump("loc_3604")

    label("loc_3506")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #48
        "\x07\x05Move to [Saint-Croix Forest]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3573"),
        (1, "loc_3580"),
        (SWITCH_DEFAULT, "loc_3583"),
    )


    label("loc_3573")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3583")

    label("loc_3580")

    Jump("loc_3583")

    label("loc_3583")

    Jump("loc_3604")

    label("loc_3586")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #49
        "\x07\x05Move to [Grimsel Fortress]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_35F1"),
        (1, "loc_35FE"),
        (SWITCH_DEFAULT, "loc_3601"),
    )


    label("loc_35F1")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3601")

    label("loc_35FE")

    Jump("loc_3601")

    label("loc_3601")

    Jump("loc_3604")

    label("loc_3604")

    Jump("loc_32FA")

    label("loc_3607")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3620"),
        (1, "loc_3654"),
        (2, "loc_3688"),
        (3, "loc_36BC"),
        (SWITCH_DEFAULT, "loc_36F0"),
    )


    label("loc_3620")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_36F0")

    label("loc_3654")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_36F0")

    label("loc_3688")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_36F0")

    label("loc_36BC")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_36F0")

    label("loc_36F0")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3712"),
        (1, "loc_372A"),
        (2, "loc_3736"),
        (3, "loc_3742"),
        (SWITCH_DEFAULT, "loc_374E"),
    )


    label("loc_3712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_END)), "loc_371E")
    SetMapFlags(0x2000000)

    label("loc_371E")

    NewScene("ED6_DT21/T5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_374E")

    label("loc_372A")

    NewScene("ED6_DT21/C5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_374E")

    label("loc_3736")

    NewScene("ED6_DT21/C5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_374E")

    label("loc_3742")

    NewScene("ED6_DT21/C5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_374E")

    label("loc_374E")

    Return()

    # Function_14_3255 end

    def Function_15_374F(): pass

    label("Function_15_374F")

    EventBegin(0x0)
    SetChrPos(0x101, -4030, 0, -16260, 4)
    SetChrPos(0x10A, -3010, 0, -16920, 0)
    OP_6D(-4570, 0, 10280, 0)
    OP_67(0, 7680, -10000, 0)
    OP_6B(4880, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)

    def lambda_37BF():
        OP_6D(-3880, 0, -13000, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_37BF)
    WaitChrThread(0x10A, 0x0)
    Fade(1000)
    OP_6D(-4570, 0, -16000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #50
        0x101,
        (
            "#6P#1002FWell, from the outside,\x01",
            "it looks like nobody's here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10A,
        (
            "#2P#812FYeah... Should be safe to nose\x01",
            "around inside.\x02\x03",

            "There might be traps or something,\x01",
            "though, so let's be careful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#6P#1002FGot it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x101B)
    OP_28(0x80, 0x1, 0x1)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_15_374F end

    def Function_16_3906(): pass

    label("Function_16_3906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3997")
    EventBegin(0x1)
    OP_4A(0xA, 255)
    TurnDirection(0xA, 0x0, 400)

    ChrTalk(    #53
        0xA,
        (
            "#843FAre you two prepared?\x02\x03",

            "#840FLet me know once you're\x01",
            "ready to depart.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    OP_8C(0xA, 0, 0)
    OP_4B(0xA, 255)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_3ACF")

    label("loc_3997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A5B")
    EventBegin(0x1)

    ChrTalk(    #54
        0x101,
        (
            "#1015FI sorta feel like training\x01",
            "will start without me while\x01",
            "I'm wasting time...\x02\x03",

            "Might be a good idea to\x01",
            "head back to my room\x01",
            "and check my equipment.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_3ACF")

    label("loc_3A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ACF")
    EventBegin(0x1)

    ChrTalk(    #55
        0x101,
        (
            "#1015FI don't want to keep Kurt\x01",
            "waiting!\x02\x03",

            "I should head for the entrance.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3ACF")

    Return()

    # Function_16_3906 end

    def Function_17_3AD0(): pass

    label("Function_17_3AD0")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #56
        "\x07\x05Bracer Guild [Le Locle Training Grounds]\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_3AD0 end

    SaveToFile()

Try(main)
