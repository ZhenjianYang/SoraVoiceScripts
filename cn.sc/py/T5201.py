from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T5201   ._SN',
        MapName             = 'Other',
        Location            = 'T5201.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60117",
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
        '约修亚',                               # 9
        '乔丝特',                               # 10
        '吉尔',                                 # 11
        '多伦',                                 # 12
        '白的花束',                             # 13
        '剑',                                   # 14
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
        'ED6_DT27/CH03010 ._CH',             # 00
        'ED6_DT27/CH03100 ._CH',             # 01
        'ED6_DT27/CH03770 ._CH',             # 02
        'ED6_DT27/CH03760 ._CH',             # 03
        'ED6_DT26/CH20264 ._CH',             # 04
        'ED6_DT27/CH03101 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT27/CH03010P._CP',             # 00
        'ED6_DT27/CH03100P._CP',             # 01
        'ED6_DT27/CH03770P._CP',             # 02
        'ED6_DT27/CH03760P._CP',             # 03
        'ED6_DT26/CH20264P._CP',             # 04
        'ED6_DT27/CH03101P._CP',             # 05
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
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
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_1C3",          # 01, 1
        "Function_2_1FC",          # 02, 2
        "Function_3_10F6",         # 03, 3
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1B4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 2)
    Jump("loc_1C2")

    label("loc_1B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_1C2")
    OP_A3(0x10F1)
    Event(0, 3)

    label("loc_1C2")

    Return()

    # Function_0_19A end

    def Function_1_1C3(): pass

    label("Function_1_1C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DF")
    OP_23(0x1C3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x448, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FB")
    OP_23(0x1C3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FB")

    Return()

    # Function_1_1C3 end

    def Function_2_1FC(): pass

    label("Function_2_1FC")

    EventBegin(0x0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_6D(450, -1000, -8810, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(45000, 0)
    OP_6E(500, 0)
    SetChrPos(0x9, -2500, -1000, 14100, 0)
    SetChrPos(0xB, -3480, -1000, 13100, 0)
    SetChrPos(0xA, -1600, -1000, 13100, 0)
    SetChrPos(0x8, -2750, -900, 28300, 0)
    SetChrPos(0xC, -2850, -1000, 28850, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0xC, 0x800)
    SetChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 16)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x10A, 0x80)
    FadeToBright(1000, 0)

    def lambda_2D1():
        OP_6D(-1730, -1000, 28380, 7000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2D1)
    WaitChrThread(0x8, 0x0)
    Fade(500)
    OP_6D(-2180, -1000, 29400, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(1500, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #0
        0x8,
        "黑发的少年",
        (
            "#6P…………………………………\x02\x03",

            "卡琳姐姐……我回来了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 17)
    ClearChrFlags(0xC, 0x80)
    SetChrSubChip(0xC, 7)
    OP_0D()
    Sleep(1000)

    NpcTalk(    #1
        0x9,
        "女孩的声音",
        "#1P喂、喂……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x9,
        "女孩的声音",
        "#1P你跑到哪里去了啊！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_3E3():
        OP_6D(-1650, -1000, 23080, 3500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3E3)

    def lambda_3FB():
        OP_67(0, 9500, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3FB)

    def lambda_413():
        OP_6B(1700, 3500)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_413)
    Sleep(1000)

    def lambda_428():
        OP_8E(0xFE, 0xFFFFF790, 0xFFFFFC18, 0x49B6, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_428)
    Sleep(200)

    def lambda_448():
        OP_8E(0xFE, 0xFFFFFB1E, 0xFFFFFC18, 0x4506, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_448)
    Sleep(600)

    def lambda_468():
        OP_8E(0xFE, 0xFFFFF51A, 0xFFFFFC18, 0x4402, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_468)
    WaitChrThread(0x9, 0x0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #3
        0x9,
        "#415F#6P太好了……终于找到了。\x02",
    )

    CloseMessageWindow()

    def lambda_4C8():
        OP_8E(0xFE, 0xFFFFF510, 0xFFFFFC18, 0x64FA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4C8)

    def lambda_4E3():
        OP_6D(-1740, -1000, 27700, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4E3)

    def lambda_4FB():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_4FB)
    Sleep(100)

    def lambda_518():
        OP_8E(0xFE, 0xFFFFF8F8, 0xFFFFFC18, 0x5F8C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_518)
    Sleep(400)

    def lambda_538():
        OP_8E(0xFE, 0xFFFFF290, 0xFFFFFC18, 0x5D48, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_538)
    WaitChrThread(0x9, 0x1)
    Sleep(500)

    ChrTalk(    #4
        0x9,
        (
            "#210F#6P真是的，别再让我们担心了！\x01",
            "一个人跑到这种地方来做什么嘛。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #5
        0x8,
        "#1035F#5P呵……为什么要来这里吗……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #6
        0x8,
        (
            "#1030F#5P只是一点私人事情，\x01",
            "没必要叫你们一起。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x9,
        (
            "#212F#6P真…真是一点都不可爱！\x02\x03",

            "#214F我们很担心，\x01",
            "到处在找你呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xA,
        (
            "#200F#4P而且要我们对你如此神秘的举动\x01",
            "视而不见也不现实嘛。\x02\x03",

            "据我观察，这里的村落似乎已经\x01",
            "荒废１０年之久了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xB,
        (
            "#197F#6P我们直到３年前都还一直\x01",
            "居住在帝国北部的领地……\x02\x03",

            "不过却从没听说过南部\x01",
            "有村庄被废弃啊。\x02\x03",

            "#190F这村子叫什么名字？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        "#1033F#5P……………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    Sleep(500)

    ChrTalk(    #11
        0x8,
        (
            "#1035F#5P……『哈梅尔』。\x01",
            "这是它曾经的名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x9,
        (
            "#213F#6P哈梅尔……\x01",
            "从来没听过这名字啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, -180, 400)
    Sleep(300)

    ChrTalk(    #13
        0x9,
        "#212F#5P吉尔哥哥，你听过没有？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xA,
        (
            "#204F#4P没……\x01",
            "我也从没听说过。\x02\x03",

            "#207F大哥呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xB,
        (
            "#192F#6P嗯……等我想想……\x02\x03",

            "#198F很早以前，帝国政府好像\x01",
            "发布过一个通知……\x02\x03",

            "#197F……不行，完全想不起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        "#413F#5P什么嘛～竟然连大哥都不知道。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #17
        0x8,
        (
            "#1031F#5P……我的事情已经办完了。\x02\x03",

            "把你们也牵连到无关的麻烦中，\x01",
            "真是非常抱歉。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)
    Sleep(300)

    ChrTalk(    #18
        0x9,
        (
            "#413F#6P这点小事算不了什么，不过……\x02\x03",

            "#212F你的态度和初次见面时\x01",
            "相比变化也太大了吧？\x02\x03",

            "难道是在耍我们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#1035F#5P……这种话好像\x01",
            "不应该从你口中说出啊。\x02\x03",

            "#1031F初次见面时\x01",
            "你的演技不是\x01",
            "更精彩吗？\x02\x03",

            "我也和你一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #20
        0x9,
        (
            "#216F#6P呜……\x02\x03",

            "那、那么说的话，现在这样子\x01",
            "难道才是你真正的本性！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#1033F#5P……你这样想也可以。\x02\x03",

            "#1035F至少现在的我，\x01",
            "已经和游击士没有任何关系了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        (
            "#203F#4P呼……虽然不知道具体原因，\x01",
            "不过看来在你身上发生了不少事情啊。\x02\x03",

            "#200F算了，既然你能对我们如此坦诚，\x01",
            "我们自然也可以相信你。\x02\x03",

            "总比大家互相猜疑好的多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "#1034F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xB,
        (
            "#490F#6P毕竟当初被王国军\x01",
            "追击的时候全靠你的帮忙\x01",
            "才能顺利逃脱。\x02\x03",

            "看在这个的份上，你这小鬼头的傲慢态度\x01",
            "我就不多计较了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#1035F#5P……没有那个必要。\x02\x03",

            "#1031F我帮助你们，\x01",
            "只不过是想利用\x01",
            "你们而已。\x02\x03",

            "想还我人情的话\x01",
            "以后多尽力就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "#198F#6P哼，真是个嘴硬的臭小子。\x02\x03",

            "#490F算了，反正你的提议\x01",
            "对我们来说也是迟早要做的事情。\x02\x03",

            "今后大家就互相帮忙，让我们也好好\x01",
            "利用你的力量吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#1031F#5P……就是这样。\x02\x03",

            "#1035F和我共同行动本来\x01",
            "就是件很危险的事情。\x02\x03",

            "为了达成目标\x01",
            "大家只能相互协助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "#212F#6P真…真是一点都不可爱啊！\x02\x03",

            "#215F这种讨厌的家伙\x01",
            "我当时竟然还会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        "#1034F#5P……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        (
            "#214F#6P没什么！\x01",
            "别用那种奇怪的眼神看我！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        (
            "#203F#4P好啦好啦，乔丝特。\x02\x03",

            "#200F不管怎么说，\x01",
            "在达成各自的目的之前\x01",
            "我们就是同伴了。\x02\x03",

            "#202F请多多关照了，约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#1030F#5P……………………………\x02\x03",

            "#1035F嗯，请多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xB,
        (
            "#490F#6P哟……\x01",
            "我们也该出发了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        "#1031F#5P嗯……回去吧。\x02",
    )

    CloseMessageWindow()

    def lambda_F36():
        OP_6D(-1950, -1000, 30090, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F36)

    def lambda_F4E():
        OP_67(0, 7140, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F4E)

    def lambda_F66():
        OP_6B(1840, 1500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_F66)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    ChrTalk(    #35
        0x8,
        (
            "#1032F#6P回到利贝尔──\x01",
            "那片被阴影笼罩的大地。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_AD(0x2400AD, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x1040)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x122), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存进度】\x01",        # 0
            "【进入下一章】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1041")
    ShowSaveMenu()

    label("loc_1041")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_20(0x1388)
    OP_AE(0xC8)
    OP_24(0x1C3, 0x5F)
    Sleep(200)
    OP_24(0x1C3, 0x5A)
    Sleep(200)
    OP_24(0x1C3, 0x55)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x4B)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x41)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x37)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x2D)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x23)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    OP_21()
    OP_23(0x1C3)
    Sleep(1000)
    OP_A3(0x1040)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/C4302   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1FC end

    def Function_3_10F6(): pass

    label("Function_3_10F6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_22(0x1C3, 0x1, 0x46)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x101, -2830, -1000, 27070, 0)
    SetChrPos(0x102, -3640, -960, 28120, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_6D(5280, -1000, 36730, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(1500, 0)
    OP_6C(45000, 0)
    OP_6E(500, 0)
    OP_D2(0x260201, 0x260206, 0x6)
    OP_D2(0x260202, 0x260207, 0x7)
    OP_D2(0x260203, 0x260208, 0x8)
    OP_D2(0x26022E, 0x260231, 0x9)
    OP_D2(0x260235, 0x26023A, 0xA)
    OP_D2(0x26022E, 0x260231, 0xB)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x101, 7)
    SetChrChipByIndex(0x102, 6)
    OP_7E(0xFD44, 0xFAD8, 0x96, 0x73, 0x1)
    FadeToBright(1000, 0)

    def lambda_11EF():
        OP_6D(-2160, -1000, 29130, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11EF)

    def lambda_1207():
        OP_67(0, 7350, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1207)

    def lambda_121F():
        OP_6B(1790, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_121F)

    def lambda_122F():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_122F)

    def lambda_123F():
        OP_6E(444, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_123F)
    WaitChrThread(0x101, 0x0)
    Sleep(300)

    ChrTalk(    #36
        0x102,
        (
            "#1035F#6P……姐姐，我回来了。\x02\x03",

            "#1041F这个……\x01",
            "是我替莱维带来给你的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_99(0x102, 0x0, 0x6, 0x3E8)
    Fade(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x102, 7)
    SetChrChipByIndex(0xD, 6)
    SetChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x80)
    SetChrSubChip(0xD, 12)
    SetChrPos(0xD, -3650, -1100, 28360, 0)
    ClearChrFlags(0xD, 0x80)
    OP_0D()
    Sleep(1000)
    OP_99(0x102, 0x8, 0xB, 0x5DC)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x1)
    Sleep(500)

    ChrTalk(    #37
        0x102,
        "#1053F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1017F太好了啊，约修亚。\x02\x03",

            "莱维他……\x01",
            "现在也一定会很高兴吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 400)
    Sleep(300)

    ChrTalk(    #39
        0x102,
        (
            "#1035F#5P……嗯……\x02\x03",

            "#1043F莱维和姐姐之间的感情\x01",
            "一直都非常好……\x02\x03",

            "#1054F当时，他们一定曾有过\x01",
            "走到一起的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1003F是吗……\x02\x03",

            "#1025F那个…让我也来\x01",
            "和卡琳姐姐打个招呼可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        "#1053F#5P嗯……当然。\x02",
    )

    CloseMessageWindow()

    def lambda_145D():
        OP_6D(-2620, -790, 29440, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_145D)

    def lambda_1475():
        OP_8F(0xFE, 0xFFFFF060, 0xFFFFFC18, 0x6B58, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1475)
    Sleep(100)
    OP_8F(0x101, 0xFFFFF588, 0xFFFFFC22, 0x6D88, 0x3E8, 0x0)
    WaitChrThread(0x102, 0x2)

    def lambda_14AE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14AE)
    WaitChrThread(0x102, 0x1)
    Sleep(500)

    ChrTalk(    #42
        0x101,
        (
            "#1012F#4P初次见面，卡琳姐姐。\x02\x03",

            "#1006F我是艾丝蒂尔。\x01",
            "艾丝蒂尔·布莱特。\x02\x03",

            "是您弟弟的家人，也就是姐姐……#2990W #20W \x01",
            "#1013F基…基本上也可以算是女朋友吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 11)
    SetChrSubChip(0x102, 0)
    OP_99(0x102, 0x0, 0x2, 0x5DC)
    Sleep(100)

    ChrTalk(    #43
        0x102,
        (
            "#1048F#6P真是的……\x01",
            "为什么还要加上个『基本上』啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 0)
    OP_99(0x101, 0x0, 0x2, 0x5DC)
    Sleep(100)

    ChrTalk(    #44
        0x101,
        (
            "#1013F#5P可、可是……\x01",
            "人家还是有点儿不习惯嘛……\x02\x03",

            "总觉得……\x01",
            "有些难为情呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        (
            "#1052F#6P真是的……\x02\x03",

            "#1054F哈哈，\x01",
            "不过这样才像是艾丝蒂尔呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1019F#5P唔……什么嘛。\x01",
            "你竟然摆出那种若无其事的样子。\x02\x03",

            "不过话说回来，约修亚。你呀，在两人\x01",
            "独处的时候…总是很大胆呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_99(0x101, 0x2, 0x0, 0x7D0)
    SetChrChipByIndex(0x101, 7)
    SetChrSubChip(0x101, 0)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    def lambda_171D():
        OP_99(0x102, 0x2, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_171D)

    ChrTalk(    #47
        0x101,
        (
            "#1013F#4P啊，对不起！\x01",
            "在问候姐姐的时候竟然说起这样的……\x02\x03",

            "#1017F那个……\x01",
            "今天，我和约修亚一起回他的故乡，\x01",
            "特意来向姐姐您问候的。\x02\x03",

            "今后也请您多多关照了……\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 8)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x2)
    OP_0D()
    OP_99(0x101, 0x0, 0x8, 0x3E8)
    Fade(250)
    SetChrSubChip(0x101, 9)
    SetChrChipByIndex(0xC, 8)
    SetChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x80)
    SetChrSubChip(0xC, 12)
    SetChrPos(0xC, -2670, -900, 28900, 0)
    ClearChrFlags(0xC, 0x80)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #48
        0x101,
        "#1012F#4P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#1035F#6P……谢谢你，艾丝蒂尔。\x02\x03",

            "#1041F姐姐她……\x01",
            "一定会很高兴的。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0xA, 0xB, 0x514)
    Sleep(200)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x101, 0x2)

    def lambda_18B9():
        OP_6D(-2830, -780, 28720, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18B9)
    OP_8F(0x101, 0xFFFFF524, 0xFFFFFC18, 0x6AFE, 0x3E8, 0x0)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 11)
    SetChrSubChip(0x102, 0)
    OP_99(0x102, 0x0, 0x2, 0x5DC)
    Sleep(100)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x101, 0x0)
    Sleep(200)

    ChrTalk(    #50
        0x101,
        (
            "#1008F#2P哈哈……\x01",
            "那真是太好了啊，不过…\x02\x03",

            "#1007F现在的我还是很孩子气，\x01",
            "好像总是给人一种靠不住的感觉……\x02\x03",

            "真不知道卡琳姐姐会不会认为\x01",
            "我没资格做他弟弟的女朋友啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#1054F#6P哈哈，你想得太多了啊。\x02\x03",

            "#1053F姐姐如果活着的话，\x01",
            "肯定会和你非常投缘的。\x02\x03",

            "因为你们的性格有着鲜明的对比啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 11)
    SetChrSubChip(0x101, 24)
    Sleep(300)

    ChrTalk(    #52
        0x101,
        "#1016F#2P嘻嘻嘻～是吗……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 25)
    Sleep(500)

    ChrTalk(    #53
        0x101,
        (
            "#1019F#2P……唔？\x01",
            "怎么觉得这话怪怪的。\x02\x03",

            "你不会是想说我没有\x01",
            "卡琳姐姐那样\x01",
            "坚强沉稳吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        (
            "#1052F#6P唔……嗯……\x01",
            "虽然你内心很坚强……\x02\x03",

            "#1054F不过说到沉稳嘛，\x01",
            "确实有些……\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #55
        0x101,
        "#1007F#2P哼哼哼……\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        (
            "#1041F#6P不过，那不是也很好嘛。\x02\x03",

            "总是乐观开朗、积极向上，\x01",
            "像太阳一样灿烂耀眼……\x02\x03",

            "#1049F所以，\x01",
            "我最喜欢的女孩就是这样的了。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(300)

    ChrTalk(    #57
        0x101,
        "#1004F#2P#3S！！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 90, 600)
    Sleep(500)

    ChrTalk(    #58
        0x101,
        (
            "#1013F#5P真、真是的！约……\x02\x03",

            "约修亚你总是这样随口就说出\x01",
            "一些让人难为情的话啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        "#1044F#6P哎？你不高兴吗？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 600)
    Sleep(500)

    ChrTalk(    #60
        0x101,
        (
            "#1019F#2P#3S高兴！高兴！非常高兴！\x01",
            "这样总可以了吧！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        "#1052F#6P你怎么又突然生气……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1007F#2P……嗯！好了！已经问候过姐姐了，\x01",
            "我们差不多也该出发了！\x02\x03",

            "再在这里喋喋不休说个没完的话，\x01",
            "姐姐大概要烦死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#1044F#6P啊……嗯。\x02\x03",

            "#1043F…………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1015F#2P嗯？怎么了？\x02",
    )

    CloseMessageWindow()
    OP_99(0x102, 0x2, 0x0, 0x5DC)
    Sleep(500)

    ChrTalk(    #65
        0x102,
        (
            "#1043F#6P……那个…这样真的好吗？\x02\x03",

            "和我一起\x01",
            "离开利贝尔……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1004F#2P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        (
            "#1035F#6P为了偿还在『结社』时代犯下的罪过，\x01",
            "周游大陆各地其实只是我一个人的事情。\x02\x03",

            "也为了变得像莱维一样强，\x01",
            "我要再次踏上旅程。\x02\x03",

            "#1043F把你也牵连进来，真的好吗？\x01",
            "老实说……我还是有点迷茫啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 11)
    SetChrSubChip(0x101, 11)
    OP_99(0x101, 0xB, 0xD, 0x708)
    Sleep(500)

    ChrTalk(    #68
        0x101,
        (
            "#1007F#2P真是的……\x01",
            "你怎么还说这种话。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x102, 0x0, 0x2, 0x5DC)
    Sleep(500)

    ChrTalk(    #69
        0x102,
        "#1044F#6P哎……\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0xD, 0xF, 0x5DC)
    Sleep(300)

    ChrTalk(    #70
        0x101,
        (
            "#1006F#2P雷格纳特不是说过吗，\x01",
            "今后在这个世界中也许还会发生\x01",
            "很多很多的大事。\x02\x03",

            "『噬身之蛇』肯定还会\x01",
            "继续在其他地方制造乱子。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0xF, 0x11, 0x5DC)
    Sleep(300)

    ChrTalk(    #71
        0x101,
        (
            "#1029F#2P为了应付这一切，我们还要继续锻炼，\x01",
            "要超越老爸才行。\x02\x03",

            "因此对我来说，\x01",
            "这样的旅行也是很有必要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        (
            "#1054F超越父亲……\x01",
            "你又在说大话了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x11, 0x13, 0x5DC)
    Sleep(300)

    ChrTalk(    #73
        0x101,
        "#1006F#2P目标本来就是要定大一些嘛！\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x13, 0x15, 0x5DC)
    Sleep(300)

    ChrTalk(    #74
        0x101,
        (
            "#1012F#2P我和莱维也做过约定的，\x01",
            "还有玲的去向我也很在意。\x02\x03",

            "总之，到没有涉足的土地旅行\x01",
            "也是一种享受呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x15, 0x17, 0x5DC)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #75
        0x101,
        "#1008F#2P#1000F而且……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(100)

    def lambda_2209():
        OP_6D(-3300, -780, 28870, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2209)
    SetChrFlags(0x101, 0x40)
    OP_8E(0x101, 0xFFFFF31C, 0xFFFFFC18, 0x6B08, 0x3E8, 0x0)
    Sleep(100)
    SetChrFlags(0x102, 0x800)
    ClearChrFlags(0x102, 0x1)
    SetChrFlags(0x101, 0x80)
    SetChrSubChip(0x102, 3)
    OP_99(0x102, 0x3, 0x7, 0x5DC)
    Sleep(500)

    ChrTalk(    #76
        0x102,
        "#1044F#6P艾、艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#1006F#2P最重要的是，我和约修亚在一起\x01",
            "难道还需要什么理由吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        (
            "#1044F#6P啊……\x02\x03",

            "#1040F…………………………………\x02\x03",

            "#1053F嗯……你说的对。\x02\x03",

            "#1054F根本就……不需要。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1016F#2P对吧？\x02\x03",

            "#1017F约修亚真是的，\x01",
            "这种事情竟然还要我提醒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x102,
        "#1049F#6P哈哈……是啊。\x02",
    )

    CloseMessageWindow()

    def lambda_238A():
        OP_99(0xFE, 0x8, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_238A)

    def lambda_239A():
        OP_6D(-4070, -1000, 40590, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_239A)

    def lambda_23B2():
        OP_67(0, 7350, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23B2)

    def lambda_23CA():
        OP_6B(1790, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_23CA)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x400, 0x0, 0xFDE4, 0x400, 0x400, 0x0, 0x0, 0x280, 0x400, 0xFFFFFF, 0x0, "C_VIS177._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x400, 0x0, 0xFDE4, 0x400, 0x400, 0x0, 0x0, 0x280, 0x400, 0xFFFFFF, 0x0, "C_VIS178._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x7, 0, -386000, 3000)
    OP_C7(0x0, 0x0, 0x0)
    Sleep(500)
    OP_C6(0x1, 0x3, -1, 0, 0)
    SetMessageWindowPos(80, 340, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #81
        (
            "\x07\x00──走吧！艾丝蒂尔。\x02\x03",

            "虽然还不知道前方的道路\x01",
            "会通向何处……\x02\x03",

            "不过，我相信我们一定可以\x01",
            "在旅途里找到属于自己的方向。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(340, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #82
        (
            "\x07\x00嗯……！\x02\x03",

            "迈开我们的脚步，\x01",
            "一步一步向前走吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x7, 0, 0, 4000)
    OP_C7(0x0, 0x1, 0x0)
    Sleep(1000)
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS179._CH")
    OP_C6(0x2, 0x3, -1, 3000, 0)
    Sleep(3500)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_56(0x2)
    OP_C6(0x2, 0x3, 16777215, 3000, 0)
    Sleep(4000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_40(0x31, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x417, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2609")
    OP_A2(0x22B3)

    label("loc_2609")

    OP_A2(0x2242)
    OP_C4(0x0, 0x10)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x12B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x1B, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x31, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2636")
    OP_A2(0x22B3)

    label("loc_2636")

    OP_A2(0x22AE)
    OP_A2(0x22B5)

    Menu(
        0,
        200,
        180,
        0,
        (
            "【储存通关存档】\x01",      # 0
            "【回到标题画面】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267D")
    ShowSaveMenu()
    EventBegin(0x4)

    label("loc_267D")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x1, 0x10)
    OP_A3(0x2242)
    FadeToDark(0, 0, -1)
    OP_20(0xBB8)
    SetMapFlags(0x2000000)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    Sleep(200)
    OP_24(0x1C3, 0xA)
    Sleep(200)
    OP_23(0x1C3)
    OP_21()
    Sleep(3000)
    OP_B4(0x1)
    Return()

    # Function_3_10F6 end

    SaveToFile()

Try(main)
