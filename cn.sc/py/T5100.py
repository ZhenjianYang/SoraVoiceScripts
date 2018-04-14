from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '亚妮拉丝',                             # 9
        '菲莉斯管理员',                         # 10
        '克鲁茨',                               # 11
        '艾丝蒂尔',                             # 12
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
        "Function_4_5A1",          # 04, 4
        "Function_5_1DE3",         # 05, 5
        "Function_6_1FA9",         # 06, 6
        "Function_7_21FF",         # 07, 7
        "Function_8_275A",         # 08, 8
        "Function_9_27F5",         # 09, 9
        "Function_10_289E",        # 0A, 10
        "Function_11_2932",        # 0B, 11
        "Function_12_2AC1",        # 0C, 12
        "Function_13_2C3F",        # 0D, 13
        "Function_14_2E0F",        # 0E, 14
        "Function_15_3319",        # 0F, 15
        "Function_16_3494",        # 10, 16
        "Function_17_35F7",        # 11, 17
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
    Jump("loc_59D")

    label("loc_3A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC5, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F")

    ChrTalk(    #0
        0xA,
        (
            "#842F你们两个，食物准备得如何了？\x02\x03",

            "长时间的作战行动中\x01",
            "要是小看补给可会吃苦头的哦。\x02\x03",

            "好好去向菲莉斯管理员\x01",
            "请教一下吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x261, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x258, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x25E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x26D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x2C1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x273, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x2C8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x26A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x2C1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_476")
    OP_A2(0x1026)
    Jump("loc_4D5")

    label("loc_476")


    ChrTalk(    #1
        0xA,
        (
            "#842F不合成新型\x01",
            "结晶回路没问题吗？\x02\x03",

            "若不能使用回复系的魔法，\x01",
            "参加演习是相当危险的哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    label("loc_4D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x6E)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F6")
    OP_A2(0x1008)
    Call(0, 11)
    Jump("loc_59D")

    label("loc_4F6")


    ChrTalk(    #2
        0xA,
        (
            "#843F你们似乎合成了\x01",
            "一些新型结晶回路啊。\x02\x03",

            "#842F但是，若不能使用回复系的魔法，\x01",
            "参加演习是相当危险的哦。\x02\x03",

            "用水之耀晶片合成结晶回路，\x01",
            "然后镶嵌到导力器上就好了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    label("loc_59D")

    TalkEnd(0xA)
    Return()

    # Function_3_393 end

    def Function_4_5A1(): pass

    label("Function_4_5A1")

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
        "\x07\x05２个月后──\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #4
        (
            "\x07\x05塞姆里亚大陆中西部\x01",
            "列曼自治州·峡谷地带──\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #5
        (
            "\x07\x05游击士协会\x01",
            "卢·洛克尔训练场──\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0xA, 0x1, 0x0, 0x6)

    def lambda_711():
        OP_6D(4130, 0, 23930, 8000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_711)
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

    def lambda_7CA():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7CA)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)

    def lambda_7EC():
        OP_6D(200, 0, 23150, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7EC)

    def lambda_804():
        OP_6B(3200, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_804)

    def lambda_814():
        OP_67(0, 6800, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_814)

    def lambda_82C():
        OP_6E(224, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_82C)
    ClearChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 10)

    def lambda_846():
        OP_8E(0xFE, 0xB4A, 0x0, 0x5C94, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_846)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 15)
    SetChrChipByIndex(0xB, 8)

    def lambda_875():
        OP_8F(0xFE, 0x7B2, 0x0, 0x5C76, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_875)
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

    def lambda_8F7():
        OP_8F(0xFE, 0x5B4, 0x0, 0x5AF0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8F7)
    Sleep(50)

    def lambda_917():
        OP_8F(0xFE, 0xFFFFFEF2, 0x0, 0x582A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_917)
    Sleep(50)
    SetChrSubChip(0x8, 1)
    SetChrSubChip(0xB, 0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    Sleep(200)
    SetChrSubChip(0x8, 0)
    Sleep(200)

    def lambda_98F():
        OP_8F(0xFE, 0x30C, 0x0, 0x5A32, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_98F)

    def lambda_9AA():

        label("loc_9AA")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_9AA")

    QueueWorkItem2(0xB, 2, lambda_9AA)

    def lambda_9BB():
        OP_96(0xFE, 0xAC8, 0x0, 0x5014, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9BB)

    def lambda_9D9():
        OP_6D(4180, 0, 23500, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9D9)

    def lambda_9F1():
        OP_6C(206000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F1)
    SetChrSubChip(0x8, 0)
    Sleep(100)
    SetChrSubChip(0x8, 1)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_A1F():
        OP_96(0xFE, 0x18BA, 0x0, 0x5B4A, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A1F)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_44(0xB, 0x2)
    WaitChrThread(0x101, 0x0)

    def lambda_A50():
        OP_6D(1220, 0, 23560, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A50)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 5)

    def lambda_A72():
        OP_96(0xFE, 0x9C4, 0x0, 0x5ADC, 0x898, 0xFA0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A72)

    def lambda_A90():
        OP_99(0xFE, 0x5, 0x9, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_A90)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(200)
    SetChrChipByIndex(0x8, 9)

    def lambda_AAF():
        TurnDirection(0xFE, 0xB, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AAF)
    WaitChrThread(0xB, 0x1)
    OP_44(0xB, 0x2)
    SetChrChipByIndex(0x8, 14)
    SetChrSubChip(0x8, 0)
    PlayEffect(0x4, 0xFF, 0x8, 0, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_B0A():
        OP_8F(0xFE, 0xFFFFFAC4, 0x0, 0x5960, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B0A)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    def lambda_B34():
        OP_6D(2180, 0, 22700, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B34)

    def lambda_B4C():
        OP_6C(206000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B4C)

    def lambda_B5C():
        OP_6E(250, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B5C)
    SetChrChipByIndex(0xB, 8)
    SetChrSubChip(0xB, 0)

    def lambda_B76():
        OP_96(0xFE, 0x17F2, 0x0, 0x5C94, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B76)
    Sleep(200)
    SetChrChipByIndex(0x8, 9)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(200)

    def lambda_BBC():
        OP_6D(6330, 0, 23100, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BBC)

    def lambda_BD4():
        OP_67(0, 8100, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BD4)
    ClearChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 10)

    def lambda_BF6():
        OP_8E(0xFE, 0xCDA, 0x0, 0x5974, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BF6)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x20)

    def lambda_C1B():
        OP_6C(164000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C1B)

    def lambda_C2B():
        OP_96(0xFE, 0x1ACC, 0x0, 0x50AA, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C2B)

    def lambda_C49():

        label("loc_C49")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_C49")

    QueueWorkItem2(0x8, 2, lambda_C49)

    def lambda_C5A():
        OP_8C(0xFE, 184, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_C5A)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x2)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_C7B():
        OP_96(0xFE, 0x14C8, 0x0, 0x682E, 0x960, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C7B)
    OP_8C(0x8, 90, 800)
    OP_8C(0x8, 180, 800)
    OP_8C(0x8, 270, 800)
    OP_8C(0x8, 0, 800)
    OP_8C(0x8, 90, 800)
    OP_8C(0x8, 164, 800)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)

    def lambda_CD2():
        OP_6E(210, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_CD2)
    SetChrChipByIndex(0x8, 11)

    def lambda_CE7():
        OP_8F(0xFE, 0x175C, 0x0, 0x5F3C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CE7)

    def lambda_D02():
        OP_99(0xFE, 0x0, 0x4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D02)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 16)
    SetChrSubChip(0xB, 11)

    def lambda_D21():
        OP_8F(0xFE, 0x15CC, 0x0, 0x5924, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D21)

    def lambda_D3C():
        OP_99(0xFE, 0xB, 0xC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_D3C)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    Sleep(400)
    SetChrFlags(0xB, 0x800)

    def lambda_D60():
        OP_6D(5340, 0, 24640, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D60)

    def lambda_D78():
        OP_67(0, 5980, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D78)

    def lambda_D90():
        OP_6C(158000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D90)

    def lambda_DA0():
        OP_6E(258, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_DA0)
    ClearChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 5)
    TurnDirection(0xB, 0x8, 0)

    def lambda_DC1():
        OP_99(0xFE, 0x0, 0x9, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_DC1)
    Sleep(200)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 6)

    def lambda_DE0():
        OP_96(0xFE, 0x10D6, 0x0, 0x6BBC, 0x258, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DE0)

    def lambda_DFE():

        label("loc_DFE")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_DFE")

    QueueWorkItem2(0x8, 2, lambda_DFE)
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

    def lambda_E4F():
        OP_6D(4620, 0, 27120, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E4F)

    def lambda_E67():
        OP_6C(182000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E67)

    def lambda_E77():
        OP_6E(280, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E77)

    def lambda_E87():
        OP_67(0, 5340, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E87)
    ClearChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 2)

    def lambda_EAE():
        OP_96(0xFE, 0x11B2, 0x0, 0x6B12, 0xBB8, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_EAE)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(200)

    def lambda_ED6():
        OP_99(0xFE, 0x2, 0x9, 0x9C4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_ED6)
    OP_22(0x84, 0x0, 0x64)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 6)
    SetChrFlags(0x8, 0x4)

    def lambda_EFA():
        OP_96(0xFE, 0x1054, 0x80C, 0x7FBC, 0x9C4, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EFA)
    OP_22(0xA3, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_F27():
        OP_96(0xFE, 0x1BEE, 0x0, 0x6EAA, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F27)

    def lambda_F45():

        label("loc_F45")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_F45")

    QueueWorkItem2(0x8, 2, lambda_F45)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x2)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_F64():
        OP_6D(4530, 0, 27250, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F64)

    def lambda_F7C():
        OP_67(0, 6360, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F7C)

    def lambda_F94():
        OP_6E(256, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F94)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)

    def lambda_FAE():
        OP_8F(0xFE, 0x1608, 0x0, 0x6D1A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FAE)
    Sleep(100)
    SetChrSubChip(0x8, 1)
    OP_22(0x84, 0x0, 0x64)
    SetChrChipByIndex(0xB, 8)
    SetChrSubChip(0xB, 0)
    OP_8C(0xB, 25, 0)

    def lambda_FE9():
        OP_8F(0xFE, 0xF82, 0x0, 0x68C4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_FE9)
    WaitChrThread(0xB, 0x1)
    Sleep(400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    def lambda_101D():
        OP_6D(3930, 0, 23850, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_101D)

    def lambda_1035():
        OP_6C(162000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1035)

    def lambda_1045():
        OP_67(0, 6360, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1045)

    def lambda_105D():
        OP_6E(280, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_105D)

    def lambda_106D():

        label("loc_106D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_106D")

    QueueWorkItem2(0xB, 2, lambda_106D)

    def lambda_107E():
        OP_96(0xFE, 0x398, 0x0, 0x63BA, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_107E)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)

    def lambda_10AB():
        OP_96(0xFE, 0x6B8, 0x0, 0x56C2, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_10AB)
    Sleep(100)
    SetChrChipByIndex(0x8, 9)

    def lambda_10D3():

        label("loc_10D3")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_10D3")

    QueueWorkItem2(0x8, 2, lambda_10D3)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_44(0xB, 0x2)
    OP_44(0x8, 0x2)
    SetChrChipByIndex(0xB, 3)
    ClearChrFlags(0xB, 0x800)
    SetChrChipByIndex(0xB, 17)
    Sleep(500)

    ChrTalk(    #6
        0xB,
        "#1006F要上了，亚妮拉丝！\x02",
    )

    CloseMessageWindow()
    OP_99(0xB, 0x0, 0x4, 0x3E8)
    Sleep(500)

    ChrTalk(    #7
        0xB,
        "#1005F#4S烈破──无双击！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 4)

    def lambda_1170():
        OP_8E(0xFE, 0x1054, 0x0, 0x625C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1170)
    WaitChrThread(0xB, 0x1)

    def lambda_1190():
        OP_6D(5450, 0, 26870, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1190)

    def lambda_11A8():
        OP_6C(130000, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11A8)

    def lambda_11B8():
        OP_6E(215, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11B8)

    def lambda_11C8():
        OP_67(0, 7460, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_11C8)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 18)
    SetChrSubChip(0xB, 1)

    def lambda_11F4():
        OP_8F(0xFE, 0x12A2, 0x0, 0x684C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_11F4)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0x8, 14)
    SetChrChipByIndex(0xB, 7)
    SetChrSubChip(0xB, 0)

    def lambda_1223():
        OP_9E(0xFE, 0x1E, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1223)
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

    def lambda_1349():
        OP_99(0xFE, 0x0, 0xC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1349)
    Sleep(400)
    PlayEffect(0x1, 0x1, 0xB, 1000, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1393():
        OP_6D(6410, 0, 28130, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1393)

    def lambda_13AB():
        OP_6C(156000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13AB)

    def lambda_13BB():
        OP_6E(226, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13BB)

    def lambda_13CB():
        OP_67(0, 6540, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13CB)

    def lambda_13E3():
        OP_96(0xFE, 0x1ACC, 0x0, 0x7418, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13E3)
    WaitChrThread(0x8, 0x1)

    def lambda_1406():
        OP_96(0xFE, 0x1D4C, 0x0, 0x7710, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1406)
    WaitChrThread(0x8, 0x1)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)

    ChrTalk(    #8
        0x8,
        (
            "#814F#6P哇哇，好猛烈。\x02\x03",

            "#816F不过……\x01",
            "这次轮到我了！\x02",
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

    def lambda_1499():
        OP_96(0xFE, 0xE56, 0x0, 0x646E, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1499)
    Sleep(500)

    ChrTalk(    #9
        0x8,
        "#815F#4S剑技──八叶灭杀！\x02",
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

    def lambda_152A():
        OP_8E(0xFE, 0x1234, 0x0, 0x6824, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_152A)

    def lambda_1545():
        OP_6D(4730, 0, 26490, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1545)

    def lambda_155D():
        OP_6C(50000, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_155D)
    WaitChrThread(0x8, 0x1)
    OP_43(0xA, 0x1, 0x0, 0x7)
    WaitChrThread(0xA, 0x1)
    OP_82(0x3, 0x0)

    ChrTalk(    #10
        0xB,
        "#1021F呜……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "#815F#6P还没结束呢～！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 0)

    def lambda_15BB():
        OP_8E(0xFE, 0xF78, 0x0, 0x652C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_15BB)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 11)
    SetChrSubChip(0x8, 0)
    OP_43(0xA, 0x1, 0x0, 0x9)

    ChrTalk(    #12
        0xB,
        (
            "#1003F（呜……\x01",
            "这样下去会撑不住的……）\x02\x03",

            "#1002F（那就……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_82(0x3, 0x0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0xB, 17)
    SetChrSubChip(0xB, 7)
    OP_7D(0x0, 0xB, 0x32, 0x1F4)

    def lambda_164C():
        OP_8F(0xFE, 0x14E6, 0x0, 0x5FD2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_164C)

    def lambda_1667():
        OP_99(0xFE, 0x7, 0xE, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1667)

    def lambda_1677():
        OP_6D(4400, 0, 26560, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1677)

    def lambda_168F():
        OP_6C(0, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_168F)

    def lambda_169F():
        OP_67(0, 6660, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_169F)
    WaitChrThread(0xB, 0x2)
    SetChrChipByIndex(0xB, 8)
    SetChrSubChip(0xB, 1)
    TurnDirection(0xB, 0x8, 0)
    OP_7D(0x1, 0xB, 0x0, 0x0)

    ChrTalk(    #13 op#A
        0x8,
        "#814F#5P#10A咦，不会吧！？\x02",
    )

    Sleep(1000)
    OP_56(0x0)

    ChrTalk(    #14 op#A
        0xB,
        "#1005F#3S#10A得手了！\x02",
    )

    Sleep(500)
    OP_56(0x0)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 0)

    def lambda_1726():
        OP_99(0xFE, 0x0, 0xC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1726)
    Sleep(400)
    TurnDirection(0x8, 0xB, 0)
    SetChrChipByIndex(0x8, 14)
    SetChrSubChip(0x8, 0)

    def lambda_174C():
        OP_8F(0xFE, 0xC1C, 0x0, 0x682E, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_174C)

    def lambda_1767():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1767)
    PlayEffect(0x1, 0x1, 0x8, 500, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_20(0x5DC)

    ChrTalk(    #15 op#A
        0x8,
        "#1312F#5P#10A呀～！\x02",
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
        "#1312F#5P好痛～……\x02",
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

    def lambda_1877():
        OP_6D(3820, 0, 27610, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1877)
    OP_92(0xB, 0x8, 0x5DC, 0xFA0, 0x0)
    OP_62(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0xB, 21)
    SetChrSubChip(0xB, 0)
    Sleep(500)

    ChrTalk(    #17
        0xB,
        "#1004F没、没事吧，亚妮拉丝？\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x19)
    Sleep(600)

    ChrTalk(    #18
        0x8,
        (
            "#819F#5P啊哈哈，没事啦。\x01",
            "总算来得及防御。\x02",
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
            "#1316F#5P唉～不过真是败给你了。\x02\x03",

            "#1314F还是被艾丝蒂尔\x01",
            "挡回了那招～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        (
            "#1016F嘿嘿，是歪打正着啦。\x02\x03",

            "#1006F之前老被你压得死死的，\x01",
            "也要稍微讨回一点颜面才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#816F#5P呵呵。\x01",
            "真有干劲啊，艾丝蒂尔。\x02\x03",

            "#1310F那么，就顺便\x01",
            "再来一回合试试怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        "#1006F嗯，正合我意！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, 3820, 0, 12520, 0)

    NpcTalk(    #23
        0x9,
        "女性的声音",
        "#5P哎呀哎呀，你们俩可真有精神。\x02",
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

    def lambda_1AFF():
        OP_8E(0x9, 0xEEC, 0x0, 0x5672, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1AFF)
    Sleep(100)
    TurnDirection(0xB, 0x9, 400)
    Sleep(100)
    TurnDirection(0x8, 0x9, 400)
    Sleep(200)
    ClearChrFlags(0x9, 0x80)
    Sleep(1000)

    ChrTalk(    #24
        0x8,
        (
            "#811F#6P啊，管理员。\x01",
            "早上好～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xB,
        "#1018F#5P管理员，早上好！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #26
        0x9,
        (
            "#2P你们早啊。\x01",
            "艾丝蒂尔，亚妮拉丝。\x02\x03",

            "早餐已经做好了，\x01",
            "我过来招呼你们用餐……\x02\x03",

            "嗯～该不会打扰你们了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        "#1004F#5P啊，这样啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 400)
    Sleep(300)

    ChrTalk(    #28
        0xB,
        "#1015F#5P亚妮拉丝你觉得呢？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 400)
    Sleep(300)

    ChrTalk(    #29
        0x8,
        (
            "#817F#6P嗯～是啊。\x02\x03",

            "#810F饭菜冷掉就可惜了，\x01",
            "今天早上就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C91():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C91)
    Sleep(50)

    def lambda_1CA4():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1CA4)
    Sleep(300)

    ChrTalk(    #30
        0x8,
        (
            "#1310F#6P管理员。\x01",
            "克鲁茨前辈现在在干吗呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "#2P克鲁茨先生\x01",
            "说要去准备演习，\x01",
            "已经先吃完早餐了。\x02\x03",

            "听说今天的演习\x01",
            "相当严峻呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        "#1019F#5P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#1317F#6P前、前辈是\x01",
            "那么说的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "嗯，他要我转告说，\x01",
            "请你们早餐要好好吃饱。\x02\x03",

            "你们两人都多吃点，\x01",
            "好储备足够的体力哦㈱\x02",
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

    # Function_4_5A1 end

    def Function_5_1DE3(): pass

    label("Function_5_1DE3")

    SetChrPos(0xB, 510, 0, 22930, 90)
    SetChrPos(0x8, 7610, 0, 24760, 270)

    def lambda_1E0B():
        OP_8E(0xFE, 0x104A, 0x0, 0x5CBC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1E0B)
    Sleep(300)

    def lambda_1E2B():
        OP_8E(0xFE, 0x15CC, 0x0, 0x5C80, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E2B)
    Sleep(300)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 5)

    def lambda_1E5A():
        OP_99(0xFE, 0x5, 0xC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1E5A)
    WaitChrThread(0x8, 0x1)

    def lambda_1E6F():
        OP_96(0xFE, 0x13BA, 0x0, 0x532A, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1E6F)
    Sleep(200)

    def lambda_1E92():
        TurnDirection(0x8, 0xB, 0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E92)
    Sleep(200)
    OP_44(0xB, 0x0)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    TurnDirection(0x8, 0xB, 1000)

    def lambda_1EBA():
        OP_8E(0xFE, 0x10FE, 0x0, 0x5AAA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1EBA)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)

    def lambda_1EE4():
        OP_96(0xFE, 0x10B8, 0x0, 0x6504, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1EE4)
    SetChrSubChip(0x8, 1)
    WaitChrThread(0xB, 0x0)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 0)

    def lambda_1F16():
        OP_8F(0xFE, 0x1054, 0x0, 0x5F14, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1F16)
    WaitChrThread(0x8, 0x1)

    def lambda_1F36():
        OP_8F(0xFE, 0xF78, 0x0, 0x6C66, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1F36)
    TurnDirection(0x8, 0xB, 1000)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 1)
    Sleep(200)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 0)

    def lambda_1F71():
        OP_8F(0xFE, 0x102C, 0x0, 0x5D8E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1F71)
    SetChrPos(0xB, 3960, 0, 27750, 180)
    SetChrPos(0x8, 4140, 0, 23950, 0)
    Return()

    # Function_5_1DE3 end

    def Function_6_1FA9(): pass

    label("Function_6_1FA9")

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

    def lambda_2012():
        OP_8F(0xFE, 0xF3C, 0x0, 0x6950, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2012)
    WaitChrThread(0xB, 0x1)
    Sleep(200)
    ClearChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 4)
    SetChrSubChip(0xB, 0)

    def lambda_2046():
        OP_8E(0xFE, 0xF3C, 0x0, 0x5A8C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2046)
    Sleep(200)

    def lambda_2066():
        OP_96(0xFE, 0xF3C, 0x0, 0x613A, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2066)
    OP_22(0xA3, 0x0, 0x3C)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 5)

    def lambda_209D():
        OP_8F(0xFE, 0xF3C, 0x0, 0x5550, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_209D)

    def lambda_20B8():
        OP_99(0xFE, 0x5, 0x9, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_20B8)
    OP_22(0x84, 0x0, 0x3C)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x3C)

    def lambda_20D7():
        OP_96(0xFE, 0xF3C, 0x0, 0x6950, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_20D7)

    def lambda_20F5():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_20F5)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x3C)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 0)
    OP_22(0xA3, 0x0, 0x3C)

    def lambda_211C():
        OP_96(0xFE, 0xF3C, 0x0, 0x6306, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_211C)

    def lambda_213A():
        OP_99(0xFE, 0x0, 0x9, 0x9C4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_213A)

    def lambda_214A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_214A)
    Sleep(300)

    def lambda_215D():
        OP_96(0xFE, 0x1DBA, 0x0, 0x60B8, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_215D)

    def lambda_217B():

        label("loc_217B")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_217B")

    QueueWorkItem2(0x8, 2, lambda_217B)
    Sleep(100)
    OP_22(0x84, 0x0, 0x50)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x50)
    Sleep(400)
    SetChrChipByIndex(0xB, 8)
    SetChrSubChip(0xB, 0)

    def lambda_21AF():
        OP_96(0xFE, 0x1FE, 0x0, 0x5992, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_21AF)

    def lambda_21CD():

        label("loc_21CD")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_21CD")

    QueueWorkItem2(0xB, 2, lambda_21CD)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x50)
    OP_44(0x8, 0x2)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x50)
    OP_44(0xB, 0x2)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    Return()

    # Function_6_1FA9 end

    def Function_7_21FF(): pass

    label("Function_7_21FF")

    SetChrChipByIndex(0x8, 11)
    SetChrSubChip(0x8, 0)
    OP_99(0x8, 0x0, 0x7, 0xFA0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_2252():
        OP_9E(0xFE, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_2252)
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_22A1():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_22A1)

    def lambda_22BC():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22BC)
    OP_99(0x8, 0x0, 0x7, 0xFA0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_234F():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_234F)

    def lambda_236A():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_236A)
    OP_99(0x8, 0x0, 0x7, 0xFA0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_23FD():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_23FD)

    def lambda_2418():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2418)
    OP_99(0x8, 0x0, 0x7, 0xFA0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_24AB():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_24AB)

    def lambda_24C6():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_24C6)
    OP_99(0x8, 0x0, 0x7, 0xFA0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2559():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2559)

    def lambda_2574():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2574)
    OP_99(0x8, 0x0, 0x7, 0xFA0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2607():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2607)

    def lambda_2622():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2622)
    SetChrSubChip(0x8, 0)

    def lambda_2642():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0xBB8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2642)
    Sleep(500)

    def lambda_2665():
        OP_99(0x8, 0x0, 0x5, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2665)

    def lambda_2675():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFFF7E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2675)
    Sleep(300)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0x12C, 0x64)
    WaitChrThread(0x8, 0x0)
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_271A():
        OP_96(0xFE, 0x1928, 0x0, 0x6F68, 0x9C4, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_271A)
    OP_43(0xA, 0x2, 0x0, 0x8)
    WaitChrThread(0xA, 0x2)
    WaitChrThread(0x8, 0x3)
    OP_22(0xA4, 0x0, 0x64)
    TurnDirection(0x8, 0xB, 1000)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 0)
    Return()

    # Function_7_21FF end

    def Function_8_275A(): pass

    label("Function_8_275A")

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

    # Function_8_275A end

    def Function_9_27F5(): pass

    label("Function_9_27F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_289D")
    PlayEffect(0x3, 0x0, 0x8, -1000, 800, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x8, 0x0, 0x7, 0xFA0)
    PlayEffect(0x4, 0xFF, 0xB, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_287C():
        OP_9E(0xB, 0x1E, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_287C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_289A")
    Jump("loc_289D")

    label("loc_289A")

    Jump("Function_9_27F5")

    label("loc_289D")

    Return()

    # Function_9_27F5 end

    def Function_10_289E(): pass

    label("Function_10_289E")

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
        "#840F#6P两人都准备好了吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 12)
    Return()

    # Function_10_289E end

    def Function_11_2932(): pass

    label("Function_11_2932")

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
            "#840F#6P制造了新的结晶回路，\x01",
            "也准备好回复系魔法了吗。\x02\x03",

            "这样一来总算可以出发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1007F#5P哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10A,
        (
            "#818F嗯，记得是西边的\x01",
            "中世纪地下水道吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xA,
        (
            "#843F#6P嗯嗯，是『巴斯塔尔水道』。\x02\x03",

            "#842F话先说在前头，水道里\x01",
            "徘徊着危险的魔兽。\x02\x03",

            "你们两人都准备好了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC5, 0x1, 0x40)
    OP_28(0xC5, 0x4, 0x10)
    OP_28(0xC5, 0x4, 0x20)
    Call(0, 12)
    Return()

    # Function_11_2932 end

    def Function_12_2AC1(): pass

    label("Function_12_2AC1")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【向目的地出发】\x01",      # 0
            "【还要准备准备】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B50")

    ChrTalk(    #40
        0xA,
        (
            "#840F#6P明白了。\x01",
            "准备充足一点吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_2B50")


    ChrTalk(    #41
        0xA,
        (
            "#840F#6P明白了。\x01",
            "那么出发吧。\x02\x03",

            "你们两个都跟我来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#1018F#5P明白！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10A,
        "#1310F明白了！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x40)
    OP_8C(0xA, 180, 500)

    def lambda_2BC2():
        OP_8E(0xA, 0xFFFFF484, 0x0, 0xFFFF5FC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2BC2)
    Sleep(300)

    def lambda_2BE2():
        OP_8E(0x10A, 0xFFFFF484, 0x0, 0xFFFF5FC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2BE2)
    Sleep(500)

    def lambda_2C02():
        OP_8E(0x101, 0xFFFFF484, 0x0, 0xFFFF5FC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C02)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    ClearChrFlags(0x101, 0x40)
    Call(0, 13)
    NewScene("ED6_DT21/C5503   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2AC1 end

    def Function_13_2C3F(): pass

    label("Function_13_2C3F")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS137._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DD4")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D01"),
        (1, "loc_2D4F"),
        (SWITCH_DEFAULT, "loc_2DD1"),
    )


    label("loc_2D01")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("克鲁茨")

    AnonymousTalk(    #44
        (
            "\x07\x00#840F目的地是西边的\x01",
            "【巴斯塔尔水道】。\x02\x03",

            "选那边吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_2DD1")

    label("loc_2D4F")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #45
        "\x07\x05要移动至【巴斯塔尔水道】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2DBE"),
        (1, "loc_2DCB"),
        (SWITCH_DEFAULT, "loc_2DCE"),
    )


    label("loc_2DBE")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DCE")

    label("loc_2DCB")

    Jump("loc_2DCE")

    label("loc_2DCE")

    Jump("loc_2DD1")

    label("loc_2DD1")

    Jump("loc_2CA0")

    label("loc_2DD4")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_13_2C3F end

    def Function_14_2E0F(): pass

    label("Function_14_2E0F")

    ClearMapFlags(0x2000000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_2E32")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E43")

    label("loc_2E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 2)), scpexpr(EXPR_END)), "loc_2E43")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E43")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS137._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31D1")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2EDF"),
        (1, "loc_2F0B"),
        (2, "loc_2F48"),
        (SWITCH_DEFAULT, "loc_2F9A"),
    )


    label("loc_2EDF")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
        )
    )

    Jump("loc_2F9A")

    label("loc_2F0B")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
            "【圣科洛瓦森林】\x01",      # 2
        )
    )

    Jump("loc_2F9A")

    label("loc_2F48")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",            # 0
            "【巴斯塔尔水道】\x01",          # 1
            "【圣科洛瓦森林】\x01",          # 2
            "【格林姆瑟尔小要塞】\x01",      # 3
        )
    )

    Jump("loc_2F9A")

    label("loc_2F9A")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FC4"),
        (1, "loc_3044"),
        (2, "loc_30C6"),
        (3, "loc_3148"),
        (SWITCH_DEFAULT, "loc_31CE"),
    )


    label("loc_2FC4")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #46
        "\x07\x05要移动至【训练场宿舍】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3031"),
        (1, "loc_303E"),
        (SWITCH_DEFAULT, "loc_3041"),
    )


    label("loc_3031")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3041")

    label("loc_303E")

    Jump("loc_3041")

    label("loc_3041")

    Jump("loc_31CE")

    label("loc_3044")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #47
        "\x07\x05要移动至【巴斯塔尔水道】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30B3"),
        (1, "loc_30C0"),
        (SWITCH_DEFAULT, "loc_30C3"),
    )


    label("loc_30B3")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30C3")

    label("loc_30C0")

    Jump("loc_30C3")

    label("loc_30C3")

    Jump("loc_31CE")

    label("loc_30C6")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #48
        "\x07\x05要移动至【圣科洛瓦森林】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3135"),
        (1, "loc_3142"),
        (SWITCH_DEFAULT, "loc_3145"),
    )


    label("loc_3135")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3145")

    label("loc_3142")

    Jump("loc_3145")

    label("loc_3145")

    Jump("loc_31CE")

    label("loc_3148")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #49
        "\x07\x05要移动至【格林姆瑟尔小要塞】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31BB"),
        (1, "loc_31C8"),
        (SWITCH_DEFAULT, "loc_31CB"),
    )


    label("loc_31BB")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31CB")

    label("loc_31C8")

    Jump("loc_31CB")

    label("loc_31CB")

    Jump("loc_31CE")

    label("loc_31CE")

    Jump("loc_2EB4")

    label("loc_31D1")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_31EA"),
        (1, "loc_321E"),
        (2, "loc_3252"),
        (3, "loc_3286"),
        (SWITCH_DEFAULT, "loc_32BA"),
    )


    label("loc_31EA")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_32BA")

    label("loc_321E")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_32BA")

    label("loc_3252")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_32BA")

    label("loc_3286")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_32BA")

    label("loc_32BA")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_32DC"),
        (1, "loc_32F4"),
        (2, "loc_3300"),
        (3, "loc_330C"),
        (SWITCH_DEFAULT, "loc_3318"),
    )


    label("loc_32DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_END)), "loc_32E8")
    SetMapFlags(0x2000000)

    label("loc_32E8")

    NewScene("ED6_DT21/T5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3318")

    label("loc_32F4")

    NewScene("ED6_DT21/C5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3318")

    label("loc_3300")

    NewScene("ED6_DT21/C5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_3318")

    label("loc_330C")

    NewScene("ED6_DT21/C5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_3318")

    label("loc_3318")

    Return()

    # Function_14_2E0F end

    def Function_15_3319(): pass

    label("Function_15_3319")

    EventBegin(0x0)
    SetChrPos(0x101, -4030, 0, -16260, 4)
    SetChrPos(0x10A, -3010, 0, -16920, 0)
    OP_6D(-4570, 0, 10280, 0)
    OP_67(0, 7680, -10000, 0)
    OP_6B(4880, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)

    def lambda_3389():
        OP_6D(-3880, 0, -13000, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3389)
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
            "#5P#1002F从这里看上去\x01",
            "好像没有人的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10A,
        (
            "#6P#812F嗯……\x01",
            "进去也没关系吧。\x02\x03",

            "但是，也有可能设了陷阱，\x01",
            "所以必须要谨慎地行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#5P#1002F明白。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x101B)
    OP_28(0x80, 0x1, 0x1)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_15_3319 end

    def Function_16_3494(): pass

    label("Function_16_3494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_351B")
    EventBegin(0x1)
    OP_4A(0xA, 255)
    TurnDirection(0xA, 0x0, 400)

    ChrTalk(    #53
        0xA,
        (
            "#843F你们两人都准备好了吗？\x02\x03",

            "#840F要出发的时候\x01",
            "就跟我说一声吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    OP_8C(0xA, 0, 0)
    OP_4B(0xA, 255)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_35F6")

    label("loc_351B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3588")
    EventBegin(0x1)

    ChrTalk(    #54
        0x101,
        (
            "#1015F……不知不觉中\x01",
            "演习就要开始了呢。\x02\x03",

            "得回房间整理装备才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_35F6")

    label("loc_3588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F6")
    EventBegin(0x1)

    ChrTalk(    #55
        0x101,
        (
            "#1015F……让克鲁茨前辈他们\x01",
            "等太久可就不好了呢。\x02\x03",

            "必须赶快到大门去。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_35F6")

    Return()

    # Function_16_3494 end

    def Function_17_35F7(): pass

    label("Function_17_35F7")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #56
        (
            "\x07\x05　　 游击士协会\x01",
            "【卢·洛克尔训练场】\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_35F7 end

    SaveToFile()

Try(main)
