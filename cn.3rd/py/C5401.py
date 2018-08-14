from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5401   ._SN',
        MapName             = 'Other',
        Location            = 'C5401.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T7000   ._SN',
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
        '怀斯曼教授',                           # 9
        '小丑肯帕雷拉',                         # 10
        '怀斯曼之杖',                           # 11
        '目标用照相机',                         # 12
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03550 ._CH',             # 00
        'ED6_DT27/CH03600 ._CH',             # 01
        'ED6_DT26/CH20765 ._CH',             # 02
        'ED6_DT26/CH20485 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03550P._CP',             # 00
        'ED6_DT27/CH03600P._CP',             # 01
        'ED6_DT26/CH20765P._CP',             # 02
        'ED6_DT26/CH20485P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_1D5",          # 01, 1
        "Function_2_204",          # 02, 2
        "Function_3_57F",          # 03, 3
        "Function_4_5D6",          # 04, 4
        "Function_5_A73",          # 05, 5
        "Function_6_DD0",          # 06, 6
        "Function_7_E29",          # 07, 7
        "Function_8_15A9",         # 08, 8
        "Function_9_16A4",         # 09, 9
        "Function_10_179F",        # 0A, 10
        "Function_11_1817",        # 0B, 11
        "Function_12_18BB",        # 0C, 12
        "Function_13_19AD",        # 0D, 13
        "Function_14_1A57",        # 0E, 14
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_166"),
        (102, "loc_16D"),
        (SWITCH_DEFAULT, "loc_174"),
    )


    label("loc_166")

    Event(0, 8)
    Jump("loc_174")

    label("loc_16D")

    Event(0, 9)
    Jump("loc_174")

    label("loc_174")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_18D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_1B8")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)
    Jump("loc_1D4")

    label("loc_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1D4")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_1D4")

    Return()

    # Function_0_14A end

    def Function_1_1D5(): pass

    label("Function_1_1D5")

    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F1")
    OP_1B(0x1, 0x0, 0xA)
    OP_1B(0x2, 0x0, 0xB)
    Jump("loc_203")

    label("loc_1F1")

    OP_71(0x407, 0x0)
    ExitThread()
    OP_71(0x408, 0x0)
    ExitThread()
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)

    label("loc_203")

    Return()

    # Function_1_1D5 end

    def Function_2_204(): pass

    label("Function_2_204")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_22(0x85, 0x28, 0x64)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1140, 1500, 85570, 0)
    OP_6D(-300, 0, 53260, 0)
    OP_67(0, 9770, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(45000, 0)
    OP_6E(410, 0)

    def lambda_282():
        OP_6D(-510, 1500, 87040, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_282)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    Fade(500)
    OP_71(0x404, 0x0)
    ExitThread()
    OP_79(0x9, 0x2)
    OP_7B()
    OP_6D(20, 1500, 86880, 0)
    OP_67(0, 4690, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #0
        0x11,
        (
            "#850F#5P呵呵，这声音真令人心情舒畅啊。\x02\x03",

            "所有的一切都在\x01",
            "崩坏毁灭的声音……\x02\x03",

            "……枕着古代都市的瓦砾\x01",
            "陷入永远的长眠。\x02\x03",

            "教授也一定\x01",
            "会满意吧？\x02\x03",

            "哈哈，没问题。\x01",
            "之后的事就交给我吧。\x02\x03",

            "所以，教授……\x02\x03",

            "……你不用再从那\x01",
            "炼狱出来了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x2)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x11, 1)
    Sleep(300)
    OP_22(0xBC, 0x0, 0x64)
    SetChrSubChip(0x11, 2)
    Sleep(300)
    OP_43(0x12, 0x0, 0x0, 0x3)
    WaitChrThread(0x12, 0x0)
    Fade(250)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x11, 0x2)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x00◆追加肯帕雷拉喜欢打响指。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #2
        0x11,
        (
            "#850F#5PＮｏ．０――\x01",
            "『小丑肯帕雷拉』。\x02\x03",

            "代替『蛇之使徒』第三支柱――\x01",
            "怀斯曼\x01",
            "申请进入『星辰之间』。\x02",
        )
    )

    Jump("loc_4F2")

    label("loc_4F2")

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x3, 0x0, 0x0, 0x6)
    OP_20(0x7D0)
    Fade(2000)
    OP_6D(20, 1500, 156880, 0)
    OP_67(0, 4690, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x11, -1140, 1500, 155570, 0)
    SetChrPos(0x12, -1140, 1500, 156570, 0)
    OP_0D()
    OP_A2(0x2506)
    OP_4F(0x43, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/C5416   ._SN", 100, 1, 0)
    IdleLoop()
    Return()

    # Function_2_204 end

    def Function_3_57F(): pass

    label("Function_3_57F")

    SetChrFlags(0xFE, 0x800)
    SetChrChipByIndex(0xFE, 3)
    SetChrSubChip(0xFE, 5)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1140, 1500, 86570, 0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x2)

    def lambda_5BF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5BF)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_3_57F end

    def Function_4_5D6(): pass

    label("Function_4_5D6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_71(0x406, 0x0)
    ExitThread()
    OP_6D(0, 0, 60700, 0)
    OP_67(0, 8920, -10000, 0)
    OP_6B(4560, 0)
    OP_6C(55000, 0)
    OP_6E(328, 0)
    LoadEffect(0x0, "map\\\\mp294_00.eff")
    LoadEffect(0x1, "map\\\\mp294_01.eff")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1000, 0, 65360, 0)

    def lambda_681():
        OP_6D(1000, 0, 84400, 7000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_681)

    def lambda_699():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_699)

    def lambda_6A9():
        OP_8E(0xFE, 0xFFFFFC18, 0x5DC, 0x14F00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6A9)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x13, 0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(-60, 1500, 86800, 0)
    OP_67(0, 5300, -10000, 0)
    OP_6B(3450, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x11, 0x1)
    Sleep(500)

    ChrTalk(    #3
        0x11,
        (
            "#850F呵呵，外面的杂音\x01",
            "到这里面就听不到了。\x02\x03",

            "#853F不过，如果不是这样，\x01",
            "也就没法完成任务了呢。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x11, 1)
    Sleep(200)
    SetChrSubChip(0x11, 2)
    Sleep(400)
    OP_22(0xBC, 0x0, 0x64)
    SetChrSubChip(0x11, 3)
    Sleep(50)
    OP_20(0x0)
    Sleep(450)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_7DF():
        OP_6D(-1000, 2300, 88200, 1500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_7DF)

    def lambda_7F7():
        OP_67(0, 4440, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_7F7)

    def lambda_80F():
        OP_6C(0, 1500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_80F)

    def lambda_81F():
        OP_6E(605, 1500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_81F)
    WaitChrThread(0x13, 0x0)
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(200)
    OP_22(0x9D, 0x0, 0x64)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x403, 0x0)
    ExitThread()
    OP_72(0x404, 0x0)
    ExitThread()
    OP_72(0x405, 0x0)
    ExitThread()
    OP_0D()
    Sleep(400)
    Fade(200)
    OP_22(0x9D, 0x0, 0x64)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0x11,
        (
            "#853F#6P──接入。\x02\x03",

            "#854F执行者Ｎｏ．０。\x01",
            "『小丑』肯帕雷拉。\x02\x03",

            "代替『蛇之使徒』第三支柱\x01",
            "盖鲁格·怀斯曼，\x01",
            "申请进入『星辰之间』。\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0xE0)
    Sleep(500)
    OP_59()
    Fade(1000)
    PlayEffect(0x0, 0x1, 0xFF, -6820, 5000, 75500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 4820, 5000, 75500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xFF, -13120, 5000, 85000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0xFF, 11120, 5000, 85000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x5, 0xFF, -1000, 8500, 91000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_C0(0x14, 0xFA0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/C5416   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_5D6 end

    def Function_5_A73(): pass

    label("Function_5_A73")

    EventBegin(0x0)
    FadeToDark(0, 16777215, -1)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_71(0x406, 0x0)
    ExitThread()
    OP_6D(-60, 1500, 86800, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(3550, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1000, 1500, 85760, 0)
    OP_AE(0x5DC)

    def lambda_B00():
        OP_6B(3350, 3000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_B00)
    FadeToBright(3000, 16777215)
    OP_0D()
    Sleep(500)

    ChrTalk(    #5
        0x11,
        (
            "#853F#6P『幻焰计划』……\x01",
            "终于要开始了吗。\x02\x03",

            "已经做好充分准备……\x01",
            "规模和完成度都是\x01",
            "『福音计划』所无法比拟的。\x02\x03",

            "#854F呵呵……\x01",
            "这下变得好玩了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #6
        0x11,
        (
            "#855F#6P……对了。\x02\x03",

            "虽然我也不太好\x01",
            "说别人什么──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_C3C():
        OP_6D(-360, 1500, 86500, 1200)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_C3C)

    def lambda_C54():
        OP_67(0, 7000, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C54)

    def lambda_C6C():
        OP_6B(3550, 1200)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_C6C)
    OP_8C(0x11, 225, 300)
    WaitChrThread(0x13, 0x0)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #7
        0x11,
        (
            "#854F#5P──我不知道你是谁，\x01",
            "不过能不能不要再偷窥了？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00Episode『幻焰计划』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    ClearMapFlags(0x2000000)
    ClearMapFlags(0x100000)
    Sleep(500)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x12, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC3")
    Sleep(500)
    OP_28(0x12, 0x4, 0x10)
    OP_28(0x12, 0x4, 0x20)
    OP_3E(0x18F, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x8F\x01\x07\x00。\x02",
    )

    Jump("loc_D8A")

    label("loc_D8A")

    CloseMessageWindow()
    AddMira(30000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #10
        "\x07\x00得到了\x07\x02３００００米拉\x07\x00。\x02",
    )

    Jump("loc_DB7")

    label("loc_DB7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_DC3")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M5401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_A73 end

    def Function_6_DD0(): pass

    label("Function_6_DD0")

    OP_24(0x85, 0x5A)
    Sleep(100)
    OP_24(0x85, 0x50)
    Sleep(100)
    OP_24(0x85, 0x46)
    Sleep(100)
    OP_24(0x85, 0x3C)
    Sleep(100)
    OP_24(0x85, 0x32)
    Sleep(100)
    OP_24(0x85, 0x28)
    Sleep(100)
    OP_24(0x85, 0x1E)
    Sleep(100)
    OP_24(0x85, 0x14)
    Sleep(100)
    OP_24(0x85, 0xA)
    Sleep(100)
    OP_24(0x85, 0x0)
    OP_23(0x85)
    Return()

    # Function_6_DD0 end

    def Function_7_E29(): pass

    label("Function_7_E29")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x124, -1000, 0, 43070, 0)
    SetChrPos(0x10, -1170, 1500, 85080, 0)
    SetChrPos(0x11, 70, 1500, 84280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_6D(-1000, 0, 50840, 0)
    OP_67(0, 7100, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(429, 0)

    def lambda_EB5():
        OP_6D(-1000, 1500, 87960, 5000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_EB5)

    def lambda_ECD():
        OP_67(0, 6100, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_ECD)

    def lambda_EE5():
        OP_6B(3820, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_EE5)

    def lambda_EF5():
        OP_6E(500, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_EF5)

    def lambda_F05():
        OP_8F(0xFE, 0xFFFFFC18, 0x0, 0x130C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x124, 0, lambda_F05)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x10, 0x0)
    Sleep(1000)

    def lambda_F34():
        OP_6D(-1000, 1500, 83010, 5000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_F34)

    def lambda_F4C():
        OP_67(0, 3250, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F4C)

    def lambda_F64():
        OP_6B(2380, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_F64)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x124, 0x0)
    Fade(500)
    OP_71(0x404, 0x0)
    ExitThread()
    OP_79(0x9, 0x2)
    OP_7B()
    OP_6D(830, 420, 83300, 0)
    OP_67(0, 4650, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(386, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x10, 180, 400)
    Sleep(100)
    OP_8C(0x11, 180, 400)
    Sleep(500)

    ChrTalk(    #11
        0x11,
        "#850F#2P呀，莱维。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        "#1150F完全休息好了么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x124,
        (
            "#120F啊啊……\x02\x03",

            "好了，说说现在的状况吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#1150F呵呵呵……完全超越了希望值。\x02\x03",

            "『环』引发的现象，\x01",
            "使王国陷入了一片混乱之中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#850F#2P结合时机\x01",
            "还投降了大量的人形兵器。\x02\x03",

            "暂时，王国军的家伙们\x01",
            "应该无法采取任何有组织的行动。\x02\x03",

            "当然，那个麻烦的\x01",
            "卡西乌斯·布莱特也一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x124,
        (
            "#120F很顺利啊。\x02\x03",

            "……约修亚的动向如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#1150F他所乘坐的巡洋舰\x01",
            "刚在瓦雷利亚湖着水。\x02\x03",

            "估计会有所行动，\x01",
            "不过目前还不需要考虑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        (
            "#850F#2P呵呵，到时候就迟了。\x02\x03",

            "因为那个『铁血宰相』\x01",
            "似乎对这次异变\x01",
            "也有极大兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x124,
        (
            "#120F呼……\x01",
            "干嘛说得事不关己似的。\x02\x03",

            "那位大人会知道这个计划，\x01",
            "不都是你做的手脚吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#850F#2P啊哈哈，这可\x01",
            "不能说出来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "#1150F不过，演员越多\x01",
            "舞台越热闹嘛。\x02\x03",

            "……对了，莱维。\x02\x03",

            "其实我来这里，\x01",
            "发现了一个很大的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x124,
        "#120F哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x11,
        (
            "#850F#2P浮游都市的防卫系统……\x02\x03",

            "那东西居然\x01",
            "现在还好好的运作着。\x02\x03",

            "要着陆的话\x01",
            "必须使其失效才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#1150F巨大的『古罗力亚斯』\x01",
            "会遭到系统的集中炮火攻击。\x02\x03",

            "但是，为你开发的\x01",
            "『梦幻曲·德尔基昂』\x01",
            "有可能穿过火线进行攻击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x124,
        (
            "#120F原来如此……\x02\x03",

            "因此才叫我来吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        "#850F#2P有办法吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x124,
        (
            "#120F『盟主』赐予的这把剑……\x02\x03",

            "……世上没有它切不开的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "#850F#2P呵呵，是啊。\x02\x03",

            "这也是以『外』之理\x01",
            "制造的东西吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#1150F『德尔基昂』\x01",
            "已经在甲板待机了。\x02\x03",

            "去吧，驾着那黑色的野兽\x01",
            "推开传说之门扉吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x124, 180, 400)
    Fade(500)
    OP_72(0x404, 0x0)
    ExitThread()
    OP_79(0x9, 0x1)
    OP_7B()
    OP_6D(-970, -1500, 81290, 0)
    OP_67(0, 3720, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(0, 0)
    OP_6E(542, 0)

    def lambda_1555():
        OP_8F(0xFE, 0xFFFFFC54, 0x0, 0xF83E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x124, 0, lambda_1555)
    OP_0D()
    Sleep(500)

    def lambda_1576():
        OP_6D(-1000, 11000, 85270, 7000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1576)
    WaitChrThread(0x10, 0x0)
    OP_44(0x124, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/C5408   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_E29 end

    def Function_8_15A9(): pass

    label("Function_8_15A9")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-980, 0, 56040, 0)
    SetChrPos(0x3, -920, 0, 55420, 0)
    SetChrPos(0x2, -1670, 0, 56080, 0)
    SetChrPos(0x1, -310, 0, 56080, 0)
    SetChrPos(0x0, -980, 0, 56670, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 12)
    Call(0, 13)
    Fade(500)
    OP_6D(-960, 0, 58290, 0)
    SetChrPos(0x0, -960, 0, 58290, 0)
    SetChrPos(0x1, -960, 0, 58290, 0)
    SetChrPos(0x2, -960, 0, 58290, 0)
    SetChrPos(0x3, -960, 0, 58290, 0)
    EventEnd(0x0)
    Return()

    # Function_8_15A9 end

    def Function_9_16A4(): pass

    label("Function_9_16A4")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-960, 0, 78190, 0)
    SetChrPos(0x3, -960, 0, 78810, 180)
    SetChrPos(0x2, -350, 0, 78190, 180)
    SetChrPos(0x1, -1580, 0, 78190, 180)
    SetChrPos(0x0, -960, 0, 77580, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 12)
    Call(0, 13)
    Fade(500)
    OP_6D(-960, 0, 75810, 0)
    SetChrPos(0x0, -960, 0, 75810, 180)
    SetChrPos(0x1, -960, 0, 75810, 180)
    SetChrPos(0x2, -960, 0, 75810, 180)
    SetChrPos(0x3, -960, 0, 75810, 180)
    EventEnd(0x0)
    Return()

    # Function_9_16A4 end

    def Function_10_179F(): pass

    label("Function_10_179F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-980, 0, 56040, 0)
    SetChrPos(0x0, -920, 0, 55420, 180)
    SetChrPos(0x1, -1670, 0, 56080, 180)
    SetChrPos(0x2, -310, 0, 56080, 180)
    SetChrPos(0x3, -980, 0, 56670, 180)
    OP_0D()
    Call(0, 12)
    Call(0, 14)
    NewScene("ED6_DT21/C5313   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_10_179F end

    def Function_11_1817(): pass

    label("Function_11_1817")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-1000, 0, 79150, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(0, 0)
    OP_6E(402, 0)
    SetChrPos(0x3, -960, 0, 78810, 180)
    SetChrPos(0x2, -350, 0, 78190, 180)
    SetChrPos(0x1, -1580, 0, 78190, 180)
    SetChrPos(0x0, -960, 0, 77580, 180)
    OP_0D()
    Call(0, 12)
    Call(0, 14)
    NewScene("ED6_DT21/C4103   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1817 end

    def Function_12_18BB(): pass

    label("Function_12_18BB")

    LoadEffect(0x0, "map\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_12_18BB end

    def Function_13_19AD(): pass

    label("Function_13_19AD")


    def lambda_19B3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_19B3)

    def lambda_19C5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_19C5)

    def lambda_19D7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_19D7)

    def lambda_19E9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_19E9)
    Sleep(2500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A11")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1A11")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A28")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1A28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A3F")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1A3F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A56")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1A56")

    Return()

    # Function_13_19AD end

    def Function_14_1A57(): pass

    label("Function_14_1A57")


    def lambda_1A5D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1A5D)

    def lambda_1A6F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1A6F)

    def lambda_1A81():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1A81)

    def lambda_1A93():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1A93)
    Sleep(2000)
    Return()

    # Function_14_1A57 end

    SaveToFile()

Try(main)
