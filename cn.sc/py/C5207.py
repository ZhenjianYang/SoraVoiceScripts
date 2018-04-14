from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5207   ._SN',
        MapName             = 'Other',
        Location            = 'C5207.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60066",
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
        '目标用照相机',                         # 9
        '地震控制用假人',                       # 10
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_EA",           # 00, 0
        "Function_1_EF",           # 01, 1
        "Function_2_106",          # 02, 2
        "Function_3_CBB",          # 03, 3
        "Function_4_CDE",          # 04, 4
        "Function_5_D33",          # 05, 5
    )


    def Function_0_EA(): pass

    label("Function_0_EA")

    Event(0, 2)
    Return()

    # Function_0_EA end

    def Function_1_EF(): pass

    label("Function_1_EF")

    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 1)
    OP_22(0x1C3, 0x1, 0x46)
    Return()

    # Function_1_EF end

    def Function_2_106(): pass

    label("Function_2_106")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x2601F8, 0x2601FD, 0x0)
    OP_D2(0x26008C, 0x260091, 0x1)
    SetChrPos(0x101, 940, -8000, 46490, 0)
    SetChrPos(0x102, 940, -8000, 46490, 0)
    OP_6D(1120, -7920, 44810, 0)
    OP_67(0, 5990, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(349, 0)
    OP_43(0x9, 0x3, 0x0, 0x3)
    OP_22(0x85, 0x1, 0x46)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x0, 0x10)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)

    def lambda_1BC():
        OP_6D(1070, -8000, 14420, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1BC)

    def lambda_1D4():
        OP_8E(0xFE, 0x17C, 0xFFFFE0C0, 0x3728, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D4)
    Sleep(300)

    def lambda_1F4():
        OP_8E(0xFE, 0x78A, 0xFFFFE0C0, 0x3728, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F4)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_22(0x88, 0x0, 0x64)
    OP_7C(0x3E8, 0x0, 0x3E8, 0x1F4)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x101,
        "#1014F#5P#1K呀……！\x02",
    )


    ChrTalk(    #1
        0x102,
        "#1047F#6P#1K……唔……！\x02",
    )

    OP_56(0x1)
    OP_59()
    Sleep(100)
    Fade(500)
    OP_44(0x8, 0x1)
    OP_6D(-80, -8000, 4540, 0)
    OP_67(0, 6040, -10000, 0)
    OP_6B(3870, 0)
    OP_6C(315000, 0)
    OP_6E(387, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x257, 0x0, 0x64)
    OP_6F(0x3, 1)
    OP_70(0x3, 0x6)
    OP_73(0x3)
    Sleep(500)

    ChrTalk(    #2
        0x101,
        "#1004F#6P……啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        "#1046F#6P糟了……！\x02",
    )

    CloseMessageWindow()

    def lambda_340():
        OP_8E(0xFE, 0x17C, 0xFFFFE0C0, 0x23C8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_340)
    Sleep(60)

    def lambda_360():
        OP_8E(0xFE, 0x78A, 0xFFFFE0C0, 0x23C8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_360)
    Sleep(200)
    OP_22(0x259, 0x0, 0x64)
    Sleep(300)
    OP_6F(0x3, 5)
    OP_70(0x3, 0x190)
    Sleep(1000)
    Fade(500)
    OP_6D(520, -8000, 9150, 0)
    OP_67(0, 6580, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(315000, 0)
    OP_6E(276, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #4
        0x101,
        "#1020F#5P啊啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 600)

    ChrTalk(    #5
        0x102,
        "#1046F快回去，艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    def lambda_421():
        OP_6D(770, -8000, 13840, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_421)
    OP_8C(0x101, 0, 600)

    def lambda_440():
        OP_8E(0xFE, 0x1AE, 0xFFFFE0C0, 0x3BC4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_440)
    Sleep(50)
    OP_8C(0x102, 0, 600)

    def lambda_467():
        OP_8E(0xFE, 0x848, 0xFFFFE0C0, 0x3BC4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_467)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_22(0x88, 0x0, 0x64)
    OP_7C(0x3E8, 0x0, 0x3E8, 0x1F4)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(-40, -8000, 21740, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(6500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_20(0xBB8)
    OP_22(0x259, 0x0, 0x64)
    OP_6F(0x3, 400)
    OP_70(0x3, 0x24E)
    Sleep(1000)
    OP_73(0x3)
    Fade(500)
    OP_6D(0, -8000, 17970, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(3290, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #6
        0x101,
        "#1026F#5P……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x50)
    OP_24(0x85, 0x3C)
    Sleep(100)
    OP_24(0x85, 0x32)
    Sleep(400)

    def lambda_5C2():
        OP_6D(1360, -8000, 19520, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5C2)

    def lambda_5DA():
        OP_67(0, 6370, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5DA)

    def lambda_5F2():
        OP_8F(0xFE, 0x5D2, 0xFFFFE0C0, 0x4510, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F2)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #7
        0x101,
        "#1003F#5P好像…回不……去了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1043F#6P嗯……\x02\x03",

            "#1035F大概是下面的细梁\x01",
            "支撑不住这里了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1025F#5P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#1043F#6P对不起，艾丝蒂尔……\x02\x03",

            "要是我那时候\x01",
            "没有拖累你的话……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6DC():
        OP_6D(790, -8000, 17650, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DC)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #11
        0x101,
        (
            "#1007F#2P别说这种话啦。\x02\x03",

            "#1006F当时要不是约修亚救我，\x01",
            "恐怕我都已经被落下的岩石\x01",
            "砸中了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#1043F#6P但是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1016F#2P嘿嘿……为什么呢。\x02\x03",

            "在这样的状况下，\x01",
            "却一点儿也不害怕。\x02\x03",

            "#1008F约修亚呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#1044F#6P啊……\x02\x03",

            "#1053F嗯……是啊。\x02\x03",

            "#1054F我也完全不觉得恐惧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(7350, -18890, 23200, 0)
    OP_67(0, 6770, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(315000, 0)
    OP_6E(359, 0)
    OP_0D()
    OP_22(0x154, 0x0, 0x64)
    OP_6F(0x3, 590)
    OP_70(0x3, 0x258)
    OP_73(0x3)
    Sleep(1000)

    def lambda_876():
        OP_6D(790, -8000, 17650, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_876)

    def lambda_88E():
        OP_67(0, 4800, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_88E)

    def lambda_8A6():
        OP_6B(3290, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8A6)

    def lambda_8B6():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8B6)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #15
        0x101,
        (
            "#1013F#2P那个……约修亚。\x02\x03",

            "能不能拜托你两件事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#1040F#6P可以啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1012F#2P第一件事……\x02\x03",

            "#1017F能不能，\x01",
            "紧紧抱住我？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        "#1049F#6P非常乐意。\x02",
    )

    CloseMessageWindow()

    def lambda_96D():
        OP_6D(770, -8000, 18200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_96D)

    def lambda_985():
        OP_6B(3100, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_985)
    OP_8E(0x102, 0x5DC, 0xFFFFE0C0, 0x42B8, 0x5DC, 0x0)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x102, 0x80)
    OP_99(0x101, 0x0, 0x4, 0x3E8)
    Sleep(1000)

    ChrTalk(    #19
        0x101,
        "#1008F#2P嘿嘿……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        "#1040F#6P……还有呢？\x02",
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x24), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x25), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(500)

    ChrTalk(    #21
        0x101,
        (
            "#1013F#2P嗯，那个……\x02\x03",

            "这么说的话不知道\x01",
            "会不会被你讨厌……\x02\x03",

            "但我还是……\x01",
            "不想留下遗憾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#1035F#6P……对不起。\x01",
            "还是让我先说吧。\x02\x03",

            "#1041F艾丝蒂尔……\x01",
            "可以吻你吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1004F#2P啊……\x02",
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x24), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(500)

    ChrTalk(    #24
        0x101,
        "#1017F#2P……嗯……！\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x85)
    Sleep(500)
    OP_99(0x101, 0x4, 0x6, 0x3E8)
    Sleep(500)

    def lambda_B52():
        OP_6B(2900, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B52)
    OP_99(0x101, 0x6, 0x8, 0x3E8)
    Sleep(2000)

    def lambda_B70():
        OP_99(0xFE, 0x8, 0xA, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B70)

    def lambda_B80():
        OP_67(0, 10670, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B80)

    def lambda_B98():
        OP_6E(378, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B98)
    Sleep(1000)
    OP_22(0x259, 0x0, 0x64)
    OP_B0(0x3, 0x28)
    OP_6F(0x3, 600)
    OP_70(0x3, 0x3E8)

    def lambda_BC4():
        OP_67(0, 14670, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BC4)

    def lambda_BDC():
        OP_6D(770, -20000, 18200, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BDC)

    def lambda_BF4():
        OP_6B(1000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BF4)
    ClearChrFlags(0x101, 0x1)
    OP_99(0x101, 0xA, 0xC, 0x4B0)
    OP_43(0x102, 0x3, 0x0, 0x4)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x85, 0x28)
    Sleep(200)
    OP_24(0x85, 0x1E)
    Sleep(200)
    OP_24(0x85, 0x14)
    Sleep(200)
    OP_24(0x85, 0xA)
    Sleep(200)
    OP_23(0x85)
    ClearMapFlags(0x100000)
    OP_C4(0x0, 0x10)
    OP_48()
    FadeToBright(1, 0)
    PlayMovie(0x0, "ED6_DT46.dat", 0x0, 0x1)

    label("loc_C72")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C8C")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_C89")
    Jump("loc_C8C")

    label("loc_C89")

    Jump("loc_C72")

    label("loc_C8C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(500)
    OP_C4(0x1, 0x10)
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0110   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_2_106 end

    def Function_3_CBB(): pass

    label("Function_3_CBB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CDD")
    OP_7C(0x1E, 0x1E, 0x3E8, 0x384)
    Sleep(1000)
    Jump("Function_3_CBB")

    label("loc_CDD")

    Return()

    # Function_3_CBB end

    def Function_4_CDE(): pass

    label("Function_4_CDE")

    SetChrPos(0x101, 1500, -8500, 17200, 0)
    SetChrFlags(0x101, 0x20)

    def lambda_CFA():
        OP_91(0xFE, 0x0, 0xFFFF3CB0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CFA)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    def lambda_D25():

        label("loc_D25")

        OP_99(0x101, 0xE, 0x1D, 0x5DC)
        OP_48()
        Jump("loc_D25")

    QueueWorkItem2(0x102, 2, lambda_D25)
    Return()

    # Function_4_CDE end

    def Function_5_D33(): pass

    label("Function_5_D33")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D7F")
    OP_51(0x8, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_5_D33")

    label("loc_D7F")

    Return()

    # Function_5_D33 end

    SaveToFile()

Try(main)
