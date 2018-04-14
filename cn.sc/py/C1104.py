from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1104   ._SN',
        MapName             = 'Bose',
        Location            = 'C1104.x',
        MapIndex            = 49,
        MapDefaultBGM       = "ed60031",
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
        '小丑肯帕雷拉',                         # 9
        '凯文神父',                             # 10
        '特务兵',                               # 11
        '特务兵',                               # 12
        '特务兵',                               # 13
        '特务兵',                               # 14
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
        'ED6_DT27/CH03600 ._CH',             # 00
        'ED6_DT27/CH03080 ._CH',             # 01
        'ED6_DT27/CH03095 ._CH',             # 02
        'ED6_DT07/CH00120 ._CH',             # 03
        'ED6_DT07/CH00121 ._CH',             # 04
        'ED6_DT07/CH00122 ._CH',             # 05
        'ED6_DT07/CH00124 ._CH',             # 06
        'ED6_DT07/CH00150 ._CH',             # 07
        'ED6_DT07/CH00151 ._CH',             # 08
        'ED6_DT07/CH00152 ._CH',             # 09
        'ED6_DT07/CH00154 ._CH',             # 0A
        'ED6_DT07/CH00420 ._CH',             # 0B
        'ED6_DT07/CH00421 ._CH',             # 0C
        'ED6_DT07/CH00424 ._CH',             # 0D
        'ED6_DT06/CH20042 ._CH',             # 0E
        'ED6_DT26/CH20299 ._CH',             # 0F
        'ED6_DT26/CH20300 ._CH',             # 10
        'ED6_DT07/CH00340 ._CH',             # 11
        'ED6_DT07/CH00440 ._CH',             # 12
        'ED6_DT07/CH00341 ._CH',             # 13
        'ED6_DT07/CH00441 ._CH',             # 14
        'ED6_DT07/CH00123 ._CH',             # 15
        'ED6_DT07/CH00153 ._CH',             # 16
        'ED6_DT07/CH00423 ._CH',             # 17
        'ED6_DT07/CH00055 ._CH',             # 18
        'ED6_DT07/CH00025 ._CH',             # 19
        'ED6_DT26/CH20298 ._CH',             # 1A
        'ED6_DT26/CH20305 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT27/CH03600P._CP',             # 00
        'ED6_DT27/CH03080P._CP',             # 01
        'ED6_DT27/CH03095P._CP',             # 02
        'ED6_DT07/CH00120P._CP',             # 03
        'ED6_DT07/CH00121P._CP',             # 04
        'ED6_DT07/CH00122P._CP',             # 05
        'ED6_DT07/CH00124P._CP',             # 06
        'ED6_DT07/CH00150P._CP',             # 07
        'ED6_DT07/CH00151P._CP',             # 08
        'ED6_DT07/CH00152P._CP',             # 09
        'ED6_DT07/CH00154P._CP',             # 0A
        'ED6_DT07/CH00420P._CP',             # 0B
        'ED6_DT07/CH00421P._CP',             # 0C
        'ED6_DT07/CH00424P._CP',             # 0D
        'ED6_DT06/CH20042P._CP',             # 0E
        'ED6_DT26/CH20299P._CP',             # 0F
        'ED6_DT26/CH20300P._CP',             # 10
        'ED6_DT07/CH00340P._CP',             # 11
        'ED6_DT07/CH00440P._CP',             # 12
        'ED6_DT07/CH00341P._CP',             # 13
        'ED6_DT07/CH00441P._CP',             # 14
        'ED6_DT07/CH00123P._CP',             # 15
        'ED6_DT07/CH00153P._CP',             # 16
        'ED6_DT07/CH00423P._CP',             # 17
        'ED6_DT07/CH00055P._CP',             # 18
        'ED6_DT07/CH00025P._CP',             # 19
        'ED6_DT26/CH20298P._CP',             # 1A
        'ED6_DT26/CH20305P._CP',             # 1B
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_24A",          # 00, 0
        "Function_1_25E",          # 01, 1
        "Function_2_264",          # 02, 2
        "Function_3_27A",          # 03, 3
        "Function_4_1B80",         # 04, 4
        "Function_5_43C9",         # 05, 5
        "Function_6_43DE",         # 06, 6
        "Function_7_4407",         # 07, 7
        "Function_8_4445",         # 08, 8
        "Function_9_448D",         # 09, 9
    )


    def Function_0_24A(): pass

    label("Function_0_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_25D")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_25D")

    Return()

    # Function_0_24A end

    def Function_1_25E(): pass

    label("Function_1_25E")

    OP_22(0x10E, 0x1, 0x5A)
    Return()

    # Function_1_25E end

    def Function_2_264(): pass

    label("Function_2_264")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_279")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_264")

    label("loc_279")

    Return()

    # Function_2_264 end

    def Function_3_27A(): pass

    label("Function_3_27A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_28B")
    ClearParty()
    AddParty(0x5, 0xF6, 0xFF)
    Jump("loc_290")

    label("loc_28B")

    ClearParty()
    AddParty(0x2, 0xF6, 0xFF)

    label("loc_290")

    AddParty(0x9, 0xF7, 0xFF)
    OP_6D(-330, 0, 3610, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2410, 0)
    OP_6C(45000, 0)
    OP_6E(547, 0)
    SetChrPos(0xF6, 4590, 0, -23390, 333)
    SetChrPos(0x10A, 3790, 50, -24060, 333)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_303():
        OP_6D(3640, 130, -22260, 8000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_303)

    def lambda_31B():
        OP_67(0, 10920, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_31B)

    def lambda_333():
        OP_6B(2240, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_333)

    def lambda_343():
        OP_6E(262, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_343)
    OP_6C(3000, 8000)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_42B")

    ChrTalk(    #0
        0x106,
        (
            "#552F#2P真奇怪啊……\x01",
            "明明是预想中的基地……\x02\x03",

            "但感觉不到有人的气息啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10A,
        (
            "#1317F是、是啊……\x02\x03",

            "刚才的士兵们\x01",
            "去了哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x106,
        (
            "#053F#2P哼，搞不好\x01",
            "被察觉了也说不定……\x02\x03",

            "#050F不管了，赶快调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504")

    label("loc_42B")


    ChrTalk(    #3
        0x103,
        (
            "#022F#2P真是奇怪呢……\x01",
            "似乎如预料一般是座大本营……\x02\x03",

            "但感觉不到有人存在的气息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10A,
        (
            "#1317F是、是啊……\x02\x03",

            "刚才的士兵们\x01",
            "去了哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x103,
        (
            "#026F#2P那么……\x01",
            "是被察觉了，还是……\x02\x03",

            "#027F算了。\x01",
            "总之还是慎重进行调查吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_504")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrPos(0xF6, 1180, 0, -470, 90)
    SetChrPos(0x10A, -6500, 0, 5600, 180)
    OP_6D(-2610, 0, -760, 0)
    OP_67(0, 9420, -10000, 0)
    OP_6B(1730, 0)
    OP_6C(45000, 0)
    OP_6E(449, 0)
    FadeToBright(1000, 0)

    def lambda_582():
        OP_6B(1400, 4000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_582)

    def lambda_592():
        OP_8F(0xFE, 0xFFFFF2E0, 0x0, 0xFFFFFBDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_592)
    Sleep(1500)
    OP_8C(0xF6, 270, 400)

    def lambda_5B9():
        OP_8E(0xFE, 0xFFFFF8D0, 0x0, 0xFFFFFB46, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF6, 0, lambda_5B9)
    WaitChrThread(0x10A, 0x0)
    OP_8C(0x10A, 90, 400)
    WaitChrThread(0xF6, 0x0)
    WaitChrThread(0x10A, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_FF2")

    ChrTalk(    #6
        0x10A,
        (
            "#1316F#6P不行啊。\x01",
            "感觉像是人去楼空的样子。\x02\x03",

            "#818F前辈那边怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x106,
        (
            "#555F这边也是一样。\x02\x03",

            "是出去了呢，还是\x01",
            "刚转移据点了呢……\x02\x03",

            "哪怕能发现一些\x01",
            "线索也好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10A,
        (
            "#810F#6P不过，好像没有\x01",
            "任何有关他们去向的线索……\x02\x03",

            "不过在那边的帐篷\x01",
            "发现了这个文件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x106,
        "#052F哦，我看看。\x02",
    )

    CloseMessageWindow()
    OP_92(0x10A, 0xF6, 0x320, 0x5DC, 0x0)
    Sleep(500)
    OP_8F(0x10A, 0xFFFFF2E0, 0x0, 0xFFFFFBDC, 0x5DC, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_AD(0x240112, 0xBE, 0x96, 0x1F4)
    Sleep(3000)
    OP_AE(0x1F4)
    FadeToBright(300, 0)
    Sleep(1500)

    ChrTalk(    #10
        0x106,
        (
            "#555F这是什么……\x01",
            "画着奇怪的图案啊。\x02\x03",

            "『奥尔杰尤』开发计划……\x02\x03",

            "好像是什么交通工具的设计图啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10A,
        (
            "#810F#6P『奥尔杰尤』……\x01",
            "略微有点华丽的名字呢。\x02\x03",

            "是飞船吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x106,
        (
            "#053F这个，我是门外汉\x01",
            "不大清楚……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #13
        0x106,
        "#052F……嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10A,
        "#814F#6P怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x106,
        (
            "#555F书页之间\x01",
            "夹着一张纸条。\x02\x03",

            "『请帖发送完毕了。』\x02\x03",

            "『桌椅也准备好了。』\x02\x03",

            "『这样一来茶会的准备就完成了。』\x02\x03",

            "『只剩下烤点心\x01",
            "和等待客人到齐了。』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10A,
        (
            "#1310F#6P哦～\x01",
            "内容听起来很温暖呢。\x02\x03",

            "#811F感觉像是图画书中的一段文字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x106,
        (
            "#053F唔……\x01",
            "反正是什么密码吧。\x02\x03",

            "#552F问题是这个讯息\x01",
            "到底意味着什么……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #18
        0x106,
        "#054F#4S散开！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #19
        0x10A,
        "#814F#6P咦……！\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -4210, 0, -6050, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -3380, 0, -4490, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -3300, 0, -2370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x106, 7)
    SetChrChipByIndex(0x10A, 11)

    def lambda_AC0():
        OP_96(0xFE, 0xFFFFFC22, 0x0, 0xFFFFFA06, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_AC0)

    def lambda_ADE():
        OP_96(0xFE, 0xFFFFEE30, 0x0, 0xFFFFFB28, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_ADE)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -2300, 0, -1090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_B40():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_B40)

    def lambda_B4E():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_B4E)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -2540, 0, 130, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -2000, 0, 1320, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(500)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, -11440, 0, -1180, 90)
    SetChrPos(0xB, 7610, 0, -2040, 270)
    SetChrPos(0xC, -3650, 0, -10100, 0)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0xB, 17)
    SetChrChipByIndex(0xC, 18)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)

    def lambda_C3F():
        OP_6D(-3470, 0, -1890, 3000)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_C3F)

    def lambda_C57():
        OP_67(0, 8380, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C57)

    def lambda_C6F():
        OP_6B(2100, 3000)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_C6F)

    def lambda_C7F():
        OP_6E(501, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_C7F)
    WaitChrThread(0x106, 0x0)
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x106, 0x2)
    OP_8C(0x106, 90, 400)
    OP_8C(0x10A, 270, 400)

    ChrTalk(    #20
        0x10A,
        "#1317F#6P骗人……什么时候。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x106,
        (
            "#051F#5P哼，好巧妙的\x01",
            "让人放松警惕的方法啊。\x02\x03",

            "跟那个红头盔少尉学的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        "#1K#2P…………………\x02",
    )


    ChrTalk(    #23
        0xB,
        "#1K#6P…………………\x02",
    )


    ChrTalk(    #24
        0xC,
        "#1K#1P…………………\x02",
    )

    Sleep(1000)
    OP_56(0x1)
    OP_59()
    SetChrChipByIndex(0xA, 19)
    SetChrChipByIndex(0xB, 19)
    SetChrChipByIndex(0xC, 20)

    def lambda_D7A():
        OP_8F(0xFE, 0xFFFFD71A, 0x0, 0xFFFFFBF0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D7A)

    def lambda_D95():
        OP_8E(0xFE, 0x15A4, 0x0, 0xFFFFF77C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D95)

    def lambda_DB0():
        OP_8E(0xFE, 0xFFFFF11E, 0x0, 0xFFFFDCC4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DB0)
    Sleep(1000)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_43(0x10A, 0x0, 0x0, 0x6)

    def lambda_DE3():
        OP_6D(-2240, 0, -1410, 3000)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_DE3)

    def lambda_DFB():
        OP_67(0, 7870, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_DFB)

    def lambda_E13():
        OP_6B(2000, 3000)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_E13)
    Sleep(250)

    def lambda_E28():
        OP_8F(0xFE, 0xFFFFDB84, 0x0, 0xFFFFFBD2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E28)

    def lambda_E43():
        OP_8E(0xFE, 0x1266, 0x0, 0xFFFFF768, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E43)

    def lambda_E5E():
        OP_8E(0xFE, 0xFFFFF178, 0x0, 0xFFFFE0A3, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E5E)
    Sleep(1000)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x10A, 0x0)
    Sleep(250)

    def lambda_E93():
        OP_8F(0xFE, 0xFFFFE142, 0x0, 0xFFFFFAA6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E93)

    def lambda_EAE():
        OP_8E(0xFE, 0xEB0, 0x0, 0xFFFFF75E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_EAE)

    def lambda_EC9():
        OP_8E(0xFE, 0xFFFFF204, 0x0, 0xFFFFE48A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_EC9)
    OP_43(0x10A, 0x0, 0x0, 0x6)
    Sleep(1000)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0xB, 17)
    SetChrChipByIndex(0xC, 18)
    WaitChrThread(0x106, 0x0)
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x106, 0x2)

    ChrTalk(    #25
        0x10A,
        "#812F#6P（阿加特前辈……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x106,
        (
            "#053F#5P（啊啊……\x01",
            "  果然非同寻常啊。）\x02\x03",

            "#050F（还是先联手打倒一个，\x01",
            "  然后再各自处理残局。）\x02\x03",

            "（能做到吧？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10A,
        "#816F#6P（放心吧！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        "#054F#5P那好──上吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10A,
        "#815F#6P好！\x02",
    )

    CloseMessageWindow()
    Jump("loc_19D3")

    label("loc_FF2")


    ChrTalk(    #30
        0x10A,
        (
            "#1316F#6P不行啊。\x01",
            "感觉像是人去楼空的样子。\x02\x03",

            "#818F前辈那边怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x103,
        (
            "#025F这边也一样。\x02\x03",

            "#522F出去了呢，还是\x01",
            "刚转移据点了呢……\x02\x03",

            "哪怕是有一些\x01",
            "他们去向的线索也好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10A,
        (
            "#810F#6P嗯，看来没有任何\x01",
            "关于去向的线索……\x02\x03",

            "不过在那边的帐篷\x01",
            "发现了这个文件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x103,
        "#023F哎呀，给我看看。\x02",
    )

    CloseMessageWindow()
    OP_92(0x10A, 0xF6, 0x320, 0x5DC, 0x0)
    Sleep(500)
    OP_8F(0x10A, 0xFFFFF2E0, 0x0, 0xFFFFFBDC, 0x5DC, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_AD(0x240112, 0xBE, 0x96, 0x1F4)
    Sleep(3000)
    OP_AE(0x1F4)
    FadeToBright(300, 0)
    Sleep(1500)

    ChrTalk(    #34
        0x103,
        (
            "#022F嗯……\x01",
            "画着奇怪的图案呢。\x02\x03",

            "『奥尔杰尤』开发计划……\x02\x03",

            "好像是什么交通工具的设计图啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10A,
        (
            "#810F#6P『奥尔杰尤』……\x01",
            "略微有点华丽的名字呢。\x02\x03",

            "是飞船吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        (
            "#025F嗯～我不是专家\x01",
            "不太明白……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #37
        0x103,
        "#023F……哎呀？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10A,
        "#814F#6P怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x103,
        (
            "#022F书页间夹着一张纸条呢。\x02\x03",

            "『请帖发送完毕了。』\x02\x03",

            "『桌椅也准备好了。』\x02\x03",

            "『这样一来茶会的准备就完成了。』\x02\x03",

            "『只剩下烤点心\x01",
            "  和等待客人到齐了。』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10A,
        (
            "#1310F#6P哦～\x01",
            "感觉好温暖的内容啊。\x02\x03",

            "#811F感觉像是图画书中的一段文字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x103,
        (
            "#026F嗯……\x01",
            "好像是什么暗语似的。\x02\x03",

            "#522F问题是这个讯息\x01",
            "意味着什么……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #42
        0x103,
        "#024F#4S散开！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10A,
        "#814F#6P咦……！\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -4210, 0, -6050, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -3380, 0, -4490, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -3300, 0, -2370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_14AC():
        OP_96(0xFE, 0xFFFFFC22, 0x0, 0xFFFFFA06, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14AC)

    def lambda_14CA():
        OP_96(0xFE, 0xFFFFEE30, 0x0, 0xFFFFFB28, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_14CA)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -2300, 0, -1090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrChipByIndex(0x103, 3)
    SetChrChipByIndex(0x10A, 11)

    def lambda_1536():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1536)

    def lambda_1544():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1544)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -2540, 0, 130, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -2000, 0, 1320, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(500)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, -11440, 0, -1180, 90)
    SetChrPos(0xB, 7610, 0, -2040, 270)
    SetChrPos(0xC, -3650, 0, -10100, 0)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0xB, 17)
    SetChrChipByIndex(0xC, 18)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)

    def lambda_1635():
        OP_6D(-3470, 0, -1890, 3000)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1635)

    def lambda_164D():
        OP_67(0, 8380, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_164D)

    def lambda_1665():
        OP_6B(2100, 3000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1665)

    def lambda_1675():
        OP_6E(501, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1675)
    WaitChrThread(0x103, 0x0)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x103, 0x2)
    OP_8C(0x103, 90, 400)
    OP_8C(0x10A, 270, 400)

    ChrTalk(    #44
        0x10A,
        "#1317F#6P骗人……什么时候。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x103,
        (
            "#027F#5P呵呵，遮蔽气息的\x01",
            "方式挺巧妙的呢。\x02\x03",

            "跟那个银发\x01",
            "少尉学来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        "#1K#2P…………………\x02",
    )


    ChrTalk(    #47
        0xB,
        "#1K#6P…………………\x02",
    )


    ChrTalk(    #48
        0xC,
        "#1K#1P…………………\x02",
    )

    OP_56(0x1)
    OP_59()
    SetChrChipByIndex(0xA, 19)
    SetChrChipByIndex(0xB, 19)
    SetChrChipByIndex(0xC, 20)

    def lambda_1768():
        OP_8F(0xFE, 0xFFFFD71A, 0x0, 0xFFFFFBF0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1768)

    def lambda_1783():
        OP_8E(0xFE, 0x15A4, 0x0, 0xFFFFF77C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1783)

    def lambda_179E():
        OP_8E(0xFE, 0xFFFFF11E, 0x0, 0xFFFFDCC4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_179E)
    Sleep(1000)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_43(0x10A, 0x0, 0x0, 0x6)

    def lambda_17D1():
        OP_6D(-2240, 0, -1410, 3000)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_17D1)

    def lambda_17E9():
        OP_67(0, 7870, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_17E9)

    def lambda_1801():
        OP_6B(2000, 3000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1801)
    Sleep(250)

    def lambda_1816():
        OP_8F(0xFE, 0xFFFFDB84, 0x0, 0xFFFFFBD2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1816)

    def lambda_1831():
        OP_8E(0xFE, 0x1266, 0x0, 0xFFFFF768, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1831)

    def lambda_184C():
        OP_8E(0xFE, 0xFFFFF178, 0x0, 0xFFFFE0A3, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_184C)
    Sleep(1000)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x10A, 0x0)
    Sleep(250)

    def lambda_1881():
        OP_8F(0xFE, 0xFFFFE142, 0x0, 0xFFFFFAA6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1881)

    def lambda_189C():
        OP_8E(0xFE, 0xEB0, 0x0, 0xFFFFF75E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_189C)

    def lambda_18B7():
        OP_8E(0xFE, 0xFFFFF204, 0x0, 0xFFFFE48A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_18B7)
    OP_43(0x10A, 0x0, 0x0, 0x6)
    Sleep(1000)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0xB, 17)
    SetChrChipByIndex(0xC, 18)
    WaitChrThread(0x103, 0x0)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x103, 0x2)

    ChrTalk(    #49
        0x10A,
        "#812F#6P（雪拉前辈……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#026F#5P（嗯嗯……\x01",
            "  看来不一般呢。）\x02\x03",

            "#020F（先联手打倒一个，\x01",
            "  然后各自解决残余。）\x02\x03",

            "（能做到吧？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10A,
        "#816F#6P（放心吧！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        "#024F#5P那好──上了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10A,
        "#815F#6P好！\x02",
    )

    CloseMessageWindow()

    label("loc_19D3")

    SetChrChipByIndex(0xA, 19)
    SetChrChipByIndex(0xB, 19)
    SetChrChipByIndex(0xC, 20)

    def lambda_19E8():
        OP_8E(0xFE, 0xFFFFEF48, 0x0, 0xFFFFFA42, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_19E8)

    def lambda_1A03():
        OP_8E(0xFE, 0x28, 0x0, 0xFFFFFA7E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1A03)

    def lambda_1A1E():
        OP_8E(0xFE, 0xFFFFF4D4, 0x0, 0xFFFFF13C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1A1E)

    def lambda_1A39():
        OP_6B(1300, 500)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_1A39)
    WaitChrThread(0x10A, 0x3)
    OP_D6(0x0)
    OP_3E(0x1F6, 4)
    OP_3E(0x1FC, 2)
    OP_3E(0x1FB, 4)
    OP_31(0x9, 0x0, 0x35)
    OP_31(0x9, 0xFE, 0x0)
    OP_31(0x9, 0x5, 0x23)
    OP_41(0x9, 0xCF, 0xFF)
    OP_41(0x9, 0x101, 0xFF)
    OP_41(0x9, 0x121, 0xFF)
    OP_41(0x9, 0x2C2, 0x0)
    OP_41(0x9, 0x2C9, 0x1)
    OP_41(0x9, 0x262, 0x2)
    OP_41(0x9, 0x265, 0x4)
    OP_41(0x9, 0x259, 0x5)
    OP_41(0x9, 0x0, 0x3)
    OP_41(0x9, 0x0, 0x4)
    OP_35(0x9, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AF9")
    OP_31(0x2, 0x0, 0x37)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x2, 0x5, 0x23)
    OP_41(0x2, 0x45, 0xFF)
    OP_41(0x2, 0x101, 0xFF)
    OP_41(0x2, 0x121, 0xFF)
    OP_41(0x2, 0x45, 0x0)
    OP_41(0x2, 0x26F, 0x0)
    OP_41(0x2, 0x265, 0x1)
    OP_41(0x2, 0x25C, 0x2)
    OP_41(0x2, 0x280, 0x4)
    OP_41(0x2, 0x25F, 0x5)
    OP_41(0x2, 0x0, 0x3)
    OP_41(0x2, 0x0, 0x4)
    OP_35(0x2, 0x0)
    Jump("loc_1B3E")

    label("loc_1AF9")

    OP_31(0x5, 0x0, 0x37)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x5, 0x5, 0x23)
    OP_41(0x5, 0xA0, 0xFF)
    OP_41(0x5, 0x101, 0xFF)
    OP_41(0x5, 0x121, 0xFF)
    OP_41(0x5, 0x260, 0x0)
    OP_41(0x5, 0x271, 0x1)
    OP_41(0x5, 0x268, 0x2)
    OP_41(0x5, 0x283, 0x5)
    OP_41(0x5, 0x262, 0x6)
    OP_41(0x5, 0x0, 0x3)
    OP_41(0x5, 0x0, 0x4)
    OP_35(0x5, 0x0)

    label("loc_1B3E")

    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x7A0, 0x0, 0x1, 0x0, 0xFF)
    OP_D6(0x1)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Call(0, 4)
    Return()

    # Function_3_27A end

    def Function_4_1B80(): pass

    label("Function_4_1B80")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    SetChrChipByIndex(0xA, 14)
    SetChrChipByIndex(0xB, 14)
    SetChrChipByIndex(0xC, 14)
    SetChrSubChip(0xA, 3)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 2)
    OP_44(0xA, 0x0)
    OP_44(0xB, 0x0)
    OP_44(0xC, 0x0)
    SetChrSubChip(0xF6, 0)
    SetChrChipByIndex(0xF6, 65535)
    ClearChrFlags(0xF6, 0x2)
    SetChrChipByIndex(0x10A, 65535)
    SetChrPos(0xF6, -3000, 0, -2660, 270)
    SetChrPos(0x10A, -2930, 0, -3910, 270)
    SetChrPos(0xA, -6360, 0, -3390, 90)
    SetChrPos(0xB, -7770, 0, -4330, 270)
    SetChrPos(0xC, -7530, 0, -2270, 90)
    SetChrPos(0x8, 6360, 0, -3740, 270)
    ClearChrFlags(0x8, 0x80)
    OP_6D(-4000, 0, -2190, 0)
    OP_67(0, 7230, -10000, 0)
    OP_6B(1700, 0)
    OP_6C(45000, 0)
    OP_6E(464, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3017")

    ChrTalk(    #54
        0x106,
        (
            "#057F#5P这些家伙是什么……\x02\x03",

            "解决是解决了……\x01",
            "但感觉还真是奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10A,
        (
            "#812F#2P嗯～是不是用了\x01",
            "什么危险的药物啊。\x02\x03",

            "听说之前卢安的不良集团\x01",
            "被药物操纵过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x106,
        (
            "#552F#5P不……\x01",
            "不过反应还是不同啊。\x02\x03",

            "简直像在砍\x01",
            "石头和树木一样……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_22(0x7B, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #57
        0x8,
        "少年的声音",
        "#3P啊哈哈，厉害厉害。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #58
        0x8,
        "少年的声音",
        (
            "#3P你们真是\x01",
            "相当优秀的游击士呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_21()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_59()
    OP_1D(0x6F)
    Sleep(1000)

    def lambda_1E38():
        OP_6D(-130, 0, -2660, 2500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1E38)

    def lambda_1E50():
        OP_67(0, 7230, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E50)

    def lambda_1E68():
        OP_6B(2009, 2500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1E68)

    def lambda_1E78():
        OP_8E(0xFE, 0xD20, 0x0, 0xFFFFF164, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1E78)

    def lambda_1E93():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1E93)
    TurnDirection(0x10A, 0x8, 400)
    WaitChrThread(0x8, 0x3)
    WaitChrThread(0x8, 0x0)

    ChrTalk(    #59
        0x106,
        "#052F#1P你是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #60
        0x8,
        "奇怪的少年",
        "#853F呼呵呵……\x02",
    )

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x200, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS118._CH")
    OP_C6(0x0, 0x0, 150000, 60000, 0)
    OP_C6(0x0, 0x0, 175000, 60000, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("奇怪的少年")

    AnonymousTalk(    #61
        (
            "#850F执行者Ｎｏ．０。\x01",
            "『小丑』肯帕雷拉。\x02\x03",

            "『噬身之蛇』的成员之一。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    Sleep(250)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #62
        0x10A,
        "#1317F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x106,
        "#057F#1P终于出现了吗……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x106, 7)
    SetChrSubChip(0x106, 0)
    Sleep(300)
    SetChrChipByIndex(0x10A, 11)
    SetChrSubChip(0x10A, 0)
    Sleep(500)

    ChrTalk(    #64
        0x106,
        (
            "#057F#1P你小子……\x01",
            "为什么会在这种地方？\x02\x03",

            "和特务兵的余党在一起\x01",
            "你打算做什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#853F呵呵呵～\x01",
            "这次我的任务仅仅是当一个旁观者。\x02\x03",

            "如果要问我关于具体计划的事情\x01",
            "那可就问错人了。\x02\x03",

            "因为我也一无所知呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x106,
        "#555F#1P旁观者……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#850F不过，要参加茶会的话\x01",
            "可能还是抓紧点比较好哦。\x02\x03",

            "虽然不知道在哪举行\x01",
            "不过至少不是这里就对了。\x02\x03",

            "#851F还是说，待在这里和我一起\x01",
            "喝一晚上咖啡？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x106,
        "#057F#1P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10A,
        (
            "#813F#6P唔，我说你……\x02\x03",

            "好像还很年轻\x01",
            "真的是『结社』的人？\x02\x03",

            "#812F为了你自己好，\x01",
            "还是别干了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "#853F哈哈哈，好善良的姐姐。\x02\x03",

            "把小丑当笑话\x01",
            "也就算了……\x02\x03",

            "#854F担心别人可是很不礼貌的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10A,
        "#814F#6P咦……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 8)
    OP_99(0x8, 0x9, 0xA, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    SetChrSubChip(0x8, 8)

    def lambda_22DA():
        OP_6D(-2000, 0, -2270, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22DA)
    Fade(1000)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xB, 0x2)
    ClearChrFlags(0xC, 0x2)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0xB, 17)
    SetChrChipByIndex(0xC, 18)
    OP_8C(0xA, 90, 0)
    OP_8C(0xB, 90, 0)
    OP_8C(0xC, 90, 0)
    OP_0D()
    WaitChrThread(0x8, 0x1)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_236D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_236D)
    OP_8C(0x10A, 270, 400)

    ChrTalk(    #72
        0x10A,
        "#1317F骗、骗人！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x106,
        (
            "#055F#5P经受那样的打击\x01",
            "居然还能动弹……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#854F#8P哈哈哈，所以说你们这些\x01",
            "游击士真是太天真了。\x02\x03",

            "要打就应该将其\x01",
            "彻底地破坏掉㈱\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x1, "monster\\msc0100.eff")
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 8)
    OP_99(0x8, 0x9, 0xA, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    SetChrSubChip(0x8, 8)
    PlayEffect(0x1, 0x1, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x2, 0xB, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x3, 0xC, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    LoadEffect(0x2, "map\\mp047_00.eff")
    PlayEffect(0x2, 0x4, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0x5, 0xB, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0x6, 0xC, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_43(0x8, 0x3, 0x0, 0x7)
    Fade(500)

    def lambda_25D7():
        OP_6D(-130, 0, -2660, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_25D7)
    OP_44(0xA, 0x0)
    OP_44(0xB, 0x0)
    OP_44(0xC, 0x0)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xA, 15)
    SetChrChipByIndex(0xB, 15)
    SetChrChipByIndex(0xC, 15)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 1)
    SetChrSubChip(0xC, 2)
    SetChrPos(0xA, -5990, 0, -2060, 0)
    SetChrPos(0xC, -7310, 0, -5200, 0)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 15)
    SetChrSubChip(0xD, 3)
    SetChrPos(0xD, -4610, 0, -4540, 0)
    SetChrChipByIndex(0x106, 22)
    SetChrChipByIndex(0x10A, 23)
    SetChrSubChip(0x106, 0)
    SetChrSubChip(0x10A, 0)

    def lambda_2697():
        OP_96(0xFE, 0xFFFFF948, 0x0, 0xFFFFF75E, 0x12C, 0x1B58)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2697)

    def lambda_26B5():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_26B5)

    def lambda_26CF():
        OP_96(0xFE, 0xFFFFF876, 0x0, 0xFFFFF06A, 0x12C, 0x1B58)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_26CF)

    def lambda_26ED():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_26ED)
    WaitChrThread(0x10A, 0x1)
    OP_8C(0x106, 270, 0)
    OP_8C(0x10A, 270, 0)
    SetChrChipByIndex(0x106, 10)
    SetChrChipByIndex(0x10A, 13)
    SetChrSubChip(0x106, 3)
    SetChrSubChip(0x10A, 3)

    ChrTalk(    #75 op#A op#5
        0x106,
        "#056F#10A#1P啊……！\x05\x02",
    )


    ChrTalk(    #76 op#A op#5
        0x10A,
        "#1312F#1P#10A#2P啊呜……！\x05\x02",
    )

    OP_0D()
    WaitChrThread(0x8, 0x0)
    Sleep(1000)
    OP_9E(0x106, 0x14, 0x0, 0x1F4, 0xFA0)
    Sleep(500)

    ChrTalk(    #77
        0x106,
        "#550F#5P唔……你小子！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10A,
        "#1317F好过分……竟然做这种事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#851F啊哈哈，吓了一跳吗？\x02\x03",

            "很精彩的演出～\x01",
            "让你们受惊了～\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x2, "map\\\\mp055_00.eff")
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 8)
    OP_99(0x8, 0x9, 0xA, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    SetChrSubChip(0x8, 8)
    PlayEffect(0x2, 0x1, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #80
        0x8,
        (
            "#854F哈哈哈～好了，\x01",
            "今晚的演出到此结束。\x02",
        )
    )

    CloseMessageWindow()
    Fade(100)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_99(0x8, 0x0, 0x3, 0x3E8)

    ChrTalk(    #81
        0x8,
        "#854F那么各位，保重。\x02",
    )

    CloseMessageWindow()

    def lambda_28EE():

        label("loc_28EE")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_28EE")

    QueueWorkItem2(0x106, 3, lambda_28EE)
    Sleep(500)
    OP_99(0x106, 0x3, 0x0, 0x5DC)
    OP_44(0x106, 0x3)
    SetChrChipByIndex(0x106, 7)
    SetChrSubChip(0x106, 0)
    Sleep(300)
    OP_8C(0x106, 90, 600)

    ChrTalk(    #82
        0x106,
        "#054F#3S别开玩笑了！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x8, 0)
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x106, 8)

    def lambda_295E():
        OP_6D(2500, 0, -2270, 1200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_295E)

    def lambda_2976():
        OP_8F(0xFE, 0x1F4, 0x0, 0xFFFFF380, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2976)

    def lambda_2991():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2991)
    WaitChrThread(0x106, 0x1)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x106, 9)
    SetChrSubChip(0x106, 0)
    SetChrFlags(0x106, 0x20)
    OP_82(0x1, 0x2)
    OP_43(0x8, 0x3, 0x0, 0x8)

    def lambda_29C6():
        OP_94(0x1, 0xFE, 0x0, 0x9C4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_29C6)

    def lambda_29DC():
        OP_99(0xFE, 0x0, 0x7, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_29DC)
    Sleep(300)
    OP_22(0x208, 0x0, 0x64)
    OP_20(0x7D0)
    WaitChrThread(0x106, 0x2)
    OP_44(0x106, 0x1)
    Sleep(2000)
    OP_99(0x106, 0x7, 0x0, 0x5DC)
    ClearChrFlags(0x106, 0x1000)
    ClearChrFlags(0x106, 0x20)
    SetChrFlags(0x8, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #83
        0x106,
        "#057F#5P…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_2A49():

        label("loc_2A49")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_2A49")

    QueueWorkItem2(0x10A, 3, lambda_2A49)
    Sleep(500)
    OP_99(0x10A, 0x3, 0x0, 0x3E8)
    OP_44(0x10A, 0x3)
    Fade(250)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x10A, 90, 400)
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #84
        0x10A,
        (
            "#813F#1P…………………………\x02\x03",

            "阿加特前辈……那个……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x106,
        "#053F#5P……啊啊………\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x106, 270, 400)
    Sleep(500)

    def lambda_2B12():

        label("loc_2B12")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_2B12")

    QueueWorkItem2(0x10A, 1, lambda_2B12)

    def lambda_2B23():
        OP_6D(-2500, 0, -3390, 2000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2B23)
    OP_8E(0x106, 0xFFFFF7EA, 0x0, 0xFFFFF56A, 0x5DC, 0x0)
    WaitChrThread(0x106, 0x1)
    Sleep(500)

    ChrTalk(    #86
        0x106,
        (
            "#552F明明没有那么\x01",
            "罪大恶极，\x01",
            "却沦落到这种死法……\x02\x03",

            "总之……\x01",
            "不能就这样放着不管。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x10A, 400)
    Sleep(500)

    ChrTalk(    #87
        0x106,
        (
            "#556F你就在那边\x01",
            "随便打发打发时间吧。\x02\x03",

            "对年轻女孩来说，这种场面太残酷了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x10A,
        "#1317F#4P但、但是……！\x02",
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_44(0x10A, 0x1)
    OP_8C(0x10A, 270, 400)

    ChrTalk(    #89
        0x10A,
        "#814F咦……？\x02",
    )

    CloseMessageWindow()

    def lambda_2C5D():

        label("loc_2C5D")

        TurnDirection(0xFE, 0x10A, 400)
        OP_48()
        Jump("loc_2C5D")

    QueueWorkItem2(0x106, 1, lambda_2C5D)

    def lambda_2C6E():
        OP_8E(0xFE, 0xFFFFF150, 0x0, 0xFFFFEEA8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2C6E)
    WaitChrThread(0x10A, 0x1)
    Fade(250)
    SetChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0x10A, 2)
    SetChrSubChip(0x10A, 7)
    OP_0D()
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0xD, 0x2)
    SetChrFlags(0xD, 0x80)
    SetChrChipByIndex(0x10A, 16)
    SetChrSubChip(0x10A, 7)
    OP_0D()

    ChrTalk(    #90
        0x106,
        "#055F喂、喂！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10A,
        (
            "#1317F那个，阿加特前辈……\x02\x03",

            "这个手臂……\x01",
            "好像是人造的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x106,
        "#052F什么……！？\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_44(0x106, 0x1)
    OP_8C(0x106, 270, 400)

    def lambda_2D3B():
        OP_6D(-4620, 0, -2840, 1500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2D3B)
    OP_8E(0x106, 0xFFFFEDAE, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    Fade(250)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 24)
    SetChrSubChip(0x106, 7)
    OP_0D()
    Sleep(500)
    OP_62(0x106, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #93
        0x106,
        (
            "#057F#5P齿轮和发条……\x01",
            "还有结晶回路的碎片……\x02\x03",

            "也就是说这个东西是……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -9770, 0, 5880, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    SetChrName("青年的声音")

    NpcTalk(    #94
        0x9,
        "青年的声音",
        (
            "#4P可以按规则自己行动的导力人偶……\x01",
            "也就是那人形兵器吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_6D(-4950, 0, -600, 0)
    OP_67(0, 7230, -10000, 0)
    OP_6B(1860, 0)
    OP_6C(21000, 0)
    OP_6E(464, 0)
    ClearChrFlags(0x10A, 0x20)
    ClearChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    ClearChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    OP_44(0x10A, 0xFF)
    OP_8C(0x106, 340, 0)
    OP_8C(0x10A, 340, 0)

    def lambda_2F0F():
        OP_8E(0xFE, 0xFFFFE5AC, 0x0, 0x528, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2F0F)

    def lambda_2F2A():
        OP_6D(-5810, 0, 150, 1500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2F2A)
    OP_0D()
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #95
        0x10A,
        "#814F#2P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x106,
        "#057F#2P……什么人？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)
    Sleep(500)

    ChrTalk(    #97
        0x9,
        (
            "#1065F#5P七耀教会巡回神父，\x01",
            "凯文·格拉汉姆。\x02\x03",

            "#1060F是阿加特·科洛斯纳先生和\x01",
            "亚妮拉丝·艾尔菲德小姐对吧？\x02\x03",

            "和你们商量一下……\x01",
            "相互交换一下情报怎样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43AC")

    label("loc_3017")


    ChrTalk(    #98
        0x103,
        (
            "#022F#5P呼，这些家伙是什么……\x02\x03",

            "虽然是打倒了……\x01",
            "反应还真是奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x10A,
        (
            "#812F#2P嗯～是不是用了\x01",
            "什么危险的药物啊。\x02\x03",

            "听说之前卢安的不良集团\x01",
            "被药物操纵过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x103,
        (
            "#020F#5P是艾丝蒂尔他们\x01",
            "解决了的事件吧。\x02\x03",

            "#522F不过，和那个\x01",
            "反应又不相同。\x02\x03",

            "简直像打在石头或者木头上一样……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x7B, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #101
        0x8,
        "少年的声音",
        "#3P啊哈哈，厉害厉害。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #102
        0x8,
        "少年的声音",
        (
            "#3P姐姐们……\x01",
            "是相当优秀的游击士呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_31CA():
        OP_6D(-130, 0, -2660, 2500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_31CA)

    def lambda_31E2():
        OP_67(0, 7230, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_31E2)

    def lambda_31FA():
        OP_6B(2009, 2500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_31FA)

    def lambda_320A():
        OP_8E(0xFE, 0xD20, 0x0, 0xFFFFF164, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_320A)

    def lambda_3225():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3225)
    TurnDirection(0x10A, 0x8, 400)
    WaitChrThread(0x8, 0x3)
    WaitChrThread(0x8, 0x0)

    ChrTalk(    #103
        0x103,
        "#023F#1P你……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #104
        0x8,
        "奇怪的少年",
        "#853F呼呵呵……\x02",
    )

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x200, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS118._CH")
    OP_C6(0x0, 0x0, 150000, 60000, 0)
    OP_C6(0x0, 0x0, 175000, 60000, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("奇怪的少年")

    AnonymousTalk(    #105
        (
            "#850F执行者Ｎｏ．０。\x01",
            "『小丑』肯帕雷拉。\x02\x03",

            "『噬身之蛇』的成员之一。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    Sleep(250)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_1D(0x6F)
    Sleep(1000)

    ChrTalk(    #106
        0x10A,
        "#1317F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x103,
        "#022F#1P终于出现了呢……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x103, 3)
    SetChrSubChip(0x103, 0)
    Sleep(300)
    SetChrChipByIndex(0x10A, 11)
    SetChrSubChip(0x10A, 0)
    Sleep(500)

    ChrTalk(    #108
        0x103,
        (
            "#022F#1P你……\x01",
            "怎么会在这种地方？\x02\x03",

            "和特务兵的余党在一起\x01",
            "打算做什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x8,
        (
            "#853F呵呵呵，\x01",
            "这次我的任务仅仅是当一个『旁观者』。\x02\x03",

            "如果是要问我关于具体计划的事\x01",
            "那可就问错人了。\x02\x03",

            "因为我也一无所知。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x103,
        "#023F#1P『旁观者』？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "#850F不过，要参加『茶会』的话，\x01",
            "或许动作要快一点比较好哦。\x02\x03",

            "虽然不知道在哪举行\x01",
            "不过至少不是这里就对了。\x02\x03",

            "#851F还是说，待在这里和我一起\x01",
            "喝一晚上咖啡？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        "#022F#1P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x10A,
        (
            "#813F#6P唔，我说你……\x02\x03",

            "看起来好像很年轻，\x01",
            "真的是『结社』的人？\x02\x03",

            "#812F我不会责备你的，\x01",
            "别再继续做这种事情了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        (
            "#853F哼哼哼，好善良的姐姐。\x02\x03",

            "不过，要是你把本小丑\x01",
            "当成笑料看也就算了……\x02\x03",

            "#854F如果是为我担心，那就是多此一举了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10A,
        "#814F#6P咦……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 8)
    OP_99(0x8, 0x9, 0xA, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    SetChrSubChip(0x8, 8)

    def lambda_369A():
        OP_6D(-2000, 0, -2270, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_369A)
    Fade(1000)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xB, 0x2)
    ClearChrFlags(0xC, 0x2)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0xB, 17)
    SetChrChipByIndex(0xC, 18)
    OP_8C(0xA, 90, 0)
    OP_8C(0xB, 90, 0)
    OP_8C(0xC, 90, 0)
    OP_0D()
    WaitChrThread(0x8, 0x1)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_372D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_372D)
    OP_8C(0x10A, 270, 400)

    ChrTalk(    #116
        0x10A,
        "#1317F骗、骗人！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#024F#5P怎么会……\x01",
            "应该完全无法战斗了才对啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        (
            "#854F#8P哈哈哈，所以说你们这些\x01",
            "游击士真是太天真了。\x02\x03",

            "要做就应该要\x01",
            "彻底地破坏掉㈱\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x1, "monster\\msc0100.eff")
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 8)
    OP_99(0x8, 0x9, 0xA, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    SetChrSubChip(0x8, 8)
    PlayEffect(0x1, 0x1, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x2, 0xB, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x3, 0xC, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    LoadEffect(0x2, "map\\mp047_00.eff")
    PlayEffect(0x2, 0x4, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0x5, 0xB, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0x6, 0xC, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_43(0x8, 0x3, 0x0, 0x7)
    Fade(500)

    def lambda_399B():
        OP_6D(-130, 0, -2660, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_399B)
    OP_44(0xA, 0x0)
    OP_44(0xB, 0x0)
    OP_44(0xC, 0x0)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xA, 15)
    SetChrChipByIndex(0xB, 15)
    SetChrChipByIndex(0xC, 15)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 1)
    SetChrSubChip(0xC, 2)
    SetChrPos(0xA, -5990, 0, -2060, 0)
    SetChrPos(0xC, -7310, 0, -5200, 0)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 15)
    SetChrSubChip(0xD, 3)
    SetChrPos(0xD, -4610, 0, -4540, 0)
    SetChrChipByIndex(0x103, 21)
    SetChrChipByIndex(0x10A, 23)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0x10A, 0)

    def lambda_3A5B():
        OP_96(0xFE, 0xFFFFF948, 0x0, 0xFFFFF75E, 0x12C, 0x1B58)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A5B)

    def lambda_3A79():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3A79)

    def lambda_3A93():
        OP_96(0xFE, 0xFFFFF876, 0x0, 0xFFFFF06A, 0x12C, 0x1B58)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3A93)

    def lambda_3AB1():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_3AB1)
    WaitChrThread(0x10A, 0x1)
    OP_8C(0x103, 270, 0)
    OP_8C(0x10A, 270, 0)
    SetChrChipByIndex(0x103, 6)
    SetChrChipByIndex(0x10A, 13)
    SetChrSubChip(0x103, 3)
    SetChrSubChip(0x10A, 3)

    ChrTalk(    #119 op#A op#5
        0x103,
        "#523F#10A#1P唔……！\x05\x02",
    )


    ChrTalk(    #120 op#A op#5
        0x10A,
        "#1312F#1P#10A#2P啊呜……！\x05\x02",
    )

    OP_0D()
    WaitChrThread(0x8, 0x0)
    Sleep(1000)
    OP_9E(0x103, 0x14, 0x0, 0x1F4, 0xFA0)
    Sleep(500)

    ChrTalk(    #121
        0x103,
        "#522F#5P怎、怎么这样……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x10A,
        "#1317F好过分……这种事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        (
            "#851F啊哈哈，吓了一跳吗？\x02\x03",

            "这个吓人箱子\x01",
            "做得很不赖吧？\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x2, "map\\\\mp055_00.eff")
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 8)
    OP_99(0x8, 0x9, 0xA, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    SetChrSubChip(0x8, 8)
    PlayEffect(0x2, 0x1, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #124
        0x8,
        (
            "#854F哈哈哈，好了，\x01",
            "今晚的演出就到此结束。\x02",
        )
    )

    CloseMessageWindow()
    Fade(100)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_99(0x8, 0x0, 0x3, 0x3E8)

    ChrTalk(    #125
        0x8,
        "#854F那么各位，保重。\x02",
    )

    CloseMessageWindow()

    def lambda_3CAE():

        label("loc_3CAE")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_3CAE")

    QueueWorkItem2(0x103, 3, lambda_3CAE)
    Sleep(500)
    OP_99(0x103, 0x3, 0x0, 0x5DC)
    OP_44(0x103, 0x3)
    SetChrChipByIndex(0x103, 3)
    SetChrSubChip(0x103, 0)
    Sleep(300)
    OP_8C(0x103, 90, 600)

    ChrTalk(    #126
        0x103,
        "#024F#3S等一下！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x8, 0)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x103, 4)

    def lambda_3D1A():
        OP_6D(2500, 0, -2270, 1200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D1A)

    def lambda_3D32():
        OP_8F(0xFE, 0x5DC, 0x0, 0xFFFFF380, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3D32)

    def lambda_3D4D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3D4D)
    WaitChrThread(0x103, 0x1)
    SetChrChipByIndex(0x103, 5)
    SetChrSubChip(0x103, 0)
    OP_82(0x1, 0x2)
    OP_43(0x8, 0x3, 0x0, 0x8)

    def lambda_3D78():
        OP_99(0xFE, 0x0, 0x7, 0xFA0)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_3D78)
    OP_22(0x1F6, 0x0, 0x64)
    Sleep(300)
    OP_22(0x208, 0x0, 0x64)
    OP_20(0x7D0)
    WaitChrThread(0x103, 0x3)
    ClearChrFlags(0x103, 0x1000)
    SetChrFlags(0x8, 0x80)
    Sleep(1500)

    ChrTalk(    #127
        0x103,
        "#022F#5P…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_3DD2():

        label("loc_3DD2")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_3DD2")

    QueueWorkItem2(0x10A, 3, lambda_3DD2)
    Sleep(500)
    OP_99(0x10A, 0x3, 0x0, 0x3E8)
    OP_44(0x10A, 0x3)
    Fade(250)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x10A, 90, 400)
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #128
        0x10A,
        (
            "#813F#1P…………………………\x02\x03",

            "雪拉前辈……那个……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x103,
        "#026F#5P……嗯嗯………\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x103, 270, 400)
    Sleep(500)

    def lambda_3E99():

        label("loc_3E99")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_3E99")

    QueueWorkItem2(0x10A, 1, lambda_3E99)

    def lambda_3EAA():
        OP_6D(-2500, 0, -3390, 2000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3EAA)
    OP_8E(0x103, 0xFFFFF7EA, 0x0, 0xFFFFF56A, 0x5DC, 0x0)
    WaitChrThread(0x103, 0x1)
    Sleep(500)

    ChrTalk(    #130
        0x103,
        (
            "#522F虽然毫无痛苦地\x01",
            "死去也算是幸运……\x02\x03",

            "不管怎样……\x01",
            "不能就这样放着不管。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x10A, 400)
    Sleep(500)

    ChrTalk(    #131
        0x103,
        (
            "#524F亚妮拉丝，不好意思，\x01",
            "能不能帮我把他们埋了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x10A,
        "#812F#4P是、是……！\x02",
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_44(0x10A, 0x1)
    OP_8C(0x10A, 270, 400)

    ChrTalk(    #133
        0x10A,
        "#814F咦……？\x02",
    )

    CloseMessageWindow()

    def lambda_3FC0():

        label("loc_3FC0")

        TurnDirection(0xFE, 0x10A, 400)
        OP_48()
        Jump("loc_3FC0")

    QueueWorkItem2(0x103, 1, lambda_3FC0)

    def lambda_3FD1():
        OP_8E(0xFE, 0xFFFFF150, 0x0, 0xFFFFEEA8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3FD1)
    WaitChrThread(0x10A, 0x1)
    Fade(250)
    SetChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0x10A, 2)
    SetChrSubChip(0x10A, 7)
    OP_0D()
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0xD, 0x2)
    SetChrFlags(0xD, 0x80)
    SetChrChipByIndex(0x10A, 16)
    SetChrSubChip(0x10A, 7)
    OP_0D()

    ChrTalk(    #134
        0x103,
        "#023F慢、慢着！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x10A,
        (
            "#1317F那个，雪拉前辈……\x02\x03",

            "这个手臂……\x01",
            "好像是人造的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x103,
        "#023F咦……！？\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_44(0x103, 0x1)
    OP_8C(0x103, 270, 400)

    def lambda_409C():
        OP_6D(-4620, 0, -2840, 1500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_409C)
    OP_8E(0x103, 0xFFFFEDAE, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    Fade(250)
    SetChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 25)
    SetChrSubChip(0x103, 7)
    OP_0D()
    Sleep(500)
    OP_62(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x103)
    Sleep(500)

    ChrTalk(    #137
        0x103,
        (
            "#022F#5P齿轮和发条……\x01",
            "还有结晶回路的碎片……\x02\x03",

            "说不定这是……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -9770, 0, 5880, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    SetChrName("青年的声音")

    NpcTalk(    #138
        0x9,
        "青年的声音",
        (
            "#4P可以按规则自己行动的导力人偶……\x01",
            "也就是所谓的人形兵器吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_6D(-4950, 0, -600, 0)
    OP_67(0, 7230, -10000, 0)
    OP_6B(1860, 0)
    OP_6C(21000, 0)
    OP_6E(464, 0)
    ClearChrFlags(0x10A, 0x20)
    ClearChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    OP_44(0x10A, 0xFF)
    OP_8C(0x103, 340, 0)
    OP_8C(0x10A, 340, 0)

    def lambda_426C():
        OP_8E(0xFE, 0xFFFFE5AC, 0x0, 0x528, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_426C)

    def lambda_4287():
        OP_6D(-5810, 0, 150, 1500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4287)
    OP_0D()
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #139
        0x10A,
        "#814F#2P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x103,
        "#023F#2P你确实是……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)
    Sleep(500)

    ChrTalk(    #141
        0x9,
        (
            "#1062F#5P哟，看来\x01",
            "你还记得我呢。\x02\x03",

            "#1065F重新自我介绍一下──我是\x01",
            "七耀教会的巡回神父凯文·格拉汉姆。\x02\x03",

            "#1060F两位是雪拉扎德·哈维小姐和\x01",
            "亚妮拉丝·艾尔菲德小姐对吧？\x02\x03",

            "和你们商量一下……\x01",
            "相互交换一下情报怎样？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43AC")

    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R1203   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_1B80 end

    def Function_5_43C9(): pass

    label("Function_5_43C9")

    OP_8F(0xFE, 0xFFFFF84E, 0x0, 0xFFFFFA6A, 0x3E8, 0x0)
    Return()

    # Function_5_43C9 end

    def Function_6_43DE(): pass

    label("Function_6_43DE")

    SetChrChipByIndex(0x10A, 12)
    SetChrSubChip(0x10A, 0)
    OP_8F(0xFE, 0xFFFFF434, 0x0, 0xFFFFFA56, 0x3E8, 0x0)
    SetChrChipByIndex(0x10A, 11)
    SetChrSubChip(0x10A, 0)
    Return()

    # Function_6_43DE end

    def Function_7_4407(): pass

    label("Function_7_4407")

    OP_7C(0xC8, 0xC8, 0xBB8, 0x3E8)
    Sleep(200)
    OP_7C(0xC8, 0xC8, 0xBB8, 0x3E8)
    Sleep(200)
    OP_7C(0xC8, 0xC8, 0xBB8, 0x3E8)
    Return()

    # Function_7_4407 end

    def Function_8_4445(): pass

    label("Function_8_4445")

    Sleep(300)
    OP_24(0x10A, 0x5A)
    Sleep(300)
    OP_24(0x10A, 0x50)
    Sleep(300)
    OP_24(0x10A, 0x46)
    Sleep(300)
    OP_24(0x10A, 0x3C)
    Sleep(300)
    OP_24(0x10A, 0x32)
    Sleep(300)
    OP_24(0x10A, 0x28)
    Sleep(300)
    OP_24(0x10A, 0x1E)
    Sleep(300)
    OP_23(0x10A)
    Return()

    # Function_8_4445 end

    def Function_9_448D(): pass

    label("Function_9_448D")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4507"),
        (1, "loc_450D"),
        (SWITCH_DEFAULT, "loc_4513"),
    )


    label("loc_4507")

    OP_A2(0x1200)
    Jump("loc_4513")

    label("loc_450D")

    OP_A2(0x1201)
    Jump("loc_4513")

    label("loc_4513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4521")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_4525")

    label("loc_4521")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_4525")

    Return()

    # Function_9_448D end

    SaveToFile()

Try(main)
