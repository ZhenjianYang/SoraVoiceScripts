from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4168   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4168.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        ' ',                                    # 9
        ' ',                                    # 10
        ' ',                                    # 11
        ' ',                                    # 12
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -15730,
        Y                   = -1000,
        Z                   = -18230,
        Range               = -26740,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xFFFFD6B6,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -19450,
        TriggerZ            = 0,
        TriggerY            = -15500,
        TriggerRange        = 1000,
        ActorX              = -20540,
        ActorZ              = -500,
        ActorY              = -17840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20540,
        TriggerZ            = -700,
        TriggerY            = -17840,
        TriggerRange        = 1000,
        ActorX              = -19600,
        ActorZ              = 500,
        ActorY              = -14960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_192",          # 00, 0
        "Function_1_193",          # 01, 1
        "Function_2_1B0",          # 02, 2
        "Function_3_1B7",          # 03, 3
        "Function_4_AE5",          # 04, 4
        "Function_5_B4C",          # 05, 5
        "Function_6_B89",          # 06, 6
        "Function_7_BF5",          # 07, 7
        "Function_8_CD9",          # 08, 8
        "Function_9_D31",          # 09, 9
        "Function_10_D7B",         # 0A, 10
        "Function_11_DB7",         # 0B, 11
        "Function_12_DE5",         # 0C, 12
        "Function_13_EC9",         # 0D, 13
        "Function_14_F21",         # 0E, 14
        "Function_15_F6B",         # 0F, 15
        "Function_16_FA7",         # 10, 16
    )


    def Function_0_192(): pass

    label("Function_0_192")

    Return()

    # Function_0_192 end

    def Function_1_193(): pass

    label("Function_1_193")

    OP_16(0x2, 0xFA0, 0xFFFE3AE0, 0xFFFE69C0, 0x23006D)
    OP_22(0x1C5, 0x1, 0x64)
    OP_1C(0x1, 0x0, 0x2)
    Return()

    # Function_1_193 end

    def Function_2_1B0(): pass

    label("Function_2_1B0")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_2_1B0 end

    def Function_3_1B7(): pass

    label("Function_3_1B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C7")
    Return()

    label("loc_1C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D9")
    Return()

    label("loc_1D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 1)), scpexpr(EXPR_END)), "loc_1E1")
    Return()

    label("loc_1E1")

    EventBegin(0x0)
    Fade(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23D")
    SetChrPos(0x109, -18500, 0, -12300, 180)
    SetChrPos(0x10F, -19930, 0, -12100, 180)
    SetChrPos(0x10B, -18970, 0, -14180, 180)
    SetChrPos(0x102, -20120, 0, -13800, 180)
    Jump("loc_2C2")

    label("loc_23D")

    SetChrPos(0x109, -18790, 0, -12570, 180)
    SetChrPos(0x10F, -17690, 0, -11000, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_292")
    SetChrPos(0x10B, -18970, 0, -14180, 180)
    SetChrPos(0xF1, -19380, 0, -10920, 180)
    Jump("loc_2C2")

    label("loc_292")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2")
    SetChrPos(0x10B, -18970, 0, -14180, 180)
    SetChrPos(0xF0, -19380, 0, -10920, 180)

    label("loc_2C2")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(-21040, 0, -16650, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(224000, 0)
    OP_6E(362, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x10B,
        (
            "#213F#6P在、在这种地方……\x02\x03",

            "#215F是不是吉尔哥\x01",
            "让它紧急着陆了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45B")

    ChrTalk(    #1
        0x102,
        (
            "#1513F#12P的确……\x01",
            "如果是吉尔的话\x01",
            "应该能够顺利办到吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    Sleep(300)

    ChrTalk(    #2
        0x102,
        (
            "#1500F#11P……怎么样？\x01",
            "要不要一起进去看看呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10B, 270, 400)
    Sleep(300)

    ChrTalk(    #3
        0x10B,
        (
            "#210F#6P啊，嗯……\x01",
            "可以的话就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F2")

    label("loc_45B")


    ChrTalk(    #4
        0x109,
        (
            "#1065F#6P嗯……\x01",
            "也有这种可能性吧。\x02\x03",

            "#1060F怎么办？\x01",
            "要进去确认一下吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10B, 0, 400)
    Sleep(300)

    ChrTalk(    #5
        0x10B,
        (
            "#210F#5P……嗯。\x01",
            "那好吧。\x02",
        )
    )

    Jump("loc_4F1")

    label("loc_4F1")

    CloseMessageWindow()

    label("loc_4F2")

    Sleep(300)

    def lambda_4FD():
        OP_6D(-22370, 0, -23640, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4FD)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_573")
    SetChrPos(0x109, -18920, 0, -14160, 180)
    SetChrPos(0x10F, -17790, 0, -12650, 180)
    SetChrPos(0x10B, -23540, -610, -23920, 0)
    SetChrPos(0x102, -23540, -610, -23920, 0)
    Jump("loc_5F8")

    label("loc_573")

    SetChrPos(0x109, -18920, 0, -14160, 180)
    SetChrPos(0x10F, -17790, 0, -12650, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C8")
    SetChrPos(0x10B, -23540, -610, -23920, 0)
    SetChrPos(0xF1, -19650, 0, -13060, 180)
    Jump("loc_5F8")

    label("loc_5C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F8")
    SetChrPos(0x10B, -23540, -610, -23920, 0)
    SetChrPos(0xF0, -19650, 0, -13060, 180)

    label("loc_5F8")

    OP_6D(-23270, -610, -24000, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(3410, 0)
    OP_6C(224000, 0)
    OP_6E(273, 0)
    Sleep(1500)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B0")

    def lambda_673():
        OP_6D(-20010, 0, -17300, 4500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_673)

    def lambda_68B():
        OP_6B(3260, 4500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_68B)
    OP_43(0x10B, 0x0, 0x0, 0x5)
    OP_43(0x102, 0x0, 0x0, 0x6)
    WaitChrThread(0x10B, 0x0)
    WaitChrThread(0x102, 0x0)
    Jump("loc_6E4")

    label("loc_6B0")


    def lambda_6B6():
        OP_6D(-21170, -750, -17200, 4500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6B6)

    def lambda_6CE():
        OP_6B(3260, 4500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6CE)
    OP_43(0x10B, 0x0, 0x0, 0x4)
    WaitChrThread(0x10B, 0x0)

    label("loc_6E4")

    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #6
        0x10B,
        "#413F#5P……久等了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B2")

    ChrTalk(    #7
        0x109,
        (
            "#1067F#6P啊啊……\x01",
            "已经可以了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10B,
        (
            "#215F#5P嗯……\x01",
            "我终于亲眼见到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#1503F#5P……山猫号的引擎\x01",
            "也完全无法发动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_839")

    label("loc_7B2")


    ChrTalk(    #10
        0x109,
        (
            "#1067F#6P啊啊……\x01",
            "已经可以了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10B,
        (
            "#215F#5P嗯……\x01",
            "我终于亲眼见到了。\x02\x03",

            "山猫号的引擎\x01",
            "也不知为何无法发动……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_839")


    ChrTalk(    #12
        0x109,
        "#1841F#6P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10F,
        (
            "#1446F#12P……现在我们只有继续前进了。\x02\x03",

            "#1448F这样的话，\x01",
            "一定能受到女神的指引的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10B,
        (
            "#210F#5P嗯……好吧。\x02\x03",

            "#211F……好，\x01",
            "那就赶快把哥哥们救出来，\x01",
            "让他们好好感谢我才行！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_951")

    ChrTalk(    #15
        0x102,
        "#1514F#5P乔丝特……\x02",
    )

    CloseMessageWindow()

    label("loc_951")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_98F")

    ChrTalk(    #16
        0x107,
        (
            "#067F#12P嘿嘿……\x01",
            "就是这股气势。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A06")

    label("loc_98F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9CC")

    ChrTalk(    #17
        0x10E,
        "#179F#12P哈哈……这种精神不错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A06")

    label("loc_9CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A06")

    ChrTalk(    #18
        0x10D,
        "#278F#12P呵……这种精神还不错。\x02",
    )

    CloseMessageWindow()

    label("loc_A06")

    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-18680, 0, -12910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -18680, 0, -12910, 0)
    SetChrPos(0x1, -18680, 0, -12910, 0)
    SetChrPos(0x2, -18680, 0, -12910, 0)
    SetChrPos(0x3, -18680, 0, -12910, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2711)
    OP_28(0x2C, 0x1, 0x100)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_3_1B7 end

    def Function_4_AE5(): pass

    label("Function_4_AE5")


    def lambda_AEB():
        OP_8E(0xFE, 0xFFFFA592, 0xFFFFFD9E, 0xFFFFAC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AEB)
    Sleep(500)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x1, 89)
    OP_70(0x1, 0x0)
    WaitChrThread(0xFE, 0x1)
    OP_8E(0xFE, 0xFFFFAFEC, 0xFFFFFF9C, 0xFFFFABA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB064, 0xFFFFFCA4, 0xFFFFB78A, 0x7D0, 0x0)
    OP_71(0x1001, 0x0)
    ExitThread()
    Return()

    # Function_4_AE5 end

    def Function_5_B4C(): pass

    label("Function_5_B4C")

    OP_8E(0xFE, 0xFFFFA592, 0xFFFFFD9E, 0xFFFFAC18, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFAFEC, 0xFFFFFF9C, 0xFFFFABA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB064, 0xFFFFFCA4, 0xFFFFB78A, 0x7D0, 0x0)
    Return()

    # Function_5_B4C end

    def Function_6_B89(): pass

    label("Function_6_B89")

    Sleep(700)

    def lambda_B94():
        OP_8E(0xFE, 0xFFFFA592, 0xFFFFFD9E, 0xFFFFAC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B94)
    Sleep(500)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x1, 89)
    OP_70(0x1, 0x0)
    WaitChrThread(0xFE, 0x1)
    OP_8E(0xFE, 0xFFFFAFEC, 0xFFFFFF9C, 0xFFFFABA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB262, 0xFFFFFDD0, 0xFFFFB3C0, 0x7D0, 0x0)
    OP_71(0x1001, 0x0)
    ExitThread()
    Return()

    # Function_6_B89 end

    def Function_7_BF5(): pass

    label("Function_7_BF5")

    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0xB)
    OP_43(0x1, 0x1, 0x0, 0xA)
    OP_43(0x2, 0x1, 0x0, 0x9)
    OP_43(0x3, 0x1, 0x0, 0x8)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_7_BF5 end

    def Function_8_CD9(): pass

    label("Function_8_CD9")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_CD9 end

    def Function_9_D31(): pass

    label("Function_9_D31")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_D31 end

    def Function_10_D7B(): pass

    label("Function_10_D7B")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_D7B end

    def Function_11_DB7(): pass

    label("Function_11_DB7")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_11_DB7 end

    def Function_12_DE5(): pass

    label("Function_12_DE5")

    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0x10)
    OP_43(0x1, 0x1, 0x0, 0xF)
    OP_43(0x2, 0x1, 0x0, 0xE)
    OP_43(0x3, 0x1, 0x0, 0xD)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_12_DE5 end

    def Function_13_EC9(): pass

    label("Function_13_EC9")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_13_EC9 end

    def Function_14_F21(): pass

    label("Function_14_F21")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_14_F21 end

    def Function_15_F6B(): pass

    label("Function_15_F6B")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_15_F6B end

    def Function_16_FA7(): pass

    label("Function_16_FA7")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_16_FA7 end

    SaveToFile()

Try(main)
