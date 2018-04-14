from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0131_2 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0131.x',
        MapIndex            = 7,
        MapDefaultBGM       = "ed60010",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        "Function_1_3D05",         # 01, 1
        "Function_2_3D43",         # 02, 2
        "Function_3_3D86",         # 03, 3
        "Function_4_3DC9",         # 04, 4
        "Function_5_3E0C",         # 05, 5
        "Function_6_3E6A",         # 06, 6
        "Function_7_3E9A",         # 07, 7
        "Function_8_3EBB",         # 08, 8
        "Function_9_3EEB",         # 09, 9
        "Function_10_3F1B",        # 0A, 10
        "Function_11_3F5D",        # 0B, 11
        "Function_12_4644",        # 0C, 12
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    SoundLoad(209)
    SoundLoad(349)
    SoundLoad(524)
    SetChrPos(0x101, 37030, 0, 75500, 135)
    SetChrPos(0xF8, 37530, 0, 73700, 0)
    SetChrPos(0xF9, 36660, 0, 73320, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117")
    SetChrPos(0xF9, 37530, 0, 73700, 0)
    SetChrPos(0xF8, 36660, 0, 73320, 0)

    label("loc_117")

    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x103, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_139")
    SetChrFlags(0x104, 0x80)

    label("loc_139")

    OP_6D(43180, 0, 66690, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(315000, 0)
    OP_6E(250, 0)

    def lambda_17C():
        OP_6D(36390, 0, 75300, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17C)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #0
        0x101,
        (
            "#1007F#1P唉，最后还是不放心\x01",
            "一起来了，不过……\x02\x03",

            "#1002F……雪拉姐她们\x01",
            "好像还没来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22F")

    ChrTalk(    #1
        0x107,
        "#063F嗯……也许是邀请失败了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_305")

    label("loc_22F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26F")

    ChrTalk(    #2
        0x105,
        (
            "#040F应该还在协会\x01",
            "说服爱娜小姐吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)
    Jump("loc_305")

    label("loc_26F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AE")

    ChrTalk(    #3
        0x108,
        "#070F也许在协会里还要花些工夫啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)
    Jump("loc_305")

    label("loc_2AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_305")

    ChrTalk(    #4
        0x106,
        (
            "#551F应该还在协会里\x01",
            "说服爱娜吧。\x02\x03",

            "真是的，爱娜还真是麻烦呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    label("loc_305")


    ChrTalk(    #5
        0x101,
        (
            "#1015F#1P不管了，我们就\x01",
            "坐下慢慢等吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x103, 48000, -500, 70290, 270)
    SetChrPos(0x26, 48000, -500, 68920, 270)
    SetChrPos(0x25, 48000, -500, 71150, 270)
    SetChrPos(0x27, 48000, -500, 69890, 270)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x27, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C2")
    OP_8C(0x106, 135, 400)

    ChrTalk(    #6
        0x106,
        (
            "#050F不……\x02\x03",

            "没那个必要了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_494")

    label("loc_3C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_408")
    OP_8C(0x108, 135, 400)

    ChrTalk(    #7
        0x108,
        (
            "#070F不……\x02\x03",

            "看来似乎已经\x01",
            "没必要等了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_494")

    label("loc_408")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_454")
    OP_8C(0x105, 135, 400)

    ChrTalk(    #8
        0x105,
        (
            "#040F嗯…艾丝蒂尔……\x02\x03",

            "似乎没有\x01",
            "那个必要了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_494")

    label("loc_454")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_494")
    OP_8C(0x107, 135, 400)

    ChrTalk(    #9
        0x107,
        (
            "#064F啊～可是……\x02\x03",

            "看来已经不必等了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_494")


    ChrTalk(    #10
        0x101,
        "#1011F#2P哎哎……～？\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_4BA():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4BA)
    Sleep(200)

    def lambda_4CD():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_4CD)

    def lambda_4DB():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_4DB)

    def lambda_4E9():
        OP_6D(42950, 0, 70140, 2000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_4E9)

    def lambda_501():
        OP_6C(326000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_501)

    def lambda_511():
        OP_6E(250, 2000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_511)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x13, 0x2)
    OP_43(0x103, 0x0, 0x2, 0x1)
    OP_43(0x26, 0x0, 0x2, 0x2)
    OP_43(0x25, 0x0, 0x2, 0x3)
    OP_43(0x27, 0x0, 0x2, 0x4)
    WaitChrThread(0x27, 0x0)

    ChrTalk(    #11
        0x103,
        (
            "#020F#5P特意把你叫出来真不好意思啊，爱娜。\x02\x03",

            "接待处那里没什么问题吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x103, 400)

    ChrTalk(    #12
        0x26,
        (
            "#742F嗯，已经让利吉暂时\x01",
            "帮我照看着了。\x02\x03",

            "接受委托者的请求\x01",
            "也是和接待一样重要的工作啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x25, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #13
        0x25,
        "真对不起啊，百忙之中还把你叫来。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x25, 400)

    ChrTalk(    #14
        0x26,
        (
            "#740F没关系，不用介意。\x02\x03",

            "有什么话就\x01",
            "赶快和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x27,
        "#031F呵～那么就开始吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x25,
        "请、请多多关照！\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(36390, 0, 75300, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(250, 0)
    OP_0D()

    ChrTalk(    #17
        0x101,
        "#1020F#2P真、真的来了啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_752")

    ChrTalk(    #18
        0x108,
        (
            "#070F嗯，好像是借口说有委托者\x01",
            "需要商讨才把她带来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80D")

    label("loc_752")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79B")

    ChrTalk(    #19
        0x106,
        (
            "#050F呵，好像是借口说有委托者\x01",
            "需要商讨才把她带来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80D")

    label("loc_79B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E4")

    ChrTalk(    #20
        0x105,
        (
            "#542F好像是和她说有委托者\x01",
            "需要商谈才把她叫来的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80D")

    label("loc_7E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80D")

    ChrTalk(    #21
        0x107,
        "#067F是有事商谈吗……\x02",
    )

    CloseMessageWindow()

    label("loc_80D")


    ChrTalk(    #22
        0x101,
        (
            "#1015F#2P嗯，这个也确实是\x01",
            "商谈，不过……\x02\x03",

            "#1007F爱娜姐\x01",
            "到时会不会发怒呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B67")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A7")

    ChrTalk(    #23
        0x107,
        (
            "#561F不、不过…\x01",
            "为什么连奥利维尔也……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_975")

    label("loc_8A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E6")

    ChrTalk(    #24
        0x105,
        (
            "#045F可、可是\x01",
            "奥利维尔先生什么时候也…？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_975")

    label("loc_8E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_931")

    ChrTalk(    #25
        0x106,
        (
            "#552F那个倒也罢了，\x01",
            "但奥利维尔那家伙为什么也在那里？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_975")

    label("loc_931")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_975")

    ChrTalk(    #26
        0x108,
        (
            "#073F话说回来，奥利维尔\x01",
            "是什么时候跑到那里的啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_975")

    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x101,
        (
            "#1019F#2P说、说起来的话……\x02\x03",

            "那家伙应该在\x01",
            "协会里才对吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A26")

    ChrTalk(    #28
        0x108,
        (
            "#075F大概是偷听到了吧。\x02\x03",

            "一有这种事，那家伙的\x01",
            "嗅觉就灵敏了起来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B67")

    label("loc_A26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A94")

    ChrTalk(    #29
        0x106,
        (
            "#551F一定是偷听到之后\x01",
            "就死皮赖脸硬跟过来的吧。\x02\x03",

            "一有这种事就有他，\x01",
            "真是个敏锐的大笨蛋。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B67")

    label("loc_A94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFC")

    ChrTalk(    #30
        0x107,
        (
            "#067F一定是在协会里偷听到之后\x01",
            "就跟着过来了吧。\x02\x03",

            "#562F不、不愧是奥利维尔先生啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B67")

    label("loc_AFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B67")

    ChrTalk(    #31
        0x105,
        (
            "#045F一定是在协会听到之后\x01",
            "就硬跟来了。\x02\x03",

            "如果是奥利维尔先生的话\x01",
            "这么做就再正常不过了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B67")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_72(0x1, 0x4)
    SetChrPos(0x101, 38060, 0, 75490, 180)
    SetChrChipByIndex(0x103, 21)
    SetChrSubChip(0x103, 0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 41700, 200, 67710, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC1")
    SetChrChipByIndex(0x101, 35)
    SetChrSubChip(0x101, 1)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 41440, 1580, 77300, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C52")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF8")
    SetChrChipByIndex(0xF9, 22)
    Jump("loc_C34")

    label("loc_BF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0D")
    SetChrChipByIndex(0xF9, 23)
    Jump("loc_C34")

    label("loc_C0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C22")
    SetChrChipByIndex(0xF9, 24)
    Jump("loc_C34")

    label("loc_C22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C34")
    SetChrChipByIndex(0xF9, 25)

    label("loc_C34")

    SetChrSubChip(0xF9, 2)
    SetChrFlags(0xF9, 0x4)
    SetChrPos(0xF9, 39580, 1620, 77050, 110)
    Jump("loc_CBE")

    label("loc_C52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C67")
    SetChrChipByIndex(0xF8, 22)
    Jump("loc_CA3")

    label("loc_C67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7C")
    SetChrChipByIndex(0xF8, 23)
    Jump("loc_CA3")

    label("loc_C7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C91")
    SetChrChipByIndex(0xF8, 24)
    Jump("loc_CA3")

    label("loc_C91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA3")
    SetChrChipByIndex(0xF8, 25)

    label("loc_CA3")

    SetChrSubChip(0xF8, 2)
    SetChrFlags(0xF8, 0x4)
    SetChrPos(0xF8, 39580, 1620, 77050, 110)

    label("loc_CBE")

    Jump("loc_DBE")

    label("loc_CC1")

    OP_72(0x2, 0x4)
    SetChrChipByIndex(0x101, 35)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 40320, 1620, 78700, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFB")
    SetChrChipByIndex(0xF8, 22)
    Jump("loc_D37")

    label("loc_CFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D10")
    SetChrChipByIndex(0xF8, 23)
    Jump("loc_D37")

    label("loc_D10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D25")
    SetChrChipByIndex(0xF8, 24)
    Jump("loc_D37")

    label("loc_D25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D37")
    SetChrChipByIndex(0xF8, 25)

    label("loc_D37")

    SetChrSubChip(0xF8, 2)
    SetChrFlags(0xF8, 0x4)
    SetChrPos(0xF8, 39580, 1620, 77050, 110)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D67")
    SetChrChipByIndex(0xF9, 22)
    Jump("loc_DA3")

    label("loc_D67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7C")
    SetChrChipByIndex(0xF9, 23)
    Jump("loc_DA3")

    label("loc_D7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D91")
    SetChrChipByIndex(0xF9, 24)
    Jump("loc_DA3")

    label("loc_D91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA3")
    SetChrChipByIndex(0xF9, 25)

    label("loc_DA3")

    SetChrSubChip(0xF9, 1)
    SetChrFlags(0xF9, 0x4)
    SetChrPos(0xF9, 41440, 1580, 77300, 270)

    label("loc_DBE")

    OP_8C(0xC, 180, 0)
    OP_4A(0xC, 255)
    SetChrFlags(0x26, 0x4)
    SetChrFlags(0x26, 0x40)
    SetChrPos(0x26, 38290, -50, 67720, 114)
    SetChrChipByIndex(0x27, 17)
    SetChrSubChip(0x27, 0)
    SetChrFlags(0x27, 0x4)
    SetChrFlags(0x27, 0x40)
    SetChrPos(0x27, 39710, 80, 68530, 180)
    SetChrChipByIndex(0x25, 14)
    SetChrSubChip(0x25, 0)
    SetChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x40)
    SetChrPos(0x25, 39690, 40, 66460, 0)
    ClearChrFlags(0x28, 0x80)
    SetChrSubChip(0x28, 28)
    ClearChrFlags(0x33, 0x80)
    SetChrSubChip(0x33, 5)
    ClearChrFlags(0x34, 0x80)
    SetChrSubChip(0x34, 5)
    ClearChrFlags(0x35, 0x80)
    SetChrSubChip(0x35, 5)
    ClearChrFlags(0x36, 0x80)
    SetChrSubChip(0x36, 5)
    OP_6D(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x19)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #32
        0x27,
        (
            "#030F#2P──那么，先干一杯吧！\x02\x03",

            "为了庆祝这次美妙的会面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x103,
        "#021F嗯嗯，说的对。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x26,
        (
            "#743F#1P啊，我是没问题，不过……\x02\x03",

            "安敦先生要不要紧？\x02\x03",

            "在谈话前就先喝酒……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x25,
        (
            "不、不要紧！\x01",
            "大家开始喝吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x25,
        (
            "别看我这副样子，\x01",
            "但酒量可是很强的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x26,
        (
            "#740F#1P啊，那可失礼了。\x01",
            "果然是真人不露相啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x27,
        "#031F#2P呵呵，那就干杯吧！\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(36700, 0, 77610, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1070")

    ChrTalk(    #39
        0x105,
        "#045F马、马上就开始喝了啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1140")

    label("loc_1070")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BD")

    ChrTalk(    #40
        0x107,
        (
            "#065F直接就开始喝了啊……\x02\x03",

            "#561F……已经开始喝上了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1140")

    label("loc_10BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F4")

    ChrTalk(    #41
        0x108,
        (
            "#070F喔～这么快就\x01",
            "开始喝了啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1140")

    label("loc_10F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1140")

    ChrTalk(    #42
        0x106,
        (
            "#050F喂喂……\x01",
            "这哪里算是什么商谈，\x02\x03",

            "直接就开始喝酒了嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1140")


    ChrTalk(    #43
        0x101,
        (
            "#1002F可是，为什么连奥利维尔\x01",
            "也在一起……\x02\x03",

            "#1015F……难道他也服了那个药？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E0")

    ChrTalk(    #44
        0x106,
        (
            "#050F大概是吧。\x02\x03",

            "不然坐在爱娜面前他怎么\x01",
            "还露得出那种笑容。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E0")

    label("loc_11E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_122A")

    ChrTalk(    #45
        0x108,
        (
            "#070F啊啊，应该是的。\x02\x03",

            "不然他哪里还挤得出那种笑脸。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E0")

    label("loc_122A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1295")

    ChrTalk(    #46
        0x107,
        (
            "#062F嗯、嗯……\x01",
            "我也是那么想的。\x02\x03",

            "#067F不然的话，奥利维尔先生\x01",
            "不可能这么自信满满的…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E0")

    label("loc_1295")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E0")

    ChrTalk(    #47
        0x105,
        (
            "#040F啊啊……可能吧。\x02\x03",

            "从他那自信的态度来看应该没错……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E0")

    OP_6D(36700, 0, 74470, 1500)

    ChrTalk(    #48
        0x27,
        (
            "#031F#2P──哈哈哈哈哈哈哈。\x02\x03",

            "再来再来～～\x01",
            "──爱娜又在开玩笑了～～真是的啦～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1007F#1P是，是啊……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_0D()

    ChrTalk(    #50
        0x26,
        (
            "#744F#1P──好了，咱们还是\x01",
            "进入正题吧。\x02\x03",

            "#740F找我出来，究竟有\x01",
            "什么事情要说呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x25,
        (
            "嗯、嗯……\x01",
            "啊啊……这个…\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x25, 13)
    ClearChrFlags(0x25, 0x4)
    OP_96(0x25, 0x983A, 0x0, 0x102E8, 0x190, 0x1388)

    ChrTalk(    #52
        0x25,
        "那、那个……爱娜小姐！！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x26, 165, 0)

    ChrTalk(    #53
        0x26,
        "#740F#1P在……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x25,
        "请…请你和我…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x25,
        "#4S请你和我交往吧！！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x26, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_63(0x26)

    ChrTalk(    #56
        0x26,
        (
            "#743F#1P…………………………\x02\x03",

            "交往……\x01",
            "那个……你是指那个意思？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x25,
        (
            "是，就是那样！\x01",
            "请多关照！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x25,
        (
            "没…没有你的话\x01",
            "我就活不下去了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x26,
        (
            "#745F#1P怎、怎么会……\x02\x03",

            "突然说出这种话…\x01",
            "真是为难啊……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x27, 2)

    ChrTalk(    #60
        0x27,
        (
            "#030F#2P呵呵，爱娜\x01",
            "会感到困惑也是正常的啊。\x02\x03",

            "男女之间的事情\x01",
            "本来就不能以理性来判断……\x02\x03",

            "这可不是经过考虑后就能\x01",
            "马上给出回答的问题哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x25, 30, 400)

    ChrTalk(    #61
        0x25,
        (
            "可、可是…\x01",
            "不回答的话实在太让我为难了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x25,
        (
            "难道我只能怀着如此强烈的相思之情\x01",
            "痛苦地渡过余生吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x27, 0)

    ChrTalk(    #63
        0x27,
        (
            "#030F#2P呵～冷静点，年轻人。\x01",
            "我倒是有个绝妙的好主意。\x02\x03",

            "就在这里以决斗的方式\x01",
            "来决定结果如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x26, 114, 400)

    ChrTalk(    #64
        0x26,
        "#743F#1P决斗……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 2)

    ChrTalk(    #65
        0x103,
        "#023F……这…怎么说？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x27,
        (
            "#035F#2P决斗的舞台就是这家酒馆……\x02\x03",

            "至于决斗的方式，\x01",
            "不用我多说也该明白了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x25,
        "原，原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x26,
        "#742F#1P……是比拼酒量对吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x103,
        "#027F很有趣的提议啊。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x27, 2)

    ChrTalk(    #70
        0x27,
        (
            "#035F#2P可是这样比的话，\x01",
            "安敦先生实在太可怜了。\x02\x03",

            "应该给爱娜增加一些附加条件才公平啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x26,
        (
            "#742F#1P这个倒是没问题，不过……\x01",
            "到底是什么附加条件呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x27,
        (
            "#037F#2P条件就是我也加入\x01",
            "安敦一方，\x02\x03",

            "换言之，\x01",
            "就是二对一啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x26,
        (
            "#744F#1P…………………………\x02\x03",

            "#742F好，\x01",
            "我接受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        (
            "#525F呵呵，不愧是爱娜啊。\x02\x03",

            "那么，让我来担任\x01",
            "这场决斗的见证人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x26,
        (
            "#742F#1P不过，我也\x01",
            "有个条件。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x25, 0x26, 400)

    ChrTalk(    #76
        0x25,
        "什、什么条件呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x26,
        (
            "#742F#1P既然是决斗，\x01",
            "就要喝这家店里度数最强的酒。\x02\x03",

            "不好意思了，因为我\x01",
            "的时间有限。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x25, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #78
        0x27,
        (
            "#034F#2P明、明白了……\x01",
            "（真不愧是爱娜啊。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x25, 14)
    SetChrSubChip(0x25, 0)
    SetChrFlags(0x25, 0x4)
    SetChrPos(0x25, 39690, 50, 66460, 0)
    ClearChrFlags(0x2A, 0x80)
    SetChrSubChip(0x2A, 29)
    ClearChrFlags(0x2B, 0x80)
    SetChrSubChip(0x2B, 29)
    ClearChrFlags(0x2C, 0x80)
    SetChrSubChip(0x2C, 29)
    SetChrSubChip(0x28, 29)
    SetChrPos(0xC, 37670, 0, 66970, 62)
    SetChrSubChip(0x33, 1)
    SetChrSubChip(0x34, 1)
    SetChrSubChip(0x35, 1)
    SetChrSubChip(0x27, 0)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #79
        0xC,
        (
            "我…我想这些\x01",
            "应该足够了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xC,
        (
            "就算是熊，喝这么多\x01",
            "也会醉倒的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x26,
        (
            "#740F#1P谢谢，\x01",
            "福克纳先生。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xC, 0x0, 0x2, 0x5)
    Sleep(1000)

    ChrTalk(    #82
        0x103,
        (
            "#027F好了……\x02\x03",

            "现在就\x01",
            "开始如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x27,
        "#035F#2P呵呵，早准备好了，随时可以开始。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x26,
        "#742F#1P啊啊，那就开始吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x25,
        (
            "好、好！\x01",
            "拼了～！！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(36700, 0, 77610, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_0D()

    ChrTalk(    #86
        0x101,
        "#1002F……开始了啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C77")

    ChrTalk(    #87
        0x106,
        (
            "#050F啊啊……\x02\x03",

            "不知道要比拼多久呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4B")

    label("loc_1C77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CC2")

    ChrTalk(    #88
        0x107,
        (
            "#063F嗯、嗯嗯……\x02\x03",

            "如果那药\x01",
            "真的有效就好了，不过……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4B")

    label("loc_1CC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D07")

    ChrTalk(    #89
        0x108,
        (
            "#070F啊啊……\x02\x03",

            "不知道那两个人\x01",
            "究竟能撑多久……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4B")

    label("loc_1D07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D4B")

    ChrTalk(    #90
        0x105,
        (
            "#043F嗯……\x02\x03",

            "那个药如果\x01",
            "真的有用就好了，不过……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D4B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    SetChrSubChip(0x103, 2)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #91
        0x25,
        "呜啊啊～第５杯！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x25,
        (
            "呜呜～空腹喝酒果然\x01",
            "不舒服啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x27,
        (
            "#030F#2P呵，我正好也喝干\x01",
            "第５杯了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x103,
        (
            "#020F 2个人加起来\x01",
            "正好是１０杯啊，\x02\x03",

            "还挺不错的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x26,
        (
            "#740F#1P嗯，确实……\x02\x03",

            "不过你们要是喝太猛的话，\x01",
            "过一会儿也许会突然醉倒啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x25,
        (
            "哪里哪里。\x01",
            "这么点酒怎么可能醉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x27,
        (
            "#031F#2P哈哈，说的对，我也是\x01",
            "一点醉意都没有呢。\x02\x03",

            "来！继续啊～～\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(36700, 0, 77610, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_0D()

    ChrTalk(    #98
        0x101,
        (
            "#1002F嗯……\x01",
            "两个人发挥都不错啊。\x02\x03",

            "#1015F果然是那药\x01",
            "生效了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FC9")

    ChrTalk(    #99
        0x105,
        (
            "#042F不过爱娜小姐的表情\x01",
            "也是一点变化都没有啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2091")

    label("loc_1FC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_201E")

    ChrTalk(    #100
        0x107,
        (
            "#561F不过爱娜姐姐好像\x01",
            "也一点反应都没有啊。\x02\x03",

            "她明明没有服药啊…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2091")

    label("loc_201E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2055")

    ChrTalk(    #101
        0x106,
        (
            "#052F爱娜的脸色\x01",
            "也一点都没变啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2091")

    label("loc_2055")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2091")

    ChrTalk(    #102
        0x108,
        (
            "#070F不过爱娜君的脸色\x01",
            "也完全没有变化啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2091")


    ChrTalk(    #103
        0x101,
        (
            "#1016F所以说……\x01",
            "爱娜姐真是深不可测啊～～。\x02\x03",

            "不过这么一来的话\x01",
            "恐怕就要进入持久战了……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x2D, 0x80)
    SetChrSubChip(0x2D, 29)
    ClearChrFlags(0x2E, 0x80)
    SetChrSubChip(0x2E, 29)
    SetChrPos(0x2D, 41440, 0, 66610, 15)
    SetChrPos(0x2E, 41090, 0, 66050, 30)
    OP_6D(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #104
        0x26,
        (
            "#744F#1P呼……这是第２０杯了吧。\x02\x03",

            "#740F……你们怎样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x25,
        "我…我是第１０杯～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x27,
        "#037F#2P我也喝了１０杯了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x103,
        (
            "#027F这样的话，他们也是２０杯…\x02\x03",

            "爱娜啊，这次他们实在是很顽强啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x26,
        (
            "#743F#1P是啊，真令人吃惊。\x02\x03",

            "好像从刚开始时\x01",
            "就一直没有示弱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x25,
        (
            "哼哼哼哼。\x01",
            "我早就说过吧？我的酒量可是一流的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x25,
        (
            "不…不过，嗓子里好像\x01",
            "有团火在烧一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x27,
        (
            "#034F#2P确、确实啊……\x01",
            "简直像就要被烧伤了一样。\x02\x03",

            "#036F爱…爱娜，\x01",
            "你难道就一点感觉也没有吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x27, 2)

    ChrTalk(    #112
        0x26,
        (
            "#741F#1P哎呀，你们的嗓子怎么了？\x02\x03",

            "难道突然感冒了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x25, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x27, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #113
        0x27,
        (
            "#034F#2P明知故问……\x01",
            "真，真过分啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x26,
        (
            "#740F#1P如果感觉身体不舒服的话\x01",
            "就不要太勉强了，硬撑下去\x02\x03",

            "会给店主添麻烦的哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x25,
        "啊、啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x27,
        "#035F#2P呵，那么就继续吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x2F, 0x80)
    SetChrSubChip(0x2F, 29)
    ClearChrFlags(0x30, 0x80)
    SetChrSubChip(0x30, 29)
    SetChrSubChip(0x27, 0)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #117
        0x27,
        (
            "#037F#2P十…十五杯……\x02\x03",

            "咳咳咳……\x01",
            "啊～胃里好像已经着火了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x25,
        "…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    SetChrSubChip(0x103, 0)

    ChrTalk(    #119
        0x27,
        "#033F#2P嗯嗯……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x103,
        "#023F安敦……！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x25, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #121
        0x25,
        "哈……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x25,
        "怎、怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x26,
        (
            "#743F#1P身体不舒服吗？\x02\x03",

            "看你的表情\x01",
            "似乎非常呆滞啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x25,
        (
            "不，不是的……\x01",
            "我…没问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x27,
        (
            "#530F#2P（安敦兄！！\x01",
            "振作一点啊！！)\x02\x03",

            "(药的效力\x01",
            " 还没消失呢！)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x25,
        "（是、是的！)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x27,
        (
            "#035F#2P（别忘了爱娜也\x01",
            " 喝下了同样多的酒……)\x02\x03",

            "(不管她是怎样的酒豪，\x01",
            " 喝到这种地步肯定也快到极限了。)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x25,
        "(可、可是…奥利维尔……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x25,
        (
            "(爱娜的脸色\x01",
            "好像完全都没有……变化啊)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0x27, 2)
    Sleep(400)

    ChrTalk(    #130
        0x27,
        "#032F#2P（唔…！嗯嗯……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x26,
        (
            "#740F#1P？？？\x02\x03",

            "你们两个怎么啦？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x27, 0)
    Sleep(400)

    ChrTalk(    #132
        0x27,
        (
            "#039F#2P（可恶，你要还是男人\x01",
            "的话就不要去管那些小事！)\x02\x03",

            "(拿出全部的毅力来！\x01",
            " 用你的爱和勇气来打败她吧！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x25,
        "(了、了解！！)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x26,
        (
            "#743F#1P真的没事吗？\x02\x03",

            "如果身体感觉到异常的话，\x01",
            "最好还是早点放弃哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x27,
        (
            "#035F#2P呵，多谢你的关心，\x01",
            "但遗憾的是我们一点投降的意思也没有啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x103,
        (
            "#520F对～对～！真正的决斗现在才刚开始啊！\x02\x03",

            "好啊！大家继续决胜负吧～～\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    ClearChrFlags(0x31, 0x80)
    SetChrSubChip(0x31, 29)
    ClearChrFlags(0x32, 0x80)
    SetChrSubChip(0x32, 29)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x40)
    SetChrPos(0x25, 39690, 40, 66460, 0)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #137
        0x26,
        "#745F#1P……呼～第３６杯！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x25,
        "１…８…杯……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x27,
        "#037F#2P我…也是１…８杯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x26,
        (
            "#740F#1P你们两个看起来好痛苦啊～\x02\x03",

            "难道还要继续吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x27,
        (
            "#037F#2P哈哈哈哈哈哈。\x01",
            "事到如今，怎么还问这种话！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x25,
        "哈哈，说的对！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x25,
        (
            "要是在这时放弃的话…\x01",
            "岂不是成了男人中的窝囊废……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x25,
        "……哎、哎呀！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0)

    ChrTalk(    #145
        0x103,
        "#023F安敦！？\x02",
    )

    CloseMessageWindow()

    def lambda_2AAA():
        OP_6D(40270, 0, 67330, 1000)
        ExitThread()

    QueueWorkItem(0x26, 0, lambda_2AAA)

    def lambda_2AC2():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_2AC2)
    OP_9E(0x25, 0x14, 0x0, 0x1F4, 0xFA0)
    ClearChrFlags(0x25, 0x100)
    SetChrChipByIndex(0x25, 13)
    SetChrPos(0x25, 40480, 0, 66130, 0)
    SetChrChipByIndex(0x25, 13)
    OP_D1(37, 20000, 0, 0, 0)

    def lambda_2B18():
        OP_D1(37, 60000, -15000, -90000, 200)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_2B18)
    OP_51(0x25, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_22(0xD1, 0x0, 0x64)
    ClearChrFlags(0x2D, 0x100)
    ClearChrFlags(0x2E, 0x100)
    OP_51(0x2D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2B7D():
        OP_96(0x2D, 0xA3FC, 0x0, 0x10586, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2B7D)

    def lambda_2B9B():
        OP_D1(45, 30000, -15000, -80000, 200)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_2B9B)

    def lambda_2BB5():
        OP_D1(46, 60000, -15000, -135000, 200)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_2BB5)
    OP_22(0x15D, 0x0, 0x64)
    WaitChrThread(0x2D, 0x2)
    OP_51(0x2D, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2D, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2D, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x2E, 0x2)
    OP_51(0x2E, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x27, 1)
    SetChrSubChip(0x103, 1)
    OP_0D()
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x26, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x27, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #146
        0x27,
        "#036F#2P安…安敦老兄！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x26,
        "#743F#1P哎呀，不得了啦！\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_2CB2():
        OP_6D(41230, 0, 67950, 1000)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_2CB2)

    def lambda_2CCA():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_2CCA)
    OP_43(0x26, 0x1, 0x2, 0xC)
    SetChrChipByIndex(0x103, 65535)
    SetChrFlags(0x103, 0x40)
    ClearChrFlags(0x103, 0x4)
    OP_96(0x103, 0xA1E0, 0x0, 0x10662, 0xC8, 0x1388)
    OP_8C(0x103, 180, 0)
    ClearChrFlags(0x27, 0x4)
    SetChrChipByIndex(0x27, 16)
    OP_96(0x27, 0x9E3E, 0x0, 0x10C98, 0x190, 0x1388)
    SetChrChipByIndex(0x27, 36)
    OP_8E(0x27, 0x9F60, 0x0, 0x10C98, 0xFA0, 0x1)
    SetChrSubChip(0x27, 3)
    WaitChrThread(0x25, 0x1)

    ChrTalk(    #148
        0x27,
        "#038F#2P……哎…哎呀……！？\x02",
    )

    OP_9E(0x27, 0x14, 0x0, 0x1F4, 0xFA0)
    CloseMessageWindow()
    OP_59()
    SetChrSubChip(0x27, 0)
    SetChrFlags(0x27, 0x4)
    OP_96(0x27, 0xA3AC, 0xF0, 0x10B94, 0x190, 0xFA0)
    SetChrChipByIndex(0x27, 18)
    OP_51(0x27, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x20C, 0x0, 0x64)
    OP_96(0x27, 0xA4A6, 0xF0, 0x10B94, 0x190, 0xFA0)
    OP_8C(0x103, 0, 400)

    ChrTalk(    #149
        0x103,
        "#025F#1P哎呀～连奥利维尔都……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x26,
        "#742F#1P两个人都振作一点啊！！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x80)
    SetChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E75")
    ClearChrFlags(0xF8, 0x80)
    SetChrFlags(0xF8, 0x40)
    ClearChrFlags(0xF8, 0x4)
    SetChrChipByIndex(0xF8, 65535)
    SetChrPos(0xF8, 42530, 1500, 78540, 180)

    label("loc_2E75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EA7")
    ClearChrFlags(0xF9, 0x80)
    SetChrFlags(0xF9, 0x40)
    ClearChrFlags(0xF9, 0x4)
    SetChrChipByIndex(0xF9, 65535)
    SetChrPos(0xF9, 42960, 1500, 78910, 180)

    label("loc_2EA7")

    SetChrChipByIndex(0x101, 65535)
    SetChrPos(0x101, 42860, 1500, 77720, 180)

    def lambda_2EC3():
        OP_6D(41380, 0, 69390, 3000)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_2EC3)
    OP_43(0x101, 0x0, 0x2, 0x6)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF8")
    OP_43(0xF9, 0x0, 0x2, 0x8)
    Jump("loc_2F22")

    label("loc_2EF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F0F")
    OP_43(0xF8, 0x0, 0x2, 0x8)
    Jump("loc_2F22")

    label("loc_2F0F")

    OP_43(0xF8, 0x0, 0x2, 0x8)
    Sleep(600)
    OP_43(0xF9, 0x0, 0x2, 0x9)

    label("loc_2F22")

    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)

    ChrTalk(    #151
        0x101,
        "#1020F#2P奥、奥利维尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x27,
        "#038F#4P呜……嗯～～嗯……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FBD")

    ChrTalk(    #153
        0x106,
        (
            "#551F都已经翻白眼了啊……\x02\x03",

            "看来药的效果\x01",
            "已经过去了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B3")

    label("loc_2FBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3019")

    ChrTalk(    #154
        0x108,
        (
            "#075F不行了啊……\x01",
            "已经完全烂醉如泥了。\x02\x03",

            "嗯，看来药的效果\x01",
            "已经过去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B3")

    label("loc_3019")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_306C")

    ChrTalk(    #155
        0x105,
        (
            "#043F完、完全醉到不成样子了啊。\x02\x03",

            "看来是药劲已经\x01",
            "过去了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B3")

    label("loc_306C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30B3")

    ChrTalk(    #156
        0x107,
        (
            "#561F彻、彻底烂醉如泥了啊。\x02\x03",

            "难道药效已经过去了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B3")


    ChrTalk(    #157
        0x103,
        (
            "#025F#1P真是遗憾啊……\x02\x03",

            "本以为今天能把\x01",
            "爱娜灌醉的。\x02\x03",

            "唉，看来药这种东西\x01",
            "也只能应付一时而已啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x26,
        "#743F#1P药……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#1015F#2P……其实呢……\x02",
    )

    CloseMessageWindow()

    def lambda_3150():
        OP_6D(40560, 0, 66540, 2000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_3150)
    WaitChrThread(0x13, 0x0)
    SetChrPos(0x24, 39760, -500, 61000, 0)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x24, 0x80)

    def lambda_318E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_318E)
    OP_8E(0x24, 0x9B50, 0x0, 0xFBB8, 0x7D0, 0x0)
    OP_8C(0x24, 50, 400)

    ChrTalk(    #160
        0x24,
        "唉，这样可不行啊……\x02",
    )

    CloseMessageWindow()

    def lambda_31D5():
        TurnDirection(0xFE, 0x24, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_31D5)

    def lambda_31E3():
        TurnDirection(0xFE, 0x24, 400)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_31E3)

    def lambda_31F1():
        TurnDirection(0xFE, 0x24, 400)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_31F1)

    def lambda_31FF():
        TurnDirection(0xFE, 0x24, 400)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_31FF)
    TurnDirection(0x26, 0x24, 400)

    ChrTalk(    #161
        0x103,
        "#023F#1P啊！教区长。\x02",
    )

    CloseMessageWindow()

    def lambda_322E():
        OP_6D(41450, 0, 68050, 2500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_322E)

    def lambda_3246():

        label("loc_3246")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3246")

    QueueWorkItem2(0x101, 3, lambda_3246)

    def lambda_3257():

        label("loc_3257")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3257")

    QueueWorkItem2(0x103, 3, lambda_3257)

    def lambda_3268():

        label("loc_3268")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3268")

    QueueWorkItem2(0xF8, 3, lambda_3268)

    def lambda_3279():

        label("loc_3279")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3279")

    QueueWorkItem2(0xF9, 3, lambda_3279)

    def lambda_328A():

        label("loc_328A")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_328A")

    QueueWorkItem2(0x26, 3, lambda_328A)
    OP_8E(0x24, 0xA316, 0x0, 0xFD51, 0x7D0, 0x0)
    OP_8E(0x24, 0xA64A, 0x0, 0x10036, 0x7D0, 0x0)
    OP_8C(0x24, 315, 400)
    WaitChrThread(0x13, 0x0)
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)
    OP_44(0x26, 0x3)

    ChrTalk(    #162
        0x26,
        "#743F#1P啊，您怎么会来这里？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x26, 400)

    ChrTalk(    #163
        0x24,
        (
            "#4P嗯，我听说你在这里和\x01",
            "两个年轻人在拼酒，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x24,
        (
            "#4P忽然想起有些事情还没和他们说明，\x01",
            "就马上赶来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x24,
        "#4P不过好像还是迟了一步啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        (
            "#1007F嗯…他们两个都已经\x01",
            "完全醉倒不起了。\x02\x03",

            "看来是药的效力\x01",
            "已经过去了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x101, 400)

    ChrTalk(    #167
        0x24,
        (
            "#4P不，其实这药的效果是\x01",
            "可以持续一整晚的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x24,
        (
            "#4P大概他们是两个人一人一半\x01",
            "将药分吃了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x24,
        (
            "#4P要是不服够规定的用量\x01",
            "自然不会有什么效果啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #170
        0x101,
        "#1008F啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34E9")

    ChrTalk(    #171
        0x107,
        (
            "#561F原、原来如此……\x01",
            "原来～是这样啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3599")

    label("loc_34E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3528")

    ChrTalk(    #172
        0x106,
        (
            "#053F原来如此啊……\x01",
            "所以才会失去药效吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3599")

    label("loc_3528")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3563")

    ChrTalk(    #173
        0x108,
        (
            "#070F原来如此……\x01",
            "这就是自作自受吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3599")

    label("loc_3563")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3599")

    ChrTalk(    #174
        0x105,
        (
            "#047F原来如此……\x01",
            "所以才会这样……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3599")


    ChrTalk(    #175
        0x24,
        (
            "#4P大家以后在吃药时一定要仔细遵照\x01",
            "说明书上的用法用量服用才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x26,
        (
            "#745F#1P呼～原来如此，\x01",
            "是这么一回事啊。\x02\x03",

            "我早就觉得奇怪了，\x01",
            "奥利维尔突然兴致冲冲地\x01",
            "跑来邀约我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1016F啊、啊哈哈……\x02\x03",

            "不过这样一来他心中的恶梦\x01",
            "又再次加深了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x24,
        (
            "#4P好了，这两个人就\x01",
            "交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x24,
        (
            "#4P他们可是喝下了过量\x01",
            "的烈酒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x26,
        (
            "#740F#1P嗯嗯，那就拜托您了。\x02\x03",

            "我也得赶快\x01",
            "回协会了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x26, 400)

    ChrTalk(    #181
        0x24,
        "#4P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x26,
        "#743F#1P嗯？您怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x24,
        (
            "#4P没、没什么…爱娜啊……\x01",
            "你也太能喝了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x24,
        (
            "#4P明明喝了这么多，\x01",
            "竟然一点醉意都没有吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x26,
        (
            "#741F#1P啊，这点酒\x01",
            "根本不算什么啦。\x02\x03",

            "就喝酒而言，\x01",
            "这种程度只是陪他们玩玩而已了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382B")
    OP_62(0xF6, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3869")

    label("loc_382B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3852")
    OP_62(0xF6, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3869")

    label("loc_3852")

    OP_62(0xF6, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3869")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3890")
    OP_62(0xF7, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_38CE")

    label("loc_3890")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B7")
    OP_62(0xF7, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_38CE")

    label("loc_38B7")

    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_38CE")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3945")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3907")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3945")

    label("loc_3907")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392E")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3945")

    label("loc_392E")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3945")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3979")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_39B7")

    label("loc_3979")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A0")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_39B7")

    label("loc_39A0")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_39B7")


    def lambda_39BD():
        OP_8C(0x0, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_39BD)

    def lambda_39CB():
        OP_8C(0x1, 180, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_39CB)

    def lambda_39D9():
        OP_8C(0x2, 180, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_39D9)

    def lambda_39E7():
        OP_8C(0x3, 180, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_39E7)
    Sleep(1000)

    ChrTalk(    #186
        0x101,
        "#1020F#2P啊啊！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A33")

    ChrTalk(    #187
        0x108,
        "#073F唔…怎么会…\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AC9")

    label("loc_3A33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A69")

    ChrTalk(    #188
        0x106,
        "#055F……她好像不是在开玩笑啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AC9")

    label("loc_3A69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AA0")

    ChrTalk(    #189
        0x105,
        (
            "#045F真…真是豪气十足\x01",
            "的回答啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AC9")

    label("loc_3AA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AC9")

    ChrTalk(    #190
        0x107,
        "#065F骗、骗人的吧……\x02",
    )

    CloseMessageWindow()

    label("loc_3AC9")


    ChrTalk(    #191
        0x103,
        "#025F#5P简直就是个无底洞……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x24,
        (
            "#4P……是吗。\x01",
            "那就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x24,
        (
            "#4P确实有些酒气，\x01",
            "但一点都没醉倒是真的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x26,
        "#740F#1P那……我就先失陪了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x103, 400)
    TurnDirection(0x103, 0x26, 400)

    ChrTalk(    #195
        0x26,
        (
            "#741F#1P好啦，雪拉扎德。\x01",
            "这里的残局就交给你了。\x02\x03",

            "对了，别忘了\x01",
            "让奥利维尔掏酒钱。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BC1():

        label("loc_3BC1")

        TurnDirection(0xFE, 0x26, 400)
        OP_48()
        Jump("loc_3BC1")

    QueueWorkItem2(0x101, 0, lambda_3BC1)

    def lambda_3BD2():

        label("loc_3BD2")

        TurnDirection(0xFE, 0x26, 400)
        OP_48()
        Jump("loc_3BD2")

    QueueWorkItem2(0x103, 0, lambda_3BD2)

    def lambda_3BE3():

        label("loc_3BE3")

        TurnDirection(0xFE, 0x26, 400)
        OP_48()
        Jump("loc_3BE3")

    QueueWorkItem2(0xF8, 0, lambda_3BE3)

    def lambda_3BF4():

        label("loc_3BF4")

        TurnDirection(0xFE, 0x26, 400)
        OP_48()
        Jump("loc_3BF4")

    QueueWorkItem2(0xF9, 0, lambda_3BF4)

    def lambda_3C05():

        label("loc_3C05")

        TurnDirection(0xFE, 0x26, 400)
        OP_48()
        Jump("loc_3C05")

    QueueWorkItem2(0x24, 0, lambda_3C05)

    def lambda_3C16():
        OP_69(0x27, 0x5DC)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_3C16)
    OP_43(0x26, 0x0, 0x2, 0xA)
    WaitChrThread(0x26, 0x2)

    ChrTalk(    #196
        0x27,
        (
            "#038F#4P呜、呜呜呜……\x01",
            "不愧是爱娜啊。\x02\x03",

            "如此无懈可击的你…\x01",
            "我最喜欢了…………嗝！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x26, 0x80)
    OP_28(0x76, 0x1, 0x8)
    OP_28(0x76, 0x1, 0x10)
    OP_28(0x76, 0x1, 0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3CB2")
    OP_28(0x76, 0x1, 0x4000)

    label("loc_3CB2")

    OP_28(0x76, 0x4, 0x10)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #197
        "\x07\x02任务【千杯不醉的秘药】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_0_AA end

    def Function_1_3D05(): pass

    label("Function_1_3D05")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3D1B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3D1B)
    OP_8E(0xFE, 0xA410, 0x0, 0x11292, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_1_3D05 end

    def Function_2_3D43(): pass

    label("Function_2_3D43")

    Sleep(1000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3D5E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3D5E)
    OP_8E(0xFE, 0xA7F8, 0x0, 0x10D38, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_2_3D43 end

    def Function_3_3D86(): pass

    label("Function_3_3D86")

    Sleep(1400)
    OP_9F(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x25, 0x80)

    def lambda_3DA1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x25, 3, lambda_3DA1)
    OP_8E(0x25, 0xA7F8, 0x0, 0x115EE, 0x7D0, 0x0)
    OP_8C(0x25, 180, 400)
    Return()

    # Function_3_3D86 end

    def Function_4_3DC9(): pass

    label("Function_4_3DC9")

    Sleep(2000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3DE4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3DE4)
    OP_8E(0xFE, 0xAC44, 0x0, 0x11102, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_4_3DC9 end

    def Function_5_3E0C(): pass

    label("Function_5_3E0C")

    SetChrFlags(0xFE, 0x40)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x823C, 0x0, 0x10F54, 0x1388, 0x0)
    OP_8E(0xFE, 0x823C, 0x0, 0x11850, 0x1388, 0x0)
    OP_8E(0xFE, 0x82C8, 0x654, 0x125D4, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x8)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_5_3E0C end

    def Function_6_3E6A(): pass

    label("Function_6_3E6A")

    OP_8E(0xFE, 0xA76C, 0x0, 0x12110, 0x1388, 0x0)
    OP_8E(0xFE, 0xA4A6, 0x0, 0x110D0, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_3E6A end

    def Function_7_3E9A(): pass

    label("Function_7_3E9A")

    ClearChrFlags(0xFE, 0x1000)
    OP_8E(0xFE, 0xA564, 0x0, 0x101B2, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_7_3E9A end

    def Function_8_3EBB(): pass

    label("Function_8_3EBB")

    OP_8E(0xFE, 0xA622, 0x0, 0x12110, 0x1388, 0x0)
    OP_8E(0xFE, 0xA8A2, 0x0, 0x11044, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_8_3EBB end

    def Function_9_3EEB(): pass

    label("Function_9_3EEB")

    OP_8E(0xFE, 0xA7D0, 0x0, 0x12110, 0x1388, 0x0)
    OP_8E(0xFE, 0xA14A, 0x0, 0x1103A, 0x1388, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_9_3EEB end

    def Function_10_3F1B(): pass

    label("Function_10_3F1B")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x9EE8, 0x0, 0xF456, 0x7D0, 0x0)

    def lambda_3F3C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3F3C)
    OP_8E(0xFE, 0x9EE8, 0xFFFFFE0C, 0xDAC0, 0x7D0, 0x0)
    Return()

    # Function_10_3F1B end

    def Function_11_3F5D(): pass

    label("Function_11_3F5D")

    EventBegin(0x0)
    OP_6D(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(315000, 0)
    OP_6E(230, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x103, 0x80)
    ClearChrFlags(0x103, 0x8)
    SetChrFlags(0x26, 0x4)
    SetChrFlags(0x26, 0x40)
    SetChrPos(0x26, 38290, -100, 67720, 114)
    SetChrChipByIndex(0x27, 17)
    SetChrSubChip(0x27, 0)
    SetChrFlags(0x27, 0x4)
    SetChrFlags(0x27, 0x40)
    SetChrPos(0x27, 39710, 80, 68530, 180)
    SetChrChipByIndex(0x25, 14)
    SetChrSubChip(0x25, 0)
    SetChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x40)
    SetChrPos(0x25, 39690, 40, 66460, 0)
    OP_72(0x1, 0x4)
    SetChrChipByIndex(0x103, 21)
    SetChrSubChip(0x103, 0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 41700, 200, 67710, 225)
    ClearChrFlags(0x2D, 0x80)
    SetChrSubChip(0x2D, 29)
    ClearChrFlags(0x2E, 0x80)
    SetChrSubChip(0x2E, 29)
    SetChrPos(0x2D, 41440, 0, 66610, 15)
    SetChrPos(0x2E, 41090, 0, 66050, 30)

    ChrTalk(    #198
        0x25,
        "……哎、哎呀！？\x02",
    )

    CloseMessageWindow()
    OP_9E(0x25, 0x14, 0x0, 0x1F4, 0xFA0)
    ClearChrFlags(0x25, 0x100)
    SetChrChipByIndex(0x25, 13)
    SetChrPos(0x25, 40480, 0, 66130, 0)
    SetChrChipByIndex(0x25, 13)
    OP_D1(37, 20000, 0, 0, 0)

    def lambda_40D7():
        OP_D1(37, 60000, -15000, -90000, 200)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_40D7)
    OP_51(0x25, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    ClearChrFlags(0x2D, 0x100)
    ClearChrFlags(0x2E, 0x100)
    OP_51(0x2D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4137():
        OP_96(0x2D, 0xA3FC, 0x0, 0x10586, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_4137)

    def lambda_4155():
        OP_D1(45, 30000, -15000, -80000, 200)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_4155)

    def lambda_416F():
        OP_D1(46, 60000, -15000, -135000, 200)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_416F)
    WaitChrThread(0x2D, 0x2)
    OP_51(0x2D, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2D, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2D, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x2E, 0x2)
    OP_51(0x2E, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x27, 1)
    SetChrSubChip(0x103, 1)
    OP_0D()
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x26, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x27, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #199
        0x27,
        "#036F安、安敦老兄！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x26,
        "#743F#1P哎呀，不得了啦！\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_4264():
        OP_6D(41230, 0, 67950, 1000)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4264)

    def lambda_427C():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_427C)
    OP_43(0x26, 0x1, 0x2, 0xC)
    SetChrChipByIndex(0x103, 65535)
    SetChrFlags(0x103, 0x40)
    ClearChrFlags(0x103, 0x4)
    OP_96(0x103, 0xA1E0, 0x0, 0x10662, 0xC8, 0x1388)
    OP_8C(0x103, 180, 0)
    ClearChrFlags(0x27, 0x4)
    SetChrChipByIndex(0x27, 16)
    OP_96(0x27, 0x9E3E, 0x0, 0x10C98, 0x190, 0x1388)
    SetChrChipByIndex(0x27, 36)
    OP_8E(0x27, 0x9F60, 0x0, 0x10C98, 0xFA0, 0x1)
    SetChrSubChip(0x27, 3)
    WaitChrThread(0x25, 0x1)

    ChrTalk(    #201
        0x27,
        "#038F#2P……哎…哎呀……！？\x02",
    )

    OP_9E(0x27, 0x14, 0x0, 0x1F4, 0xFA0)
    CloseMessageWindow()
    OP_59()
    SetChrSubChip(0x27, 0)
    SetChrFlags(0x27, 0x4)
    OP_96(0x27, 0xA3AC, 0xF0, 0x10B94, 0x190, 0xFA0)
    SetChrChipByIndex(0x27, 18)
    OP_51(0x27, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_96(0x27, 0xA4A6, 0xF0, 0x10B94, 0x190, 0xFA0)
    OP_8C(0x103, 0, 400)

    ChrTalk(    #202
        0x103,
        "#025F#1P哎呀～连奥利维尔也……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x26,
        "#743F#1P两个人都振作一点啊！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x80)
    SetChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4422")
    ClearChrFlags(0xF8, 0x80)
    SetChrFlags(0xF8, 0x40)
    ClearChrFlags(0xF8, 0x4)
    SetChrChipByIndex(0xF8, 65535)
    SetChrPos(0xF8, 42530, 1500, 78540, 180)

    label("loc_4422")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4454")
    ClearChrFlags(0xF9, 0x80)
    SetChrFlags(0xF9, 0x40)
    ClearChrFlags(0xF9, 0x4)
    SetChrChipByIndex(0xF9, 65535)
    SetChrPos(0xF9, 42960, 1500, 78910, 180)

    label("loc_4454")

    SetChrChipByIndex(0x101, 65535)
    SetChrPos(0x101, 42860, 1500, 77720, 180)

    def lambda_4470():
        OP_6D(41380, 0, 69390, 3000)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_4470)
    OP_43(0x101, 0x0, 0x2, 0x6)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44A5")
    OP_43(0xF9, 0x0, 0x2, 0x8)
    Jump("loc_44CF")

    label("loc_44A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44BC")
    OP_43(0xF8, 0x0, 0x2, 0x8)
    Jump("loc_44CF")

    label("loc_44BC")

    OP_43(0xF8, 0x0, 0x2, 0x8)
    Sleep(600)
    OP_43(0xF9, 0x0, 0x2, 0x9)

    label("loc_44CF")

    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)

    ChrTalk(    #204
        0x101,
        "#1020F#2P奥、奥利维尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x27,
        "#038F#4P呜……嗯～～嗯……\x02",
    )

    CloseMessageWindow()

    def lambda_4523():
        OP_6D(40560, 0, 66540, 2000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_4523)
    WaitChrThread(0x13, 0x0)
    SetChrPos(0x24, 39760, -500, 61000, 0)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x24, 0x80)

    def lambda_4561():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_4561)
    OP_8E(0x24, 0x9B50, 0x0, 0xFBB8, 0x7D0, 0x0)
    OP_8C(0x24, 50, 400)

    ChrTalk(    #206
        0x24,
        "唉，这样可不行啊……\x02",
    )

    CloseMessageWindow()

    def lambda_45A8():
        OP_6D(41450, 0, 68050, 2500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_45A8)

    def lambda_45C0():

        label("loc_45C0")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_45C0")

    QueueWorkItem2(0x101, 3, lambda_45C0)

    def lambda_45D1():

        label("loc_45D1")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_45D1")

    QueueWorkItem2(0x103, 3, lambda_45D1)

    def lambda_45E2():

        label("loc_45E2")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_45E2")

    QueueWorkItem2(0xF8, 3, lambda_45E2)

    def lambda_45F3():

        label("loc_45F3")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_45F3")

    QueueWorkItem2(0xF9, 3, lambda_45F3)

    def lambda_4604():

        label("loc_4604")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_4604")

    QueueWorkItem2(0x26, 3, lambda_4604)
    OP_8E(0x24, 0xA316, 0x0, 0xFD51, 0x7D0, 0x0)
    OP_8E(0x24, 0xA64A, 0x0, 0x10036, 0x7D0, 0x0)
    OP_8C(0x24, 315, 400)
    WaitChrThread(0x13, 0x0)
    Return()

    # Function_11_3F5D end

    def Function_12_4644(): pass

    label("Function_12_4644")

    ClearChrFlags(0x26, 0x4)
    OP_96(0x26, 0x9380, 0x0, 0x10720, 0x190, 0x1388)
    OP_62(0x26, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x26, 0x9646, 0x0, 0x100CC, 0xBB8, 0x0)
    OP_8E(0x26, 0x9D94, 0x0, 0xFDA2, 0xBB8, 0x0)
    OP_8E(0x26, 0x9EE8, 0x0, 0x10004, 0xBB8, 0x0)
    OP_8C(0x26, 0, 400)
    Return()

    # Function_12_4644 end

    SaveToFile()

Try(main)
