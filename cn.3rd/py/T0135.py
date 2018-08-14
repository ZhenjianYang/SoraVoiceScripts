from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0135   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0135.x',
        MapIndex            = 7,
        MapDefaultBGM       = "ed60084",
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
        '雪拉扎德',                             # 9
        '奥利维尔',                             # 10
        '爱娜',                                 # 11
        '福克纳',                               # 12
        '料理',                                 # 13
        '料理',                                 # 14
        '酒瓶',                                 # 15
        '酒瓶',                                 # 16
        '玻璃杯',                               # 17
        '玻璃杯',                               # 18
        '玻璃杯',                               # 19
        '玻璃杯',                               # 20
        '玻璃杯',                               # 21
        '目标用照相机',                         # 22
        '',                                     # 23
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
        'ED6_DT07/CH00023 ._CH',             # 00
        'ED6_DT07/CH00033 ._CH',             # 01
        'ED6_DT07/CH02560 ._CH',             # 02
        'ED6_DT07/CH01270 ._CH',             # 03
        'ED6_DT06/CH20049 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
        'ED6_DT07/CH00020 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH00023P._CP',             # 00
        'ED6_DT07/CH00033P._CP',             # 01
        'ED6_DT07/CH02560P._CP',             # 02
        'ED6_DT07/CH01270P._CP',             # 03
        'ED6_DT06/CH20049P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
        'ED6_DT07/CH00020P._CP',             # 07
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
        X                   = 34500,
        Z                   = 0,
        Y                   = 75200,
        Direction           = 90,
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
        X                   = 40550,
        Z                   = 700,
        Y                   = 66950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65541,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39700,
        Z                   = 700,
        Y                   = 67470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262149,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39300,
        Z                   = 700,
        Y                   = 67950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835013,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39100,
        Z                   = 700,
        Y                   = 67050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966085,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 38900,
        Z                   = 700,
        Y                   = 68000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835013,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40550,
        Z                   = 700,
        Y                   = 68000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835013,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 38950,
        Z                   = 600,
        Y                   = 67600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327686,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40150,
        Z                   = 600,
        Y                   = 67950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327686,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40100,
        Z                   = 600,
        Y                   = 66800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65542,
        ChipIndex           = 0x6,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_2C0",          # 01, 1
        "Function_2_2C1",          # 02, 2
        "Function_3_C94",          # 03, 3
        "Function_4_CDC",          # 04, 4
        "Function_5_D44",          # 05, 5
        "Function_6_D75",          # 06, 6
        "Function_7_258C",         # 07, 7
        "Function_8_25DA",         # 08, 8
        "Function_9_2617",         # 09, 9
        "Function_10_2674",        # 0A, 10
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BF")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_2BF")

    Return()

    # Function_0_2AA end

    def Function_1_2C0(): pass

    label("Function_1_2C0")

    Return()

    # Function_1_2C0 end

    def Function_2_2C1(): pass

    label("Function_2_2C1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x10, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 39580, 200, 68570, 180)
    SetChrFlags(0x11, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 39710, 200, 66250, 0)
    SetChrFlags(0x12, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 38200, 0, 67800, 121)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x2)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_6D(37640, 0, 68540, 0)
    OP_67(0, 5060, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(302000, 0)
    OP_6E(286, 0)
    OP_20(0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0 op#5
        "\x07\x00#150W七耀历１２０２年　地方都市洛连特#20W――\x05\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_56(0x0)
    Sleep(1500)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #1
        "\x07\x00#70W#1S……雪拉扎德……#40W\x02",
    )

    Jump("loc_430")

    label("loc_430")

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #2
        "\x07\x00#40W#2S……雪拉扎德！#20W\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_46A():
        OP_6B(2960, 7000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_46A)
    FadeToBright(3000, 0)
    Sleep(1500)

    ChrTalk(    #3
        0x10,
        "#026F嗯～………………？\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_0D()

    def lambda_4AE():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4AE)
    Sleep(1000)
    SetChrSubChip(0x10, 1)
    Sleep(800)
    SetChrSubChip(0x10, 0)
    Sleep(100)
    SetChrSubChip(0x10, 2)
    Sleep(800)
    SetChrSubChip(0x10, 0)
    Sleep(100)
    WaitChrThread(0x1D, 0x0)
    Sleep(500)

    ChrTalk(    #4
        0x10,
        "#029F哎呀？　……这里是哪……？\x02",
    )

    CloseMessageWindow()
    OP_1D(0xBF)
    Sleep(500)

    ChrTalk(    #5
        0x12,
        (
            "#743F#5P没事吗？\x01",
            "你是不是喝多了点？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#025F啊……………………\x01",
            "做了个令人怀念的梦……\x02\x03",

            "那时候的我，\x01",
            "还真是年轻呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x12,
        (
            "#741F#5P呵呵，\x01",
            "好像很久没醉得这么舒服了呢。\x02\x03",

            "#740F不过事到如今说这种\x01",
            "上年纪似的话也无济于事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "#038F#100W就、就是嘛\x01",
            "写亚乍得君……\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x11, 0x14, 0x0, 0x1F4, 0x7D0)
    Sleep(500)
    OP_9E(0x11, 0x14, 0x0, 0x1F4, 0xBB8)
    Sleep(1000)
    Fade(500)
    SetChrChipByIndex(0x11, 1)
    ClearChrFlags(0x11, 0x2)
    Sleep(500)

    ChrTalk(    #9
        0x11,
        (
            "#038F#60W我我、我啊……\x01",
            "…………我哦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x12,
        (
            "#743F#5P哎呀奥利维尔，\x01",
            "你已经起来了？\x02\x03",

            "#741F呵呵，来一杯醒醒神吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0xF9, 0x0, 0x64)
    Fade(1000)
    SetChrSubChip(0x1C, 5)
    OP_0D()
    Sleep(300)

    def lambda_749():
        OP_9E(0x11, 0xF, 0x0, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_749)

    ChrTalk(    #11
        0x11,
        "#036F#100W不、#20W不要……不要……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        "#026F你在说什么鬼话啊。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x10, 2)
    Sleep(500)

    ChrTalk(    #13
        0x10,
        (
            "#520F福克纳，\x01",
            "再给奥利维尔加一瓶～！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    def lambda_80C():
        OP_9E(0x11, 0xF, 0x0, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_80C)

    ChrTalk(    #14
        0x11,
        "#038F#60W啊、啊呜啊呜…………（失去意识）\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #15
        0x10,
        (
            "#029F啊，那家伙又溜掉了。\x02\x03",

            "啧……没办法了。\x01",
            "我亲自来动手吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x11, 0x1, 0x0, 0x5)
    OP_59()
    Sleep(300)
    Fade(800)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 38560, 0, 68740, 270)
    OP_22(0x1A, 0x0, 0x64)
    OP_0D()

    def lambda_8E6():
        OP_6D(35620, 0, 70400, 6000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_8E6)
    OP_43(0x10, 0x1, 0x0, 0x3)
    Sleep(500)

    ChrTalk(    #16
        0x10,
        (
            "#520F#12P难道就没有什么\x01",
            "更带劲的家伙吗～……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x1D, 0x0)

    ChrTalk(    #17
        0x10,
        "#521F哦，找到白兰地了！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x12,
        (
            "#741F#1P不行哦，雪拉扎德。\x02\x03",

            "要提神的话，\x01",
            "用一点轻度的\x01",
            "果酒就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        "#520F那就两个一起来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        "#038F#40W#3P不要……我会死的……\x02",
    )

    CloseMessageWindow()

    def lambda_A1F():
        OP_6D(37640, 0, 68540, 6000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_A1F)
    OP_43(0x10, 0x1, 0x0, 0x4)
    Sleep(1000)

    ChrTalk(    #21
        0x10,
        "#026F话说回来，爱娜……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x1D, 0x0)
    Sleep(300)

    ChrTalk(    #22
        0x10,
        "#027F在那之后你喝了多少杯啊。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_22(0x82, 0x0, 0x64)
    OP_0D()
    Sleep(500)
    OP_44(0x11, 0x1)

    ChrTalk(    #23
        0x12,
        "#743F#11P在那之后？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#521F哎呀，\x01",
            "就是我们俩第一次喝酒的时候啦！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x172, 0x0, 0x64)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05雪拉扎德将酒倒在奥利维尔头上。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0xF9, 0x0, 0x64)
    OP_44(0x11, 0xFF)

    def lambda_B68():
        OP_9E(0xFE, 0x19, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_B68)

    def lambda_B82():
        OP_9F(0xFE, 0xFF, 0x0, 0x0, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_B82)
    Sleep(2300)

    ChrTalk(    #26
        0x12,
        (
            "#741F#11P雪拉扎德真是的，\x01",
            "倒错地方了吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#029F哎呀呀？\x02\x03",

            "啊，真的……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BFF():
        OP_9E(0xFE, 0x14, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_BFF)
    Sleep(800)

    ChrTalk(    #28
        0x11,
        "#038F呜……呜…………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x20C, 0x0, 0x64)
    Fade(500)
    SetChrChipByIndex(0x11, 4)
    SetChrFlags(0x11, 0x2)
    Sleep(500)

    def lambda_C5E():
        OP_6B(2760, 4000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_C5E)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    OP_44(0x1D, 0x0)
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_2C1 end

    def Function_3_C94(): pass

    label("Function_3_C94")


    def lambda_C9A():
        OP_8E(0xFE, 0x8318, 0x0, 0x10D60, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_C9A)
    WaitChrThread(0x10, 0x0)

    def lambda_CBA():
        OP_8E(0xFE, 0x83B8, 0x0, 0x12250, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_CBA)
    WaitChrThread(0x10, 0x0)
    OP_8C(0x10, 270, 500)
    Return()

    # Function_3_C94 end

    def Function_4_CDC(): pass

    label("Function_4_CDC")


    def lambda_CE2():
        OP_8E(0xFE, 0x8318, 0x0, 0x10D60, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_CE2)
    WaitChrThread(0x10, 0x0)

    def lambda_D02():
        OP_8E(0xFE, 0x8D18, 0x0, 0x1093C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_D02)
    WaitChrThread(0x10, 0x0)

    def lambda_D22():
        OP_8E(0xFE, 0x9664, 0x0, 0x102E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_D22)
    WaitChrThread(0x10, 0x0)
    OP_8C(0x10, 90, 500)
    Return()

    # Function_4_CDC end

    def Function_5_D44(): pass

    label("Function_5_D44")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D74")
    Sleep(1500)

    def lambda_D58():
        OP_9E(0x11, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_D58)
    Sleep(1000)
    Jump("Function_5_D44")

    label("loc_D74")

    Return()

    # Function_5_D44 end

    def Function_6_D75(): pass

    label("Function_6_D75")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x10, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 39580, 200, 68570, 180)
    SetChrFlags(0x11, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 39710, 200, 66250, 0)
    SetChrFlags(0x12, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 38200, 0, 67800, 121)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_6D(37640, 0, 68540, 0)
    OP_67(0, 5070, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(302000, 0)
    OP_6E(286, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #29
        0x11,
        (
            "#030F唔～，不愧是洛连特。\x02\x03",

            "用时令蔬菜做的料理\x01",
            "简直就是绝品。\x02\x03",

            "真是堪比帝都\x01",
            "三星餐厅的味道啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        "#020F#2P哎呀，你喜欢吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        (
            "#030F呵，当然了。\x02\x03",

            "令我爱不释口的\x01",
            "美酒和美食。\x02\x03",

            "还有这样两位仿如\x01",
            "地上的女神般的美女\x01",
            "陪伴在身侧嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x12,
        (
            "#740F#5P呵呵……\x02\x03",

            "和听说的一样，\x01",
            "真是能说会道呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#020F爱娜也要小心哦。\x02\x03",

            "这家伙啊，\x01",
            "真是没有一点分寸的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 2)
    Sleep(200)

    def lambda_FBC():
        OP_6D(35710, 0, 71540, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_FBC)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #34
        0x10,
        (
            "#020F#6P啊，福克纳！\x02\x03",

            "葡萄酒不够了哦。\x01",
            "麻烦再来两三瓶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x12,
        (
            "#740F#5P还要科涅克白兰地。\x01",
            "最好是帝国出产的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 135, 400)

    ChrTalk(    #36
        0x13,
        "#5P是、是！\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x13, 225, 400)
    OP_8E(0x13, 0x8476, 0x0, 0x122D2, 0xBB8, 0x0)
    OP_8E(0x13, 0x8188, 0x0, 0x12228, 0xBB8, 0x0)

    def lambda_10A4():
        OP_6D(37640, 0, 68540, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_10A4)
    WaitChrThread(0x0, 0x0)
    Sleep(200)
    OP_62(0x11, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #37
        0x11,
        (
            "#030F我、我说你们两个……\x02\x03",

            "是不是发飙过头了？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrSubChip(0x10, 0)
    Sleep(200)

    ChrTalk(    #38
        0x10,
        (
            "#020F#2P是吗？\x02\x03",

            "这次一直在说话，\x01",
            "算是喝得够慢的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x12,
        (
            "#740F#5P没关系啦。\x01",
            "慢慢喝吧。\x02\x03",

            "哎呀，不过……\x02\x03",

            "奥利维尔先生的\x01",
            "杯子空了呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0xF9, 0x0, 0x64)
    Fade(1000)
    SetChrSubChip(0x1C, 5)
    OP_0D()
    Sleep(300)

    ChrTalk(    #40
        0x11,
        (
            "#030F哈、哈哈……\x01",
            "多谢关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x13, 0x0, 0x0, 0xA)
    WaitChrThread(0x13, 0x0)

    ChrTalk(    #41
        0x13,
        "#5P久、久等了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_0D()
    Sleep(300)

    ChrTalk(    #42
        0x12,
        "#740F#2P谢谢。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x13, 0x1, 0x0, 0x9)
    Sleep(300)

    ChrTalk(    #43
        0x12,
        (
            "#740F#5P奥利维尔先生，\x01",
            "科涅克你要喝纯的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        "#030F#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x12,
        (
            "#740F#5P抱歉。\x01",
            "刚才总是让你喝葡萄酒。\x02\x03",

            "你是帝国的人嘛，\x01",
            "一定喜欢蒸馏酒吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        (
            "#020F#2P啊～，原来如此。\x02\x03",

            "我就说怎么这么慢呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        (
            "#030F#6P咳、咳咳……\x02\x03",

            "对、对了雪拉君……\x02\x03",

            "你和这位爱娜小姐\x01",
            "交情很深吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        (
            "#020F#2P那是当然了。\x02\x03",

            "从我还是准游击士的时候\x01",
            "我们就认识了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x11,
        (
            "#030F#6P哦……\x01",
            "好像很有趣呢。\x02\x03",

            "不介意的话\x01",
            "能不能说给我听呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x12,
        (
            "#740F#5P好啊，\x01",
            "第一次见面是在六年前的王都――\x02\x03",

            "我接受了保镖的委托\x01",
            "前往去协会的时候。\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x240074, 0x0, 0x0, 0x190)
    Sleep(1000)
    FadeToDark(0, 0, -1)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #51
        (
            "#020F那时候，\x01",
            "已经是准游击士的我偶然待在王都的支部。\x02\x03",

            "然后接受了委托，\x01",
            "结果来了个看起来\x01",
            "和事件完全无缘的大小姐。\x02",
        )
    )

    Jump("loc_14EB")

    label("loc_14EB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #52
        (
            "#030F唔，\x01",
            "爱娜小姐遇到什么麻烦了吗？\x02",
        )
    )

    Jump("loc_153A")

    label("loc_153A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("爱娜")

    AnonymousTalk(    #53
        (
            "#740F身为资产家的祖父\x01",
            "因病去世了。\x02\x03",

            "财产全部留给孙女爱娜……\x01",
            "还留下这么随便的遗嘱。\x02",
        )
    )

    Jump("loc_15A8")

    label("loc_15A8")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #54
        (
            "#020F嗯，接下来就是老段子啦。\x02\x03",

            "不知道从哪里涌来的亲戚\x01",
            "开始找爱娜的麻烦。\x02\x03",

            "好像还有人\x01",
            "不择手段想让她放弃继承权。\x02",
        )
    )

    Jump("loc_163C")

    label("loc_163C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #55
        "#030F呼，这性质可真是恶劣。\x02",
    )

    Jump("loc_167C")

    label("loc_167C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("爱娜")

    AnonymousTalk(    #56
        (
            "#740F在遗言执行之前的几天\x01",
            "真是不安……\x02\x03",

            "嗯，\x01",
            "因为这样不得已拜托了这个恐怖的姐姐。\x02",
        )
    )

    Jump("loc_16EE")

    label("loc_16EE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #57
        "#020F哎呀，你还真敢说呢。\x02",
    )

    Jump("loc_172C")

    label("loc_172C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("爱娜")

    AnonymousTalk(    #58
        (
            "#740F因为雪拉扎德……\x02\x03",

            "你很明显\x01",
            "讨厌我嘛。\x02",
        )
    )

    Jump("loc_177D")

    label("loc_177D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #59
        (
            "#030F难不成……\x02\x03",

            "相遇一开始\x01",
            "你们俩关系不好？\x02",
        )
    )

    Jump("loc_17CE")

    label("loc_17CE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #60
        (
            "#020F我也还年轻，\x01",
            "很多时候会觉得尴尬嘛。\x02\x03",

            "嗯，\x01",
            "不过光凭是资产家的女儿就看不顺眼也是确实的。\x02",
        )
    )

    Jump("loc_1854")

    label("loc_1854")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #61
        "#030F完、完全是偏见嘛。\x02",
    )

    Jump("loc_1890")

    label("loc_1890")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #62
        (
            "#020F什么啊，你真是啰嗦耶。\x02\x03",

            "……正说着呢，\x01",
            "你杯子怎么又空了。\x02",
        )
    )

    Jump("loc_18F3")

    label("loc_18F3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #63
        (
            "#030F哦、哦呀，是这样吗？\x02\x03",

            "哎，\x01",
            "不用管我继续说吧……\x02",
        )
    )

    Jump("loc_1952")

    label("loc_1952")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 30, -1, -1)
    SetChrName("爱娜")

    AnonymousTalk(    #64
        (
            "#740F好啦好啦，别这么说嘛。\x01",
            "…………（咕咚咕咚咕咚）\x02",
        )
    )

    Jump("loc_19A1")

    label("loc_19A1")

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xF9, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #65
        "#030F爱、爱娜小姐！？\x02",
    )

    Jump("loc_19E5")

    label("loc_19E5")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 30, -1, -1)
    SetChrName("爱娜")

    AnonymousTalk(    #66
        (
            "#740F嗯……\x01",
            "说到哪里了。\x02",
        )
    )

    Jump("loc_1A18")

    label("loc_1A18")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #67
        (
            "#030F呜……\x01",
            "接、接受了委托那里吧。\x02",
        )
    )

    Jump("loc_1A5F")

    label("loc_1A5F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 30, -1, -1)
    SetChrName("爱娜")

    AnonymousTalk(    #68
        (
            "#740F啊，对了对了。\x02\x03",

            "嗯，\x01",
            "就这样开始了逃亡生活。\x02",
        )
    )

    Jump("loc_1AB0")

    label("loc_1AB0")

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x240075, 0x0, 0x0, 0x190)
    Sleep(1000)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #69
        (
            "#020F为了逃避追杀\x01",
            "几乎跑遍了王都。\x02\x03",

            "不过，\x01",
            "这个大小姐出身的委托人竟然一句怨言也没有。\x02\x03",

            "大概是从这时开始吧，\x01",
            "我们开始相互理解了。\x02",
        )
    )

    Jump("loc_1B7A")

    label("loc_1B7A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("爱娜")

    AnonymousTalk(    #70
        (
            "#740F在一起相处了这么久\x01",
            "自然也知道对方性情了。\x02\x03",

            "而且更重要的是，\x01",
            "对我来说你是个很新鲜的人。\x02\x03",

            "是以前所生活的世界\x01",
            "从来不会有的类型。\x02\x03",

            "因此意气相投……\x01",
            "遗嘱顺利执行后的当晚，\x01",
            "两人还举杯庆祝呢。\x02",
        )
    )

    Jump("loc_1C53")

    label("loc_1C53")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #71
        (
            "#020F嗯，\x01",
            "真正的意气相投就是从那次饮酒会开始呢。\x02\x03",

            "养尊处优的\x01",
            "有钱人大小姐……\x02\x03",

            "我的这种偏见，\x01",
            "就是因为爱娜喝酒的样子\x01",
            "而完全粉碎掉了。\x02",
        )
    )

    Jump("loc_1D03")

    label("loc_1D03")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #72
        (
            "#030F呜……咿……\x01",
            "不、不过那次举杯庆祝……\x02\x03",

            "如果速６年前……\x01",
            "计算八是八太对头吗？\x02",
        )
    )

    Jump("loc_1D79")

    label("loc_1D79")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #73
        (
            "#020F啊ー，真是的……\x01",
            "醉鬼给我闭嘴啦。\x02\x03",

            "不过，吃惊的还在后头呢。\x02\x03",

            "因为爱娜这家伙，\x01",
            "居然把好不容易到手的遗产\x01",
            "全部捐赠出去了。\x02",
        )
    )

    Jump("loc_1E1A")

    label("loc_1E1A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #74
        "#030F真……真的么……\x02",
    )

    Jump("loc_1E54")

    label("loc_1E54")

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x240076, 0x0, 0x0, 0x190)
    Sleep(1000)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("爱娜")

    AnonymousTalk(    #75
        (
            "#740F嗯嗯，\x01",
            "分毫不差地捐给女王陛下的福利基金了。\x02",
        )
    )

    Jump("loc_1EBB")

    label("loc_1EBB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #76
        (
            "#020F到头来还一脸淡然地\x01",
            "对我说，\x01",
            "『要找工作才行了』……\x02\x03",

            "就算是我也放心不下啊。\x02",
        )
    )

    Jump("loc_1F3B")

    label("loc_1F3B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("爱娜")

    AnonymousTalk(    #77
        (
            "#740F所以就拜托她\x01",
            "介绍协会的工作给我了。\x02\x03",

            "呵呵，\x01",
            "现在回想起来还真是做过头了点。\x02",
        )
    )

    Jump("loc_1FAE")

    label("loc_1FAE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #78
        (
            "#020F哎呀，\x01",
            "既然你这么想就应该更感谢我。\x02",
        )
    )

    Jump("loc_1FFB")

    label("loc_1FFB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("爱娜")

    AnonymousTalk(    #79
        (
            "#740F所以说，\x01",
            "欠你的情不是都用工作还了吗。\x02\x03",

            "而且还有酒席上嘛。\x02\x03",

            "能够不拒绝你的邀请的\x01",
            "也只有我和卡西乌斯先生了吧。\x02",
        )
    )

    Jump("loc_2087")

    label("loc_2087")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #80
        (
            "#020F哼哼，算了㈱\x02\x03",

            "今后有奥利维尔\x01",
            "陪我了嘛。\x02\x03",

            "对吧～，奥利维尔～㈱\x02",
        )
    )

    Jump("loc_20EE")

    label("loc_20EE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #81
        "……………………………\x02",
    )

    Jump("loc_2129")

    label("loc_2129")

    CloseMessageWindow()
    OP_56(0x0)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x2)
    OP_AE(0x1F4)
    FadeToBright(1000, 0)
    Sleep(1000)
    OP_0D()

    ChrTalk(    #82
        0x10,
        "#020F#2P哎，咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x12,
        (
            "#740F#5P唉，可惜……\x02\x03",

            "已经醉倒了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10,
        (
            "#020F#2P哎～，怎么这样。\x02\x03",

            "夜晚才刚刚开始呢～。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 38570, 0, 68740, 180)
    OP_22(0xA4, 0x0, 0x64)
    OP_0D()

    def lambda_21F4():
        OP_6D(37250, 0, 68190, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_21F4)
    OP_8C(0x10, 270, 400)
    OP_8E(0x10, 0x915A, 0x0, 0x10D7E, 0xBB8, 0x0)
    OP_8E(0x10, 0x9218, 0x0, 0x10388, 0xBB8, 0x0)
    OP_8E(0x10, 0x974A, 0x0, 0x10310, 0xBB8, 0x0)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #85
        0x10,
        (
            "#020F#5P喂～，奥利维尔～！\x02\x03",

            "不准装睡哦～！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x11, 0x0, 0x0, 0x8)
    Sleep(1000)

    ChrTalk(    #86
        0x11,
        "#030F#6P哦、哦呜哦呜哦呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x12,
        (
            "#740F#2P呐，雪拉扎德……\x01",
            "不是我说啊。\x02\x03",

            "你最好还是\x01",
            "对酒友好一点吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x13, 0x0, 0x0, 0x7)
    WaitChrThread(0x13, 0x0)

    ChrTalk(    #88
        0x13,
        (
            "#5P雪、雪拉小姐！？\x01",
            "别使用暴力啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x11, 0x0)
    Sleep(200)
    OP_8C(0x10, 315, 400)
    Sleep(200)

    ChrTalk(    #89
        0x10,
        (
            "#020F#6P哎呀～，福克纳君㈱\x02\x03",

            "嗯呵呵，来得正好? \x01",
            "你代替他来陪我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x13,
        (
            "#5P不、不行！\x01",
            "我等下还有工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10,
        (
            "#020F#6P哎～，不嘛不嘛～。\x01",
            "陪我一起喝啦～。\x02\x03",

            "……不陪我喝我酒脱啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x13,
        "#5P咦！？\x02",
    )

    Jump("loc_240A")

    label("loc_240A")

    CloseMessageWindow()

    ChrTalk(    #93
        0x12,
        "#740F#2P唉，开始了……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 90, 400)

    ChrTalk(    #94
        0x13,
        (
            "#5P爱、爱娜小姐也\x01",
            "别光看着快阻止她啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x10,
        "#020F#6P呼～，好热哦～㈱\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x13, 135, 400)
    Sleep(500)

    ChrTalk(    #96
        0x13,
        "#5P啊、啊哇哇哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x11,
        "#030F#6P呜……呜……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #98
        (
            "\x07\x05就这样――\x01",
            "田园的夜晚更深了。\x02\x03",

            "这位旅人总算\x01",
            "从宴会中生还――\x02\x03",

            "但在此后，\x01",
            "不经意想起两人的面容时，\x01",
            "他仍会暗暗地颤抖。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_20(0x7D0)
    Sleep(2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E0, 0)), scpexpr(EXPR_END)), "loc_2582")
    NewScene("ED6_DT21/T0001   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_258B")

    label("loc_2582")

    NewScene("ED6_DT21/T7000   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_258B")

    Return()

    # Function_6_D75 end

    def Function_7_258C(): pass

    label("Function_7_258C")

    OP_8C(0xFE, 135, 400)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x807A, 0x0, 0x10FAE, 0x1388, 0x0)
    OP_8E(0xFE, 0x90CE, 0x0, 0x10716, 0x1388, 0x0)
    Return()

    # Function_7_258C end

    def Function_8_25DA(): pass

    label("Function_8_25DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2616")
    OP_9E(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(1500)
    Jump("Function_8_25DA")

    label("loc_2616")

    Return()

    # Function_8_25DA end

    def Function_9_2617(): pass

    label("Function_9_2617")

    OP_8C(0xFE, 315, 400)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x8296, 0x0, 0x1104E, 0x1388, 0x0)
    OP_8E(0xFE, 0x8426, 0x0, 0x12516, 0x1388, 0x0)
    OP_8E(0xFE, 0x86C4, 0x0, 0x125C0, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_9_2617 end

    def Function_10_2674(): pass

    label("Function_10_2674")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x821E, 0x0, 0x10F04, 0x7D0, 0x0)
    OP_8E(0xFE, 0x947A, 0x0, 0x10590, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_10_2674 end

    SaveToFile()

Try(main)
