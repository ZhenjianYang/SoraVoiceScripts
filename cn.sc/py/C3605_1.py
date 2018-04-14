from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3605_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3605.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C3605_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '',                                     # 8
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_B5",           # 03, 3
        "Function_4_E93",          # 04, 4
        "Function_5_ECD",          # 05, 5
        "Function_6_F07",          # 06, 6
        "Function_7_F65",          # 07, 7
        "Function_8_3DDC",         # 08, 8
        "Function_9_3DE6",         # 09, 9
        "Function_10_3E33",        # 0A, 10
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    Call(1, 3)
    Call(1, 7)
    Return()

    # Function_2_AC end

    def Function_3_B5(): pass

    label("Function_3_B5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC")
    Call(0, 5)
    Call(0, 6)

    label("loc_CC")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_E9"),
        (5, "loc_100"),
        (4, "loc_117"),
        (6, "loc_12E"),
        (8, "loc_145"),
        (SWITCH_DEFAULT, "loc_15C"),
    )


    label("loc_E9")

    OP_D2(0x701D0, 0x701DC, 0x12)
    OP_D2(0x701D1, 0x701DD, 0x13)
    Jump("loc_15C")

    label("loc_100")

    OP_D2(0x70218, 0x70224, 0x12)
    OP_D2(0x70219, 0x70225, 0x13)
    Jump("loc_15C")

    label("loc_117")

    OP_D2(0x70200, 0x7020C, 0x12)
    OP_D2(0x70201, 0x7020D, 0x13)
    Jump("loc_15C")

    label("loc_12E")

    OP_D2(0x70230, 0x7023C, 0x12)
    OP_D2(0x70231, 0x7023D, 0x13)
    Jump("loc_15C")

    label("loc_145")

    OP_D2(0x270176, 0x270183, 0x12)
    OP_D2(0x270177, 0x270184, 0x13)
    Jump("loc_15C")

    label("loc_15C")

    OP_D2(0x26019C, 0x2601A1, 0x14)
    OP_D2(0x2600A0, 0x2600A5, 0x15)
    OP_D2(0x260052, 0x260057, 0x16)
    OP_D2(0x29014C, 0x290150, 0x17)
    OP_D2(0x29014D, 0x290151, 0x18)
    OP_6D(-3550, 13000, -1710, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(307000, 0)
    OP_6E(282, 0)
    SetChrPos(0x8, -1150, 950, 12410, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 20)
    OP_71(0x5, 0x4)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_70(0x0, 0x8)
    OP_70(0x1, 0x8)
    OP_70(0x2, 0x8)
    OP_70(0x3, 0x8)
    OP_70(0x4, 0x8)
    LoadEffect(0x0, "map\\\\mp061_00.eff")
    LoadEffect(0x1, "Scraft\\\\sc005_03.eff")
    LoadEffect(0x2, "scraft\\\\sc000_11.eff")
    LoadEffect(0x3, "battle\\\\btbomb00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x101, 740, -1750, -7480, 0)
    SetChrPos(0x102, -650, -1750, -7480, 0)
    SetChrPos(0xF9, 820, -1750, -7480, 0)
    SetChrPos(0x108, -750, -1750, -7480, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_71(0xC, 0x4)
    FadeToBright(2000, 0)

    def lambda_335():
        OP_6D(-550, 0, -1710, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_335)

    def lambda_34D():
        OP_67(0, 8480, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34D)

    def lambda_365():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_365)

    def lambda_375():
        OP_6C(320000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_375)

    def lambda_385():
        OP_6E(282, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_385)
    Sleep(4000)
    ClearChrFlags(0x101, 0x80)

    def lambda_39F():
        OP_8E(0xFE, 0x2E4, 0x0, 0xFFFFF808, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39F)
    Sleep(100)
    ClearChrFlags(0x102, 0x80)

    def lambda_3C4():
        OP_8E(0xFE, 0xFFFFFD76, 0x0, 0xFFFFF827, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C4)
    Sleep(800)
    ClearChrFlags(0xF9, 0x80)

    def lambda_3E9():
        OP_8E(0xFE, 0x334, 0x0, 0xFFFFF240, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3E9)
    Sleep(100)
    ClearChrFlags(0x108, 0x80)

    def lambda_40E():
        OP_8E(0xFE, 0xFFFFFD12, 0x0, 0xFFFFF1FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_40E)
    WaitChrThread(0x108, 0x1)
    Sleep(500)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #0
        0x101,
        "#1007F#6P终、终于到了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#1043F#6P比想象的\x01",
            "还要花时间啊……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x8,
        "男人的声音",
        (
            "#3P呼呼……\x01",
            "就知道你们差不多该来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_529")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_567")

    label("loc_529")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_550")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_567")

    label("loc_550")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_567")

    Sleep(1000)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_579():
        OP_6D(-1310, 950, 13270, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_579)

    def lambda_591():
        OP_67(0, 6500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_591)

    def lambda_5A9():
        OP_6E(307, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5A9)
    WaitChrThread(0x101, 0x3)
    SetChrPos(0x108, 740, -1750, -7480, 0)
    SetChrPos(0x102, -650, -1750, -7480, 0)
    SetChrPos(0x101, 820, -1750, -7480, 0)
    SetChrPos(0xF9, -750, -1750, -7480, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 12)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 18)

    def lambda_62A():
        OP_8F(0xFE, 0xFFFFFE3E, 0x0, 0x1388, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_62A)
    Sleep(300)

    def lambda_64A():
        OP_8F(0xFE, 0x29E, 0x0, 0xED8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64A)
    Sleep(200)

    def lambda_66A():
        OP_8F(0xFE, 0xFFFFFB5A, 0x0, 0xF3C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66A)
    Sleep(300)

    def lambda_68A():
        OP_8F(0xFE, 0x64, 0x0, 0x834, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_68A)
    Fade(500)
    OP_6D(-1490, 1000, 9000, 0)
    OP_67(0, 3640, -10000, 0)
    OP_6B(3640, 0)
    OP_6C(333000, 0)
    OP_6E(293, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #3
        0x108,
        "#072F#6P瓦鲁特……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#250F#2P金……\x01",
            "你果然来了吗。\x02\x03",

            "还有『漆黑』小子。\x01",
            "好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#1035F#6P……是啊。\x02\x03",

            "#1042F不过，还真不知道\x01",
            "你和金先生竟然是同门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#252F#2P呼呼，俺除了『泰斗流』以外\x01",
            "还吸收了各种各样的流派。\x02\x03",

            "一切都是为了要达到\x01",
            "可以击败任何人的至高境地。\x02\x03",

            "你没注意到也不足为怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x108,
        "#572F#6P瓦鲁特，你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#250F#2P你又怎样……金？\x02\x03",

            "至今还死抱着『泰斗流』之类\x01",
            "老掉牙的流派不放吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x108,
        (
            "#074F#6P……因为我就是这么笨。\x02\x03",

            "#070F光是学习本门的武术就已经需要竭尽全力了，\x01",
            "没有多余的时间去关注其他的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#254F#2P啧……真没意思。\x02\x03",

            "#252F算了，我从刚才\x01",
            "就一直很无聊。\x02\x03",

            "干脆就在这里\x01",
            "做个了结吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x0, 0x2, 0x5DC)
    Sleep(1000)
    OP_99(0x8, 0x3, 0x9, 0x5DC)
    Sleep(200)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 2)
    Sleep(200)
    OP_99(0x8, 0x1, 0x2, 0x3E8)
    OP_22(0xBC, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_9A8():
        OP_6D(-930, 1000, 5500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9A8)

    def lambda_9C0():
        OP_67(0, 4160, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9C0)

    def lambda_9D8():
        OP_6B(3690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9D8)

    def lambda_9E8():
        OP_6E(293, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9E8)
    SetChrPos(0xA, 12740, 250, 9670, 270)
    SetChrPos(0xB, -13570, 250, 6260, 90)
    SetChrPos(0xC, 9220, 250, -3940, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x800)
    OP_43(0xA, 0x3, 0x0, 0x2)
    OP_43(0xB, 0x3, 0x0, 0x2)
    OP_43(0xC, 0x3, 0x0, 0x2)
    OP_43(0xA, 0x2, 0x1, 0x4)
    Sleep(100)
    OP_43(0xB, 0x2, 0x1, 0x5)
    Sleep(100)
    OP_43(0xC, 0x2, 0x1, 0x6)
    Sleep(500)
    SetChrSubChip(0x8, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE8")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B26")

    label("loc_AE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0F")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B26")

    label("loc_B0F")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B26")

    Sleep(1000)

    def lambda_B31():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B31)
    Sleep(50)

    def lambda_B44():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B44)
    Sleep(50)
    OP_8C(0xF9, 180, 400)
    WaitChrThread(0xA, 0x2)
    WaitChrThread(0xB, 0x2)
    WaitChrThread(0xC, 0x2)

    ChrTalk(    #11
        0x101,
        "#1020F#5P哇哇……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#1042F#6P『装甲猎豹』……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCE")

    ChrTalk(    #13
        0x106,
        "#054F#2P结社的装甲兽啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C88")

    label("loc_BCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFF")

    ChrTalk(    #14
        0x103,
        "#024F#2P结社的装甲兽……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C88")

    label("loc_BFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2A")

    ChrTalk(    #15
        0x107,
        "#065F#2P啊哇哇……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C88")

    label("loc_C2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5B")

    ChrTalk(    #16
        0x105,
        "#042F#2P结社的装甲兽……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C88")

    label("loc_C5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C88")

    ChrTalk(    #17
        0x109,
        "#1069F#5P结社的装甲兽吗！\x02",
    )

    CloseMessageWindow()

    label("loc_C88")


    ChrTalk(    #18
        0x8,
        (
            "#250F呼呼，小子们，\x01",
            "就和这些家伙玩玩吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-1040, 1200, 9600, 0)
    OP_67(0, 3100, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(356000, 0)
    OP_6E(240, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #19
        0x8,
        (
            "#252F金……让我见识一下吧。\x02\x03",

            "这六年时间内\x01",
            "你所练就的功夫！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x108,
        "#072F#6P……如你所愿！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 22)
    SetChrSubChip(0x8, 1)
    OP_0D()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_D88():
        OP_6D(-800, 950, 6000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D88)

    def lambda_DA0():
        OP_67(0, 3960, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA0)

    def lambda_DB8():
        OP_6B(3300, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DB8)
    SetChrSubChip(0x8, 2)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_DDA():
        OP_96(0xFE, 0xFFFFFE20, 0x0, 0x1694, 0x7D0, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_DDA)
    Sleep(100)
    SetChrChipByIndex(0xA, 24)

    def lambda_E02():
        OP_8E(0xFE, 0x2F8, 0x0, 0xEA6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_E02)
    SetChrChipByIndex(0xB, 24)

    def lambda_E22():
        OP_8E(0xFE, 0xFFFFFAC4, 0x0, 0xFBE, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_E22)
    SetChrChipByIndex(0xC, 24)

    def lambda_E42():
        OP_8E(0xFE, 0xFFFFFF10, 0x0, 0x9A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_E42)
    WaitChrThread(0x101, 0x0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x455, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_E8D"),
        (SWITCH_DEFAULT, "loc_E92"),
    )


    label("loc_E8D")

    OP_B4(0x0)
    Jump("loc_E92")

    label("loc_E92")

    Return()

    # Function_3_B5 end

    def Function_4_E93(): pass

    label("Function_4_E93")

    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x2968, 0xFA, 0x1360, 0x1770, 0x0)
    OP_8E(0xFE, 0x17B6, 0xFA, 0x114E, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 23)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_4_E93 end

    def Function_5_ECD(): pass

    label("Function_5_ECD")

    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0xFFFFD972, 0xFA, 0xC80, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFE7BE, 0xFA, 0x13CE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 23)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_ECD end

    def Function_6_F07(): pass

    label("Function_6_F07")

    SetChrChipByIndex(0xFE, 24)
    SetChrFlags(0xFE, 0x4)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0x13E2, 0x1360, 0xFFFFE610, 0x1388, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0xFFFFFF92, 0x0, 0xFFFFF330, 0x7D0, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 23)
    ClearChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_F07 end

    def Function_7_F65(): pass

    label("Function_7_F65")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x8, 0x0)
    OP_44(0xB, 0x0)
    OP_44(0xC, 0x0)
    OP_44(0xC, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_FB5"),
        (5, "loc_FCC"),
        (4, "loc_FE3"),
        (6, "loc_FFA"),
        (8, "loc_1011"),
        (SWITCH_DEFAULT, "loc_1028"),
    )


    label("loc_FB5")

    OP_D2(0x701D0, 0x701DC, 0x12)
    OP_D2(0x701D1, 0x701DD, 0x13)
    Jump("loc_1028")

    label("loc_FCC")

    OP_D2(0x70218, 0x70224, 0x12)
    OP_D2(0x70219, 0x70225, 0x13)
    Jump("loc_1028")

    label("loc_FE3")

    OP_D2(0x70200, 0x7020C, 0x12)
    OP_D2(0x70201, 0x7020D, 0x13)
    Jump("loc_1028")

    label("loc_FFA")

    OP_D2(0x70230, 0x7023C, 0x12)
    OP_D2(0x70231, 0x7023D, 0x13)
    Jump("loc_1028")

    label("loc_1011")

    OP_D2(0x270176, 0x270183, 0x12)
    OP_D2(0x270177, 0x270184, 0x13)
    Jump("loc_1028")

    label("loc_1028")

    OP_D2(0x26019C, 0x2601A1, 0x14)
    OP_D2(0x2600A0, 0x2600A5, 0x15)
    OP_D2(0x260052, 0x260057, 0x16)
    OP_D2(0x70251, 0x7025D, 0x17)
    OP_D2(0x7024D, 0x70259, 0x18)
    OP_D2(0x2601A7, 0x2601AC, 0x19)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 12)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 18)
    SetChrPos(0x108, 40, 0, 5100, 0)
    SetChrPos(0x101, 210, 0, 3200, 0)
    SetChrPos(0x102, 1130, 0, 2410, 0)
    SetChrPos(0xF9, -530, 0, 1460, 0)
    SetChrPos(0x8, 50, 0, 10340, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)
    OP_71(0x5, 0x4)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_70(0x0, 0x8)
    OP_70(0x1, 0x8)
    OP_70(0x2, 0x8)
    OP_70(0x3, 0x8)
    OP_70(0x4, 0x8)
    LoadEffect(0x0, "map\\\\mp061_00.eff")
    LoadEffect(0x1, "scraft\\sc007_10.eff")
    LoadEffect(0x2, "scraft\\\\sc000_11.eff")
    LoadEffect(0x3, "battle\\\\btbomb00.eff")
    LoadEffect(0x4, "scraft\\\\sc000_10.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_6D(1110, 0, 8260, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(344, 0)
    OP_71(0xC, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #21
        0x101,
        "#1002F#6P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        "#1043F#4P果然棘手……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(0, 0, 8800, 0)
    OP_67(0, 4720, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(0, 0)
    OP_6E(287, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x8,
        (
            "#250F……看来功夫还是\x01",
            "练得相当过硬啊。\x02\x03",

            "#252F只是，动作太过死板。\x02\x03",

            "这是你守着陈旧的\x01",
            "『泰斗流』而固步自封的结果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x108,
        "#070F#6P呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "#254F……有什么好笑？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x108,
        (
            "#074F#6P你确实是个天才\x01",
            "但却不明白最重要的事。\x02\x03",

            "师父想必也相当遗憾吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#254F嗬……\x02\x03",

            "你打算代替老头子\x01",
            "向我说教吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x108,
        (
            "#070F#6P我才没\x01",
            "那么狂妄呢。\x02\x03",

            "#074F然而，拳脚相交之间\x01",
            "我明白了一件事。\x02\x03",

            "现在的我，可能\x01",
            "难以胜过你……\x02\x03",

            "#072F但也不会输给你。\x02\x03",

            "你的拳头是打不倒我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#254F…………………………………\x02\x03",

            "#251F呼呼……有意思。\x02\x03",

            "没想到会从你的口中\x01",
            "说出这种的话来。\x02\x03",

            "原本只是想打发打发时间，\x01",
            "不过我改变主意了。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    Fade(500)
    SetChrSubChip(0x8, 0)
    OP_0D()
    SetChrChipByIndex(0x8, 25)
    OP_99(0x8, 0x0, 0x2, 0x3E8)
    Sleep(500)

    def lambda_1524():
        OP_6B(3400, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1524)
    PlayEffect(0x1, 0x1, 0x8, -100, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(    #30
        0x8,
        (
            "#254F来吧，金……\x02\x03",

            "我要让你体会到\x01",
            "什么叫实力的差距……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x108,
        "#072F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)
    OP_0D()
    Sleep(500)
    PlayEffect(0x1, 0x2, 0x108, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(    #32
        0x101,
        "#1020F（怎、怎么办！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#1042F#4P（这……\x01",
            "看来插不进手啊。）\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    OP_1D(0x2C)
    Sleep(500)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x108, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x108, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x108, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_16BE():
        OP_6B(2500, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16BE)

    def lambda_16CE():
        OP_6C(12000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16CE)

    def lambda_16DE():
        OP_6D(0, 500, 9500, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_16DE)

    def lambda_16F6():

        label("loc_16F6")

        TurnDirection(0xFE, 0x108, 400)
        OP_48()
        Jump("loc_16F6")

    QueueWorkItem2(0x101, 3, lambda_16F6)

    def lambda_1707():

        label("loc_1707")

        TurnDirection(0xFE, 0x108, 400)
        OP_48()
        Jump("loc_1707")

    QueueWorkItem2(0x102, 3, lambda_1707)

    def lambda_1718():

        label("loc_1718")

        TurnDirection(0xFE, 0x108, 400)
        OP_48()
        Jump("loc_1718")

    QueueWorkItem2(0xF9, 3, lambda_1718)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x108, 0x40)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x108, 0x1000)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_175B():
        OP_99(0xFE, 0x0, 0x1, 0x640)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_175B)

    def lambda_176B():
        OP_8F(0xFE, 0x28, 0x0, 0x2706, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_176B)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_1790():
        OP_99(0xFE, 0x0, 0x4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1790)
    OP_8F(0x108, 0x28, 0x0, 0x23BE, 0x2EE0, 0x0)

    def lambda_17B4():

        label("loc_17B4")

        OP_9E(0xFE, 0x14, 0x0, 0x1388, 0x9C4)
        OP_48()
        Jump("loc_17B4")

    QueueWorkItem2(0x8, 3, lambda_17B4)

    def lambda_17D1():

        label("loc_17D1")

        OP_9E(0xFE, 0x14, 0x0, 0x1388, 0x9C4)
        OP_48()
        Jump("loc_17D1")

    QueueWorkItem2(0x108, 3, lambda_17D1)
    PlayEffect(0x4, 0xFF, 0x8, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0x190, 0xBB8, 0x12C)
    Sleep(500)
    OP_44(0x8, 0x3)
    OP_44(0x108, 0x3)

    def lambda_1841():
        OP_6C(24000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1841)

    def lambda_1851():
        OP_96(0xFE, 0x910, 0xFA, 0x286E, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1851)

    def lambda_186F():
        OP_96(0xFE, 0xFFFFF6F0, 0xFA, 0x286E, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_186F)
    WaitChrThread(0x108, 0x1)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x108, 14)
    SetChrSubChip(0x108, 0)
    OP_8C(0x8, 270, 0)
    OP_8C(0x108, 90, 0)

    def lambda_18B4():
        OP_6D(-8380, 250, 9110, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18B4)

    def lambda_18CC():
        OP_6B(2820, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_18CC)
    SetChrPos(0x101, 300, 0, 2110, 0)
    SetChrPos(0x102, 930, 0, 1470, 0)
    SetChrPos(0xF9, -810, 0, 1110, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF9, 0)
    OP_96(0x108, 0xFFFFDB02, 0xFA, 0x2378, 0x1F4, 0x1F40)
    OP_96(0x8, 0xFFFFDEEA, 0xFA, 0x2364, 0x1F4, 0x1F40)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_1965():
        OP_99(0xFE, 0x0, 0xD, 0x640)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1965)
    SetChrChipByIndex(0x108, 14)
    SetChrSubChip(0x108, 0)
    Sleep(200)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x8, 0, 800, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_19BE():

        label("loc_19BE")

        OP_9E(0xFE, 0x1E, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_19BE")

    QueueWorkItem2(0x108, 1, lambda_19BE)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x8, 0, 800, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)

    def lambda_1A3C():
        OP_96(0xFE, 0xFFFFDDA0, 0xFA, 0x2364, 0x12C, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1A3C)
    Sleep(400)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x8, 0, 1058642330, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)
    OP_44(0x108, 0x1)
    SetChrChipByIndex(0x108, 24)
    SetChrSubChip(0x108, 1)
    Sleep(200)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_1AC7():
        OP_91(0xFE, 0xFFFFFCE0, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1AC7)
    WaitChrThread(0x8, 0x1)
    OP_96(0x108, 0xFFFFDEEA, 0xFA, 0x1F90, 0x1F4, 0x1F40)
    TurnDirection(0x108, 0x8, 0)
    TurnDirection(0x8, 0x108, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_1B20():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1B20)
    SetChrSubChip(0x8, 2)
    SetChrChipByIndex(0x8, 25)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x8, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)
    Sleep(100)
    OP_91(0x8, 0x0, 0x0, 0x320, 0x2710, 0x0)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)
    SetChrSubChip(0x8, 3)
    Sleep(300)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)

    def lambda_1BC1():
        OP_96(0xFE, 0xFFFFDB02, 0xFA, 0x209E, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1BC1)
    Sleep(100)

    def lambda_1BE4():
        OP_96(0xFE, 0xFFFFEAA2, 0xFA, 0x209E, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BE4)
    WaitChrThread(0x8, 0x1)

    def lambda_1C07():
        OP_6D(-6390, 250, 2530, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C07)

    def lambda_1C1F():
        OP_6C(48000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x108, 0x1000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 6)

    def lambda_1C43():
        OP_8E(0xFE, 0xFFFFEAA2, 0xFA, 0x1194, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C43)

    def lambda_1C5E():
        OP_8E(0xFE, 0xFFFFDB02, 0xFA, 0x11A8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1C5E)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    TurnDirection(0x108, 0x8, 0)
    TurnDirection(0x8, 0x108, 0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x108, 0x1000)

    def lambda_1CA0():
        OP_96(0xFE, 0xFFFFEAA2, 0xFA, 0x11A8, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1CA0)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_1CC8():
        OP_99(0xFE, 0x0, 0x4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1CC8)
    Sleep(100)
    OP_22(0x208, 0x0, 0x64)

    def lambda_1CE2():
        OP_96(0xFE, 0xFFFFEAA2, 0xFA, 0x1784, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1CE2)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)
    WaitChrThread(0x108, 0x2)
    TurnDirection(0x108, 0x8, 0)
    TurnDirection(0x8, 0x108, 0)

    def lambda_1D22():
        OP_6D(-2380, 250, -860, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D22)
    SetChrFlags(0x108, 0x1000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)

    def lambda_1D49():
        OP_99(0xFE, 0x0, 0xD, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1D49)
    Sleep(500)
    PlayEffect(0x4, 0xFF, 0x108, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x3DCCCCCD, 0xFA0, 0xBB8, 0x64)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 17)

    def lambda_1DAE():
        OP_96(0xFE, 0xFFFFEAA2, 0xFA, 0xFFFFF560, 0x64, 0x3A98)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1DAE)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)

    def lambda_1DE5():
        OP_6C(80000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DE5)

    def lambda_1DF5():
        OP_96(0x8, 0xFFFFEAA2, 0xFA, 0xFFFFF948, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1DF5)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_1E1D():
        OP_99(0xFE, 0x0, 0x2, 0x9C4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E1D)
    OP_22(0x208, 0x0, 0x64)
    OP_96(0x108, 0xFFFFF088, 0xFA, 0xFFFFF948, 0x1F4, 0x1F40)
    TurnDirection(0x108, 0x8, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    TurnDirection(0x8, 0x108, 0)
    OP_8F(0x8, 0xFFFFECA0, 0xFA, 0xFFFFF948, 0x2710, 0x0)
    OP_96(0x108, 0xFFFFFC40, 0xFA, 0xFFFFFD30, 0x1F4, 0x1F40)
    OP_96(0x108, 0x7A8, 0xFA, 0xFFFFF560, 0x1F4, 0x1F40)
    OP_96(0x108, 0xB90, 0xFA, 0xFFFFF948, 0x1F4, 0x1F40)

    def lambda_1EBA():
        OP_6D(10500, 250, -1530, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EBA)
    OP_96(0x8, 0x7A8, 0xFA, 0xFFFFF948, 0x1F4, 0x1B58)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)

    def lambda_1EF3():
        OP_99(0xFE, 0x0, 0xD, 0xDAC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1EF3)
    OP_22(0x208, 0x0, 0x64)
    OP_96(0x108, 0xFFFFF088, 0xFA, 0xFFFFF948, 0x7D0, 0x1F40)
    TurnDirection(0x108, 0x8, 0)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_1F30():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1F30)

    def lambda_1F3E():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1F3E)
    OP_8F(0x108, 0x3C0, 0xFA, 0xFFFFF948, 0x4E20, 0x0)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 15)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 8)
    PlayEffect(0x4, 0xFF, 0x8, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0x190, 0xBB8, 0x64)
    OP_8F(0x8, 0x2300, 0xFA, 0xFFFFF948, 0x55F0, 0x0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_1FE4():
        OP_99(0xFE, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1FE4)

    def lambda_1FF4():
        OP_8F(0xFE, 0x2AD0, 0xFA, 0xFFFFF948, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1FF4)
    Sleep(200)
    OP_22(0x208, 0x0, 0x64)

    def lambda_2019():
        OP_96(0xFE, 0x2300, 0xFA, 0xFFFFF178, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2019)

    def lambda_2037():

        label("loc_2037")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2037")

    QueueWorkItem2(0x8, 2, lambda_2037)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)
    WaitChrThread(0x8, 0x1)

    def lambda_205C():
        OP_6C(128000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_205C)

    def lambda_206C():
        OP_6D(10500, 250, -530, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_206C)
    OP_96(0x8, 0x1F18, 0xFA, 0xFFFFF948, 0x1F4, 0x1F40)
    OP_96(0x8, 0x267A, 0xFA, 0xFFFFF948, 0x1F4, 0x1F40)
    TurnDirection(0x108, 0x8, 0)
    OP_44(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_20C7():
        OP_99(0xFE, 0x0, 0xD, 0x640)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_20C7)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x108, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_212C():

        label("loc_212C")

        OP_9E(0xFE, 0x1E, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_212C")

    QueueWorkItem2(0x108, 1, lambda_212C)
    Sleep(300)

    def lambda_214E():
        OP_99(0xFE, 0x0, 0x2, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_214E)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x108, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)
    Sleep(500)
    SetChrChipByIndex(0x108, 16)
    SetChrSubChip(0x108, 0)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x108, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)
    OP_44(0x108, 0x1)

    def lambda_2207():
        OP_91(0xFE, 0x320, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2207)
    WaitChrThread(0x8, 0x1)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_2240():
        OP_91(0xFE, 0xFFFFFCE0, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2240)
    Sleep(100)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_226A():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_226A)
    Sleep(100)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x8, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)
    Sleep(100)

    def lambda_22CF():
        OP_91(0xFE, 0xFFFFFCE0, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22CF)
    WaitChrThread(0x108, 0x2)

    def lambda_22EF():
        OP_91(0xFE, 0x320, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22EF)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)

    def lambda_2314():
        OP_99(0xFE, 0x0, 0xD, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2314)
    Sleep(400)
    OP_22(0x208, 0x0, 0x64)

    def lambda_232E():
        OP_96(0xFE, 0x267A, 0xFA, 0xFFFFED90, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_232E)
    WaitChrThread(0x108, 0x1)
    TurnDirection(0x108, 0x8, 0)
    WaitChrThread(0x8, 0x2)
    TurnDirection(0x8, 0x108, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)

    def lambda_236E():
        OP_96(0xFE, 0x267A, 0xFA, 0xFFFFF63C, 0x12C, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_236E)
    Sleep(100)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_239B():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_239B)
    Sleep(50)
    OP_22(0x208, 0x0, 0x64)
    Sleep(100)
    OP_96(0x8, 0x267A, 0xFA, 0xFFFFFCC2, 0x1F4, 0x1F40)
    WaitChrThread(0x108, 0x2)

    def lambda_23D6():
        OP_96(0xFE, 0x267A, 0xFA, 0xFFFFFA06, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_23D6)
    Sleep(100)

    def lambda_23F9():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_23F9)
    Sleep(50)
    OP_22(0x208, 0x0, 0x64)
    Sleep(100)
    OP_96(0x8, 0x290E, 0xFA, 0x384, 0x1F4, 0x1F40)

    def lambda_242F():
        OP_6D(8500, 250, 6500, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_242F)
    OP_96(0x8, 0x2832, 0xFA, 0x12D4, 0x1F4, 0x1F40)
    OP_96(0x8, 0x1EDC, 0xFA, 0x22B0, 0x1F4, 0x1F40)
    OP_96(0x108, 0x1E1E, 0xFA, 0x1310, 0x1F4, 0x1F40)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_2496():
        OP_96(0xFE, 0x1EDC, 0xFA, 0x1CD4, 0x1F4, 0x2328)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2496)

    def lambda_24B4():
        OP_96(0xFE, 0x1E1E, 0xFA, 0x18EC, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_24B4)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_24DC():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_24DC)
    Sleep(100)
    WaitChrThread(0x8, 0x1)
    OP_22(0x1FB, 0x0, 0x64)
    SetChrChipByIndex(0x8, 25)
    SetChrSubChip(0x8, 2)
    PlayEffect(0x2, 0xFF, 0x8, 0, 700, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)

    def lambda_254B():
        OP_91(0xFE, 0x0, 0x0, 0x320, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_254B)
    SetChrSubChip(0x8, 3)
    WaitChrThread(0x108, 0x2)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)

    def lambda_2584():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFCE0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2584)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)

    def lambda_25A9():
        OP_99(0xFE, 0x0, 0xD, 0x640)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_25A9)
    Sleep(500)
    SetChrChipByIndex(0x108, 24)
    SetChrSubChip(0x108, 0)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x108, 0, 1300, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)

    def lambda_2613():

        label("loc_2613")

        OP_9E(0xFE, 0x14, 0x0, 0x1388, 0x9C4)
        OP_48()
        Jump("loc_2613")

    QueueWorkItem2(0x108, 3, lambda_2613)

    def lambda_2630():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFCE0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2630)
    WaitChrThread(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    OP_44(0x108, 0x3)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_266D():
        OP_96(0xFE, 0x1EDC, 0xFA, 0x22B0, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_266D)

    def lambda_268B():
        OP_96(0xFE, 0x1E1E, 0xFA, 0x1310, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_268B)
    WaitChrThread(0x108, 0x1)

    def lambda_26AE():
        OP_6D(630, 0, 6360, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_26AE)

    def lambda_26C6():
        OP_6C(153000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_26C6)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x108, 0x4)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x108, 0x1000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_26FE():
        OP_8E(0xFE, 0x0, 0xFA, 0x22B0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_26FE)

    def lambda_2719():
        OP_8E(0xFE, 0x0, 0xFA, 0x1310, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2719)
    WaitChrThread(0x108, 0x1)
    TurnDirection(0x8, 0x108, 0)
    TurnDirection(0x108, 0x8, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x108, 0x1000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_2765():
        OP_96(0xFE, 0x0, 0xFA, 0x1504, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2765)

    def lambda_2783():
        OP_99(0xFE, 0x0, 0x1, 0x640)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2783)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_279D():
        OP_96(0xFE, 0x0, 0xFA, 0x24A4, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_279D)

    def lambda_27BB():
        OP_99(0xFE, 0x0, 0x4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_27BB)
    PlayEffect(0x4, 0xFF, 0xFF, 0, 1200, 6880, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0x190, 0xBB8, 0x96)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_282A():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_282A)
    TurnDirection(0x108, 0x8, 400)
    Sleep(700)

    def lambda_2844():
        OP_96(0xFE, 0xB04, 0xFA, 0x1AE0, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2844)

    def lambda_2862():
        OP_96(0xFE, 0xFFFFF4CA, 0xFA, 0x1AE0, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2862)
    WaitChrThread(0x108, 0x1)
    TurnDirection(0x8, 0x108, 0)
    TurnDirection(0x108, 0x8, 0)
    WaitChrThread(0x108, 0x1)
    Fade(500)
    OP_6D(1220, 0, 8760, 0)
    OP_67(-500, 5590, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(45000, 0)
    OP_6E(481, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_28EA():
        OP_96(0xFE, 0xFFFFF4FC, 0xFA, 0x1AE0, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_28EA)

    def lambda_2908():
        OP_99(0xFE, 0x0, 0x1, 0x640)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2908)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_2922():
        OP_96(0xFE, 0xB36, 0xFA, 0x1AE0, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2922)

    def lambda_2940():
        OP_99(0xFE, 0x0, 0x4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2940)
    PlayEffect(0x4, 0xFF, 0xFF, 0, 1500, 6880, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x108, 0x1)
    PlayEffect(0x3, 0x3, 0xFF, -4100, 1000, 7000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0xFF, 4100, 1000, 7000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0x1F4, 0xBB8, 0x12C)
    OP_B0(0x8, 0xF)
    OP_6F(0x8, 0)
    OP_70(0x8, 0x1E)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 0)
    OP_70(0x9, 0x1E)
    OP_73(0x8)
    OP_73(0x9)
    OP_83(0x4, 0x2)
    Sleep(1000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_2A4B():
        OP_6D(1210, 0, 10570, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A4B)
    OP_22(0x23B, 0x0, 0x64)
    SetChrFlags(0x8, 0x1000)

    def lambda_2A6D():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2A6D)

    def lambda_2A7B():
        OP_96(0xFE, 0xFFFFF182, 0xFA, 0x218E, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A7B)
    Sleep(100)
    OP_22(0x23B, 0x0, 0x64)
    SetChrFlags(0x108, 0x1000)

    def lambda_2AA8():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2AA8)

    def lambda_2AB6():
        OP_96(0xFE, 0xFDB, 0xFA, 0x2378, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2AB6)
    WaitChrThread(0x108, 0x1)
    WaitChrThread(0x8, 0x1)
    ClearChrFlags(0x108, 0x1000)
    ClearChrFlags(0x8, 0x1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x3)
    OP_44(0xF9, 0x3)

    def lambda_2AFD():
        OP_8C(0xFE, 0, 0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2AFD)

    def lambda_2B0B():
        OP_8C(0xFE, 0, 0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2B0B)

    def lambda_2B19():
        OP_8C(0xFE, 0, 0)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_2B19)
    WaitChrThread(0x108, 0x1)
    WaitChrThread(0x101, 0x0)
    Sleep(300)

    ChrTalk(    #34
        0x8,
        (
            "#253F#6P呼呼……\x02\x03",

            "原来你并不是只会吹牛，\x01",
            "还挺顽强的嘛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x108,
        (
            "#077F#2P你也一样……\x02\x03",

            "#076F拥有那样的天赋\x01",
            "怎么会堕入武术的黑暗中！\x02\x03",

            "如果坚持在师傅的教导下苦练的话，\x01",
            "一定可以到达正道的极致啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "#257F#6P哼，轮得到你说吗。\x02\x03",

            "#255F看来老头子的死因\x01",
            "你还不清楚呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x108, 0xFFFFFF38, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #37
        0x108,
        "#073F#2P……什…什么…！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "#253F#6P呼呼，脸色变了啊。\x02\x03",

            "万一你要是赢了的话，\x01",
            "我就说给你听吧。\x02\x03",

            "不过赌注就是你的命。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x8, 0)
    OP_0D()
    SetChrChipByIndex(0x8, 25)
    OP_99(0x8, 0x0, 0x2, 0x5DC)
    Sleep(500)
    PlayEffect(0x1, 0x1, 0x8, 100, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(    #39
        0x108,
        (
            "#074F………………………………\x02\x03",

            "#072F……好吧。\x01",
            "我就赌上这条命。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 23)
    OP_0D()
    OP_99(0x108, 0x0, 0xF, 0x7D0)
    PlayEffect(0x1, 0x2, 0x108, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    Fade(500)
    OP_6D(0, 0, 7000, 0)
    OP_67(0, 4580, -10000, 0)
    OP_6B(4080, 0)
    OP_6C(33000, 0)
    OP_6E(243, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #40
        0x101,
        "#1020F#6P（金、金先生……！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        (
            "#1043F#4P（不行啊，艾丝蒂尔……\x01",
            "  无法阻止了。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(1000, 0, 10500, 0)
    OP_67(0, 6490, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(481, 0)
    ClearMapFlags(0x10)
    OP_0D()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2EC5():
        OP_6B(1650, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2EC5)
    OP_7C(0x0, 0x64, 0xBB8, 0x1388)

    ChrTalk(    #42 op#A op#5
        0x8,
        "#258F#30A呜喔喔喔喔喔喔……！\x05\x02",
    )


    ChrTalk(    #43 op#A op#5
        0x108,
        "#077F#30A嗬啊啊啊啊啊啊……！\x05\x02",
    )

    Sleep(5000)
    OP_56(0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    SetChrPos(0xE, 40, 2000, 2090, 270)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 4)
    SetChrSubChip(0xE, 16)
    SetChrFlags(0xE, 0x2)
    OP_22(0x38E, 0x0, 0x64)
    OP_7D(0x0, 0xE, 0x32, 0x1F4)

    def lambda_2F6F():

        label("loc_2F6F")

        OP_99(0xFE, 0x10, 0x17, 0x1F40)
        OP_48()
        Jump("loc_2F6F")

    QueueWorkItem2(0xE, 1, lambda_2F6F)

    def lambda_2F82():
        OP_8F(0xFE, 0x0, 0x4B0, 0x2580, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2F82)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_2FB1():
        OP_90(0xFE, 0xA8C, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2FB1)

    def lambda_2FCC():
        OP_90(0xFE, 0xFFFFF574, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2FCC)
    WaitChrThread(0x8, 0x1)
    OP_20(0x0)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_2FF6():
        OP_96(0xFE, 0xFFFFF614, 0xFA, 0x2350, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2FF6)
    Sleep(100)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_301E():
        OP_96(0xFE, 0xAAA, 0xFA, 0x2224, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_301E)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    Sleep(1000)
    Sleep(1000)

    ChrTalk(    #44
        0x8,
        "#259F#6P什么……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x108,
        "#073F#2P偃月轮……怎么会！\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 40, 0, -3240, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 2)
    SetChrChipByIndex(0x9, 4)

    def lambda_30E5():
        OP_8F(0xFE, 0x1F4, 0x1F4, 0xFFFFF358, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_30E5)

    def lambda_3100():
        OP_6D(310, 300, -800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3100)

    def lambda_3118():
        OP_67(0, 7680, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3118)

    def lambda_3130():
        OP_6B(1450, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3130)

    def lambda_3140():
        OP_6E(533, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3140)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 65535)

    def lambda_3182():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3182)
    Sleep(50)

    def lambda_3195():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3195)
    Sleep(50)

    def lambda_31A8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31A8)
    Sleep(50)

    def lambda_31BB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_31BB)
    Sleep(50)

    def lambda_31CE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_31CE)
    Sleep(600)
    OP_22(0xD8, 0x0, 0x64)
    WaitChrThread(0xE, 0x2)
    SetChrFlags(0xE, 0x80)
    WaitChrThread(0x101, 0x2)
    OP_99(0x9, 0x2, 0x8, 0x5DC)
    Sleep(1000)

    ChrTalk(    #46
        0x101,
        "#1004F#5P雾、雾香小姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        "#1044F#5P你怎么会在这里……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#792F#4P……蔡斯市的防卫战\x01",
            "终于结束了。\x02\x03",

            "#791F我把接待工作交给王，\x01",
            "自己只是稍微来看看情况而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1016F#5P来、来看看情况……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3305")

    ChrTalk(    #50
        0x106,
        (
            "#055F#5P那个『里塔』\x01",
            "你一个人爬上来的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BC")

    label("loc_3305")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3347")

    ChrTalk(    #51
        0x103,
        (
            "#023F#5P那个『里塔』\x01",
            "你一个人爬上来的吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BC")

    label("loc_3347")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_338A")

    ChrTalk(    #52
        0x109,
        (
            "#1064F#5P那个『里塔』\x01",
            "你一个人爬上来的吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BC")

    label("loc_338A")


    ChrTalk(    #53
        0x102,
        (
            "#1044F#5P那个『里塔』\x01",
            "你一个人爬上来的吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33BC")

    Fade(250)
    SetMapFlags(0x10)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 1)
    OP_0D()
    OP_1D(0x50)
    Sleep(1000)

    def lambda_33E8():
        OP_6D(210, 0, 8800, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_33E8)

    def lambda_3400():
        OP_67(0, 4650, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3400)

    def lambda_3418():
        OP_6B(2880, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3418)

    def lambda_3428():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3428)

    def lambda_3438():
        OP_6E(315, 4000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3438)

    def lambda_3448():
        OP_8E(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3448)

    def lambda_3463():

        label("loc_3463")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3463")

    QueueWorkItem2(0x108, 3, lambda_3463)
    Sleep(500)

    def lambda_3479():
        OP_8E(0xFE, 0x5DC, 0x0, 0x5BE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3479)
    Sleep(200)

    def lambda_3499():
        OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x456, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_3499)
    Sleep(300)

    def lambda_34B9():
        OP_8E(0xFE, 0x3E8, 0x0, 0x83E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_34B9)
    WaitChrThread(0x102, 0x3)

    def lambda_34D9():

        label("loc_34D9")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_34D9")

    QueueWorkItem2(0x102, 3, lambda_34D9)
    WaitChrThread(0xF9, 0x3)

    def lambda_34EF():

        label("loc_34EF")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_34EF")

    QueueWorkItem2(0xF9, 3, lambda_34EF)
    WaitChrThread(0x101, 0x3)

    def lambda_3505():

        label("loc_3505")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3505")

    QueueWorkItem2(0x101, 3, lambda_3505)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x8, 400)
    WaitChrThread(0x102, 0x0)
    OP_44(0x108, 0x1)
    OP_44(0x108, 0x3)
    OP_44(0x8, 0x1)
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x3)
    OP_44(0xF9, 0x3)

    def lambda_353F():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_353F)
    WaitChrThread(0x8, 0x3)
    Sleep(500)

    ChrTalk(    #54
        0x108,
        "#072F雾香，你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "#257F呼呼……还是老样子。\x02\x03",

            "#253F来看看情况，顺便\x01",
            "再给老头子报仇吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "#791F怎么会呢……\x01",
            "那只是公平决斗之后的结果吧。\x02\x03",

            "我没有理由去\x01",
            "破坏父亲的决心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        "#255F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x108,
        "#572F雾香……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "#792F我来这里，\x01",
            "只是为了向某个在六年前\x01",
            "不辞而别的人说几句话，\x02\x03",

            "#790F只是如此而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        "#251F说……几句话？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "#793F嗯嗯……\x02\x03",

            "#792F……喂，瓦鲁特。\x02\x03",

            "为什么要逃避\x01",
            "对我的感觉……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        "#255F#3S！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        (
            "#793F父亲对你说了些什么，\x01",
            "详细内容我不清楚。\x02\x03",

            "但是，那与我们的交往\x01",
            "应该没有任何关系才对啊。\x02\x03",

            "#790F而金更是如此吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x108,
        "#073F！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        "#254F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "#792F……果然是这样。\x02\x03",

            "#794F瓦鲁特……你真傻。\x02\x03",

            "你以为父亲是\x01",
            "会有那种想法的人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#254F这和老头子无关……\x01",
            "是我自己的问题。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x8, 400)
    Sleep(500)

    ChrTalk(    #68
        0x108,
        (
            "#072F等，等一下……\x02\x03",

            "#076F瓦鲁特！\x01",
            "师父究竟和你说了些什么！？\x02\x03",

            "和我又有什么关系！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#254F烦死了……\x01",
            "我没有义务告诉你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "#792F嗯嗯，和金无关。\x02\x03",

            "#790F但是……\x01",
            "你有义务告诉我。\x02\x03",

            "如果一声不响地就消失掉\x01",
            "那只不过是一种逃避而已。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x9, 400)

    ChrTalk(    #71
        0x8,
        "#254F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        (
            "#792F我......对于漠视自己\x01",
            "感情的人没有任何依恋。\x02\x03",

            "你愿意消失或离开都无所谓，\x01",
            "喜欢堕落的话就继续堕落下去吧。\x02\x03",

            "#790F而我只会以游击士协会负责人\x01",
            "的身份来对你作出处理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        "#250F……嘿嘿嘿……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #74
        0x8,
        "#252F#4S啊——哈哈哈！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    OP_22(0x99, 0x0, 0x64)
    OP_23(0xEB)
    OP_1F(0x5A, 0x7D0)
    Fade(500)
    OP_6B(2700, 0)
    OP_82(0x0, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x83, 0x2)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    Sleep(1000)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA6")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3BE4")

    label("loc_3BA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BCD")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3BE4")

    label("loc_3BCD")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3BE4")

    Sleep(1000)

    def lambda_3BEF():
        OP_6D(-250, 200, 17430, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3BEF)

    def lambda_3C07():
        OP_67(0, 3660, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C07)

    def lambda_3C1F():
        OP_6B(3460, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C1F)

    def lambda_3C2F():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3C2F)
    Sleep(50)

    def lambda_3C42():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3C42)
    Sleep(50)
    OP_8C(0x9, 0, 400)
    WaitChrThread(0x101, 0x0)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    Sleep(500)
    OP_72(0x1, 0x20)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3C)
    Sleep(100)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    Sleep(100)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    Sleep(100)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)

    ChrTalk(    #75
        0x101,
        "#1004F#5P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x102,
        "#1042F#5P回来了吗……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1F(0x64, 0x7D0)
    Fade(1000)
    OP_6D(5030, 3860, 11650, 0)
    OP_67(0, 1590, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(45000, 0)
    OP_6E(363, 0)
    OP_0D()

    def lambda_3D56():
        OP_6B(5500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3D56)
    Sleep(500)
    OP_22(0x139, 0x0, 0x64)
    LoadEffect(0x2, "map\\mp049_02.eff")
    PlayEffect(0x2, 0x2, 0xFF, 0, 0, 6720, 0, 0, 0, 550, 550, 550, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_82(0x80, 0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C3607   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_F65 end

    def Function_8_3DDC(): pass

    label("Function_8_3DDC")

    OP_6C(760000, 6000)
    Return()

    # Function_8_3DDC end

    def Function_9_3DE6(): pass

    label("Function_9_3DE6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E32")
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x108, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x108, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x108, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_9_3DE6")

    label("loc_3E32")

    Return()

    # Function_9_3DE6 end

    def Function_10_3E33(): pass

    label("Function_10_3E33")

    OP_98(0x0, 0xE)
    OP_98(0x1, 0x28, 0x7D0, 0x334A)
    OP_98(0x1, 0x28, 0xBB8, 0x3B1A)
    OP_98(0x1, 0x28, 0x1770, 0x4E20)
    OP_98(0x2, 0xFE, 0x4E20, 0x2)
    Return()

    # Function_10_3E33 end

    SaveToFile()

Try(main)
