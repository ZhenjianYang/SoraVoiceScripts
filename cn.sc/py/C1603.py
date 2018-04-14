from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1603   ._SN',
        MapName             = 'Bose',
        Location            = 'C1603.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60125",
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
        '银发的青年',                           # 9
        '怀斯曼教授',                           # 10
        '古代龙',                               # 11
        '龙',                                   # 12
        '目标',                                 # 13
        '目标',                                 # 14
        '金耀石块·艾丝蒂尔',                   # 15
        '金耀石块·阿加特',                     # 16
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
        'ED6_DT07/CH02040 ._CH',             # 00
        'ED6_DT27/CH03550 ._CH',             # 01
        'ED6_DT26/CH20340 ._CH',             # 02
        'ED6_DT06/CH20091 ._CH',             # 03
        'ED6_DT26/CH20341 ._CH',             # 04
        'ED6_DT27/CH04000 ._CH',             # 05
        'ED6_DT27/CH04001 ._CH',             # 06
        'ED6_DT27/CH04002 ._CH',             # 07
        'ED6_DT07/CH00120 ._CH',             # 08
        'ED6_DT07/CH00121 ._CH',             # 09
        'ED6_DT07/CH00122 ._CH',             # 0A
        'ED6_DT07/CH00130 ._CH',             # 0B
        'ED6_DT07/CH00131 ._CH',             # 0C
        'ED6_DT07/CH00132 ._CH',             # 0D
        'ED6_DT07/CH00140 ._CH',             # 0E
        'ED6_DT07/CH00141 ._CH',             # 0F
        'ED6_DT07/CH00142 ._CH',             # 10
        'ED6_DT07/CH00170 ._CH',             # 11
        'ED6_DT07/CH00171 ._CH',             # 12
        'ED6_DT07/CH00172 ._CH',             # 13
        'ED6_DT07/CH00160 ._CH',             # 14
        'ED6_DT07/CH00161 ._CH',             # 15
        'ED6_DT07/CH00162 ._CH',             # 16
        'ED6_DT07/CH00150 ._CH',             # 17
        'ED6_DT07/CH00151 ._CH',             # 18
        'ED6_DT07/CH00152 ._CH',             # 19
        'ED6_DT07/CH00154 ._CH',             # 1A
        'ED6_DT07/CH00155 ._CH',             # 1B
        'ED6_DT06/CH20137 ._CH',             # 1C
        'ED6_DT06/CH20085 ._CH',             # 1D
        'ED6_DT26/CH20282 ._CH',             # 1E
        'ED6_DT27/CH04540 ._CH',             # 1F
        'ED6_DT26/CH20352 ._CH',             # 20
        'ED6_DT26/CH20353 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT07/CH02040P._CP',             # 00
        'ED6_DT27/CH03550P._CP',             # 01
        'ED6_DT26/CH20340P._CP',             # 02
        'ED6_DT06/CH20091P._CP',             # 03
        'ED6_DT26/CH20341P._CP',             # 04
        'ED6_DT27/CH04000P._CP',             # 05
        'ED6_DT27/CH04001P._CP',             # 06
        'ED6_DT27/CH04002P._CP',             # 07
        'ED6_DT07/CH00120P._CP',             # 08
        'ED6_DT07/CH00121P._CP',             # 09
        'ED6_DT07/CH00122P._CP',             # 0A
        'ED6_DT07/CH00130P._CP',             # 0B
        'ED6_DT07/CH00131P._CP',             # 0C
        'ED6_DT07/CH00132P._CP',             # 0D
        'ED6_DT07/CH00140P._CP',             # 0E
        'ED6_DT07/CH00141P._CP',             # 0F
        'ED6_DT07/CH00142P._CP',             # 10
        'ED6_DT07/CH00170P._CP',             # 11
        'ED6_DT07/CH00171P._CP',             # 12
        'ED6_DT07/CH00172P._CP',             # 13
        'ED6_DT07/CH00160P._CP',             # 14
        'ED6_DT07/CH00161P._CP',             # 15
        'ED6_DT07/CH00162P._CP',             # 16
        'ED6_DT07/CH00150P._CP',             # 17
        'ED6_DT07/CH00151P._CP',             # 18
        'ED6_DT07/CH00152P._CP',             # 19
        'ED6_DT07/CH00154P._CP',             # 1A
        'ED6_DT07/CH00155P._CP',             # 1B
        'ED6_DT06/CH20137P._CP',             # 1C
        'ED6_DT06/CH20085P._CP',             # 1D
        'ED6_DT26/CH20282P._CP',             # 1E
        'ED6_DT27/CH04540P._CP',             # 1F
        'ED6_DT26/CH20352P._CP',             # 20
        'ED6_DT26/CH20353P._CP',             # 21
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 1048609,
        ChipIndex           = 0x21,
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
        Unknown3            = 1048609,
        ChipIndex           = 0x21,
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
        Unknown3            = 1048609,
        ChipIndex           = 0x21,
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
        Unknown3            = 1048609,
        ChipIndex           = 0x21,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_2BA",          # 00, 0
        "Function_1_303",          # 01, 1
        "Function_2_344",          # 02, 2
        "Function_3_B94",          # 03, 3
        "Function_4_BDC",          # 04, 4
        "Function_5_BE5",          # 05, 5
        "Function_6_1EA0",         # 06, 6
        "Function_7_1EDD",         # 07, 7
        "Function_8_1F1A",         # 08, 8
        "Function_9_5496",         # 09, 9
        "Function_10_54B2",        # 0A, 10
        "Function_11_54D1",        # 0B, 11
        "Function_12_5525",        # 0C, 12
        "Function_13_5579",        # 0D, 13
        "Function_14_55B1",        # 0E, 14
        "Function_15_56CD",        # 0F, 15
        "Function_16_56F6",        # 10, 16
        "Function_17_5729",        # 11, 17
        "Function_18_5752",        # 12, 18
        "Function_19_57DE",        # 13, 19
        "Function_20_590B",        # 14, 20
        "Function_21_5AB9",        # 15, 21
        "Function_22_5BE7",        # 16, 22
        "Function_23_5DA0",        # 17, 23
        "Function_24_5FA1",        # 18, 24
        "Function_25_5FFF",        # 19, 25
        "Function_26_60A1",        # 1A, 26
        "Function_27_612B",        # 1B, 27
    )


    def Function_0_2BA(): pass

    label("Function_0_2BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2DE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x1, 0x4)
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)
    Jump("loc_302")

    label("loc_2DE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2EA"),
        (SWITCH_DEFAULT, "loc_302"),
    )


    label("loc_2EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FF")
    OP_71(0x1, 0x4)
    Event(0, 4)

    label("loc_2FF")

    Jump("loc_302")

    label("loc_302")

    Return()

    # Function_0_2BA end

    def Function_1_303(): pass

    label("Function_1_303")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x44F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_325")
    OP_4F(0x29, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x36), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_END)), "loc_33E")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_72(0x3, 0x2)
    Jump("loc_343")

    label("loc_33E")

    OP_71(0x3, 0x2)

    label("loc_343")

    Return()

    # Function_1_303 end

    def Function_2_344(): pass

    label("Function_2_344")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-270, 0, -16520, 0)
    OP_67(0, 5490, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(200000, 0)
    OP_6E(360, 0)
    SetChrPos(0x9, 3570, 0, -26960, 0)
    SetChrPos(0x8, 2570, 0, -27960, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 970)
    SetMapFlags(0x10)
    OP_11(0xC8, 0xC8, 0xC8, 0x61A8, 0x9470, 0x0)
    FadeToBright(2000, 0)

    def lambda_3F8():
        OP_8E(0xFE, 0x24E, 0x0, 0xFFFFC414, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3F8)
    Sleep(300)
    OP_8E(0x8, 0xFFFFFE0C, 0x0, 0xFFFFC054, 0x7D0, 0x0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x8,
        "#126F#5P……这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "#1154F#5P哈哈哈……\x01",
            "果然在这里啊。\x02\x03",

            "#1150F看，莱维。\x01",
            "这是多么优美的存在啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "#124F#5P…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)
    Sleep(500)

    ChrTalk(    #3
        0x8,
        (
            "#120F#2P真的要用这种东西\x01",
            "进行实验吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #4
        0x9,
        (
            "#1150F#6P你会有所顾虑也是理所当然的。\x02\x03",

            "但是，要完成『β』\x01",
            "无论如何都必须得到这些数据。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(380, 100, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #5
        "\x07\x05…………你们是……………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x8, 0x0, 0x0, 0x3)

    def lambda_5FD():
        OP_6D(1720, 4250, -8690, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FD)

    def lambda_615():
        OP_67(0, 1070, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_615)

    def lambda_62D():
        OP_6B(3230, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_62D)

    def lambda_63D():
        OP_6C(351000, 7000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_63D)

    def lambda_64D():
        OP_6E(553, 7000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_64D)
    OP_B0(0x0, 0x5)
    OP_6F(0x0, 980)
    OP_70(0x0, 0x398)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 920)
    OP_70(0x0, 0x366)

    ChrTalk(    #6
        0x9,
        (
            "#1153F#5P哦哦……\x01",
            "好像醒了呢。\x02\x03",

            "#1154F时隔２０年的觉醒吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #7
        "\x07\x05……………………………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #8
        0x9,
        (
            "#1150F#5P初次见面。\x02\x03",

            "本人名叫盖鲁格·怀斯曼。\x02\x03",

            "是负责掌管『噬身之蛇』的\x01",
            "『蛇之使徒』的成员之一。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #9
        (
            "\x07\x05……………………………………\x02\x03",

            "……滚……\x02\x03",

            "虽然你身体里蕴藏着的力量……\x01",
            "依然还有一丝让人怀念的地方……\x02\x03",

            "不过，我不喜欢你的那种眼神……\x02\x03",

            "只有邪恶，才能使你的眼中透露喜悦\x01",
            "……我可以感觉到你那歪曲的灵魂……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #10
        0x9,
        (
            "#1151F#5P呵呵，承蒙夸奖。\x02\x03",

            "但是很遗憾\x01",
            "你没有拒绝的权利。\x02\x03",

            "因为是有关女神至宝的事情。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #11
        "\x07\x05………什么………？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #12
        0x9,
        "#1154F#5P莱维，给它看。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        "#121F#5P………………………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-1360, 0, -17130, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(206000, 0)
    OP_6E(360, 0)
    OP_8C(0x8, 0, 0)
    OP_8C(0x9, 0, 0)
    LoadEffect(0x0, "battle\\\\mgaria0.eff")
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)
    OP_99(0x8, 0x0, 0x4, 0x3E8)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(380, 100, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #14
        "\x07\x05………那是………！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #15
        0x9,
        (
            "#1151F#5P是否唤醒了１２００年前的记忆了呢？\x02\x03",

            "虽然只是复制品，\x01",
            "但做得很不错吧？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(380, 100, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #16
        (
            "\x07\x05…………你们…………\x02\x03",

            "……莫非要将『辉之环』！！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #17
        0x9,
        "#1154F#5P呵呵，就是这个意思……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)

    def lambda_AB1():
        OP_99(0x9, 0x0, 0x3, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_AB1)
    PlayEffect(0x0, 0x0, 0xFF, 590, 0, -15340, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_AFB():
        OP_99(0x9, 0x3, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_AFB)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(1000)
    OP_82(0x0, 0x2)
    Sleep(1000)

    def lambda_B1D():
        OP_99(0x9, 0x7, 0xB, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_B1D)
    Sleep(1000)

    ChrTalk(    #18
        0x9,
        (
            "#1155F#5P那么──\x01",
            "开始最后的实验吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_AD(0x2400A8, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x1A00)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0100   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_2_344 end

    def Function_3_B94(): pass

    label("Function_3_B94")

    Sleep(500)

    def lambda_B9F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B9F)
    Sleep(100)

    def lambda_BB2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BB2)
    Sleep(5000)

    def lambda_BC5():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BC5)

    def lambda_BD3():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BD3)
    Return()

    # Function_3_B94 end

    def Function_4_BDC(): pass

    label("Function_4_BDC")

    Call(0, 5)
    Call(0, 8)
    Return()

    # Function_4_BDC end

    def Function_5_BE5(): pass

    label("Function_5_BE5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFC")
    Call(0, 26)
    Call(0, 27)

    label("loc_BFC")

    OP_6D(3160, 0, -25690, 0)
    OP_67(0, 9710, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2800, 0, -25400, 0)
    SetChrPos(0x106, 4180, 0, -25530, 0)
    SetChrPos(0x107, 4310, 0, -26920, 0)
    SetChrPos(0xF9, 2780, 0, -26920, 0)
    OP_A1(0xA, 0x0)
    SetChrPos(0xA, 10000, 300, 14130, 192)
    OP_6F(0x0, 970)
    OP_70(0x0, 0x410)
    OP_8C(0xB, 180, 0)
    OP_CF(0xB, 0x0, "Frame127_FireEmitter")
    SetChrFlags(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1964), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x249F0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x7D0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D88")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DC6")

    label("loc_D88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAF")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DC6")

    label("loc_DAF")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_DC6")

    Sleep(1000)

    ChrTalk(    #19
        0x101,
        "#1020F#6P（啊啊……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x106,
        "#057F#6P（在吗……！）\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x51)
    Sleep(400)

    def lambda_E14():
        OP_6D(8480, 0, 16800, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E14)

    def lambda_E2C():
        OP_67(0, 4000, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E2C)

    def lambda_E44():
        OP_6B(4090, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E44)

    def lambda_E54():
        OP_6C(347000, 6000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_E54)
    OP_6E(421, 6000)
    Sleep(1500)
    Fade(500)
    OP_6D(3160, 0, -25690, 0)
    OP_67(0, 9710, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #21
        0x107,
        "#065F#6P（在、在睡觉吗？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F2E")

    ChrTalk(    #22
        0x103,
        (
            "#022F#6P（嗯嗯……好像是的。）\x02\x03",

            "（那个叫莱维的人\x01",
            "  好像也不在……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102F")

    label("loc_F2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F84")

    ChrTalk(    #23
        0x105,
        (
            "#043F#6P（……似乎没错。）\x02\x03",

            "（那个叫莱维的人\x01",
            "  好像也不在……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102F")

    label("loc_F84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FDB")

    ChrTalk(    #24
        0x104,
        (
            "#035F#6P（呼……似乎没错。）\x02\x03",

            "#030F（好像也没看到\x01",
            "莱维的身影。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102F")

    label("loc_FDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_102F")

    ChrTalk(    #25
        0x108,
        (
            "#070F（啊啊……似乎没错。）\x02\x03",

            "（那个叫莱维的男人\x01",
            "  好像也不在。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102F")


    ChrTalk(    #26
        0x101,
        "#1006F#6P（这可能是个机会……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    def lambda_1061():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1061)
    Sleep(300)

    ChrTalk(    #27
        0x101,
        "#1002F#5P（阿加特，怎么办？）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)
    Sleep(500)

    ChrTalk(    #28
        0x106,
        (
            "#053F#4P（首先我一个人接近。）\x02\x03",

            "#051F（要是顺利的话，\x01",
            "  就这样把『福音』\x01",
            "  一口气破坏了吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1002F#5P（是吗……明白了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x107,
        "#063F#6P（阿加特……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)

    ChrTalk(    #31
        0x106,
        (
            "#051F#2P（没问题，别担心。）\x02\x03",

            "(失败的时候拜托你们掩护了。)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x107,
        "#560F#6P（是……！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1006F#5P（小心哦……！）\x02",
    )

    CloseMessageWindow()

    def lambda_11C5():
        OP_69(0xFE, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_11C5)

    def lambda_11D3():
        OP_67(0, 5580, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11D3)

    def lambda_11EB():
        OP_6C(336000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11EB)

    def lambda_11FB():

        label("loc_11FB")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_11FB")

    QueueWorkItem2(0x101, 2, lambda_11FB)

    def lambda_120C():

        label("loc_120C")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_120C")

    QueueWorkItem2(0x107, 2, lambda_120C)

    def lambda_121D():

        label("loc_121D")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_121D")

    QueueWorkItem2(0xF9, 2, lambda_121D)
    Sleep(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 23)
    SetChrSubChip(0x106, 0)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    SetChrFlags(0x106, 0x4)
    OP_C4(0x0, 0x40)
    OP_6A(0x106)
    Sleep(300)
    OP_8C(0x106, 0, 400)
    Sleep(300)
    OP_8E(0x106, 0xF5A, 0x0, 0xFFFFD5D0, 0x1F40, 0x0)
    OP_8C(0x106, 180, 400)
    Sleep(1000)
    OP_6A(0xFF)
    OP_C4(0x1, 0x40)
    OP_44(0x101, 0x2)
    OP_44(0x107, 0x2)
    OP_44(0xF9, 0x2)

    def lambda_12A0():
        OP_6D(6440, 0, 6810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12A0)

    def lambda_12B8():
        OP_6B(2960, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12B8)
    OP_6E(206, 3000)
    Sleep(1000)

    ChrTalk(    #34
        0x106,
        "#057F#2P（是那个吗……）\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sleep(200)
    Fade(500)
    OP_6D(3410, 0, -10000, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(336000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x106, 0x40)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 32)
    OP_0D()
    Sleep(300)
    OP_22(0x9D, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp009_00.eff")

    def lambda_137E():

        label("loc_137E")

        OP_99(0xFE, 0x1, 0x7, 0x5DC)
        OP_48()
        Jump("loc_137E")

    QueueWorkItem2(0x106, 2, lambda_137E)
    Sleep(1000)

    ChrTalk(    #35
        0x106,
        "#053F（……要上啦！）\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_44(0x106, 0x2)

    def lambda_13BA():
        OP_6D(5910, 0, -11000, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13BA)
    ClearChrFlags(0x106, 0x2)
    SetChrFlags(0x106, 0x800)
    SetChrChipByIndex(0x106, 24)
    SetChrSubChip(0x106, 0)

    def lambda_13E6():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_13E6)

    def lambda_13F4():
        OP_96(0xFE, 0x1716, 0x0, 0xFFFFD508, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_13F4)
    WaitChrThread(0x106, 0x2)
    WaitChrThread(0x106, 0x3)

    def lambda_141C():
        OP_6D(7100, 0, 4690, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_141C)
    SetChrFlags(0x106, 0x1000)

    ChrTalk(    #36 op#5
        0x106,
        "#054F#6P#3S啊啊啊啊！！\x05\x02",
    )

    OP_8E(0x106, 0x1D56, 0x0, 0x12C, 0x2EE0, 0x0)
    OP_44(0x106, 0x1)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_147C():
        OP_6D(7100, 2000, 4690, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_147C)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1499():
        OP_96(0x106, 0x1CE8, 0x578, 0xD48, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1499)
    Sleep(100)
    SetChrChipByIndex(0x106, 25)

    def lambda_14C1():
        OP_99(0xFE, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_14C1)

    def lambda_14D1():
        OP_6D(6810, 0, 5420, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14D1)

    def lambda_14E9():
        OP_67(0, 7660, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14E9)

    def lambda_1501():
        OP_6B(2860, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1501)

    def lambda_1511():
        OP_6C(336000, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1511)
    Sleep(300)

    def lambda_1526():
        OP_99(0xFE, 0x4, 0x5, 0x9C4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1526)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x320)
    WaitChrThread(0x106, 0x0)
    WaitChrThread(0x106, 0x2)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 1045)
    OP_20(0x0)
    OP_22(0x9B, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 7850, 2000, 4370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrChipByIndex(0x106, 24)
    SetChrSubChip(0x106, 0)

    def lambda_15AB():
        OP_96(0x106, 0x1BE4, 0x0, 0x672, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_15AB)
    WaitChrThread(0x106, 0x0)
    OP_8C(0x106, 45, 0)
    SetChrChipByIndex(0x106, 25)

    def lambda_15DA():
        OP_99(0x106, 0x5, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_15DA)

    def lambda_15EA():
        OP_96(0x106, 0x14A0, 0x0, 0xFFFFF894, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_15EA)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetMapFlags(0x10)
    OP_6D(6460, 0, 13890, 0)
    OP_67(0, 3020, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(351000, 0)
    OP_6E(498, 0)
    WaitChrThread(0x106, 0x0)
    SetChrChipByIndex(0x106, 23)
    ClearChrFlags(0x106, 0x800)
    OP_0D()
    Sleep(500)
    OP_22(0x12C, 0x0, 0x5A)
    Sleep(2000)

    ChrTalk(    #37
        0x106,
        "#054F成功了吗……！？\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    LoadEffect(0x2, "map\\\\mp007_00.eff")
    OP_22(0x90, 0x0, 0x64)
    PlayEffect(0x2, 0x1, 0xB, 900, 900, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_16EA():
        OP_6B(3380, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16EA)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 28)
    SetChrSubChip(0x106, 0)
    Sleep(500)
    OP_72(0x0, 0x20)
    OP_B0(0x0, 0x19)
    OP_6F(0x0, 970)
    OP_70(0x0, 0x410)
    OP_8F(0xA, 0x26AC, 0x12C, 0x36CE, 0x2710, 0x0)
    OP_8F(0xA, 0x2710, 0x12C, 0x3732, 0x2710, 0x0)
    OP_8F(0xA, 0x26AC, 0x12C, 0x36CE, 0x2710, 0x0)
    OP_8F(0xA, 0x2710, 0x12C, 0x3732, 0x2710, 0x0)
    OP_8F(0xA, 0x26AC, 0x12C, 0x36CE, 0x2710, 0x0)
    OP_8F(0xA, 0x2710, 0x12C, 0x3732, 0x2710, 0x0)
    OP_73(0x0)
    OP_82(0x1, 0x2)
    OP_1D(0x36)
    Sleep(500)

    def lambda_17C6():
        OP_6D(7030, 2640, 15970, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17C6)

    def lambda_17DE():
        OP_67(0, 1000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17DE)

    def lambda_17F6():
        OP_6C(15000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17F6)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 1045)
    OP_70(0x0, 0x42E)
    OP_22(0x122, 0x0, 0x64)
    OP_73(0x0)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 125)
    OP_70(0x0, 0xB4)
    OP_8C(0x106, 0, 0)
    Sleep(75)
    OP_8C(0x106, 315, 0)
    Sleep(425)
    OP_23(0x193)
    Sleep(700)
    Sleep(100)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 5)
    OP_70(0x0, 0x37)
    Fade(500)
    OP_6D(-840, 0, 5360, 0)
    OP_67(0, 4730, -10000, 0)
    OP_6B(4190, 0)
    OP_6C(315000, 0)
    OP_6E(352, 0)
    SetChrPos(0x106, 3860, 0, -4770, 0)
    OP_8C(0x106, 0, 0)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 28)
    SetChrSubChip(0x106, 3)
    OP_0D()

    ChrTalk(    #38
        0x106,
        "#057F#5P可恶……力量太小了吗！\x02",
    )

    CloseMessageWindow()

    def lambda_1922():
        OP_6D(-500, 1060, 12470, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1922)

    def lambda_193A():
        OP_67(0, 3440, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_193A)

    def lambda_1952():
        OP_6B(3500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1952)

    def lambda_1962():
        OP_6C(339000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1962)
    Sleep(500)
    Sleep(200)
    LoadEffect(0x3, "monster\\ms30703.eff")
    OP_72(0x0, 0x20)
    OP_6F(0x0, 80)
    OP_70(0x0, 0x78)
    Sleep(1000)

    def lambda_19AA():
        OP_6D(3510, 380, 5270, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19AA)

    def lambda_19C2():
        OP_67(0, 2900, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19C2)

    def lambda_19DA():
        OP_6B(3190, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19DA)

    def lambda_19EA():
        OP_6C(339000, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19EA)

    def lambda_19FA():
        OP_6E(462, 300)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_19FA)
    PlayEffect(0x3, 0x0, 0xB, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x106, 0, 0, 0, 0)
    OP_22(0x121, 0x0, 0x64)
    Sleep(100)
    OP_43(0x106, 0x0, 0x0, 0x7)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 5)
    OP_70(0x0, 0x37)
    Sleep(1000)
    SetChrPos(0x107, 9710, 0, -14620, 0)

    ChrTalk(    #39
        0x107,
        "#2P阿加特！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    LoadEffect(0x3, "map\\\\mp019_00.eff")
    SetChrPos(0xC, 6500, 5510, 9600, 0)
    OP_22(0x1FA, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0xFF, 14500, 5730, -23660, 0, 0, 0, 1000, 1000, 1000, 0xB, 0, 1500, 0, 0)
    Fade(500)
    OP_6D(5000, 2150, 160, 0)
    OP_67(0, 1730, -10000, 0)
    OP_6B(2610, 0)
    OP_6C(339000, 0)
    OP_6E(530, 0)
    SetChrPos(0x106, 8020, 0, -5130, 0)
    SetChrSubChip(0x106, 2)
    Sleep(1500)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x4B)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 5)
    OP_70(0x0, 0x37)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x107, 0x40)
    SetChrFlags(0xF9, 0x40)
    SetChrPos(0x101, 12470, 0, -15800, 0)
    SetChrPos(0x107, 14010, 0, -16620, 0)
    SetChrPos(0xF9, 13000, 0, -17160, 0)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 21)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 6)
    SetChrSubChip(0xF9, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1BE5"),
        (3, "loc_1BED"),
        (4, "loc_1BF5"),
        (7, "loc_1BFD"),
        (SWITCH_DEFAULT, "loc_1C05"),
    )


    label("loc_1BE5")

    SetChrChipByIndex(0xF9, 9)
    Jump("loc_1C05")

    label("loc_1BED")

    SetChrChipByIndex(0xF9, 12)
    Jump("loc_1C05")

    label("loc_1BF5")

    SetChrChipByIndex(0xF9, 15)
    Jump("loc_1C05")

    label("loc_1BFD")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_1C05")

    label("loc_1C05")

    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x107, 0x1000)
    SetChrFlags(0xF9, 0x1000)

    def lambda_1C1A():
        OP_8E(0xFE, 0x1B76, 0x0, 0xFFFFEA16, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C1A)

    def lambda_1C35():
        OP_8E(0xFE, 0x20F8, 0x0, 0xFFFFE408, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1C35)
    Sleep(200)

    def lambda_1C55():
        OP_8E(0xFE, 0x1BB2, 0x0, 0xFFFFE1CE, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1C55)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x101, 0)
    WaitChrThread(0x107, 0x1)
    SetChrChipByIndex(0x107, 20)
    SetChrSubChip(0x107, 0)
    WaitChrThread(0xF9, 0x1)
    SetChrSubChip(0xF9, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1CAB"),
        (3, "loc_1CB3"),
        (4, "loc_1CBB"),
        (7, "loc_1CC3"),
        (SWITCH_DEFAULT, "loc_1CCB"),
    )


    label("loc_1CAB")

    SetChrChipByIndex(0xF9, 8)
    Jump("loc_1CCB")

    label("loc_1CB3")

    SetChrChipByIndex(0xF9, 11)
    Jump("loc_1CCB")

    label("loc_1CBB")

    SetChrChipByIndex(0xF9, 14)
    Jump("loc_1CCB")

    label("loc_1CC3")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_1CCB")

    label("loc_1CCB")


    ChrTalk(    #40
        0x101,
        "#1005F#5P阿加特！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x106,
        (
            "#054F#2P虽然已经出现裂痕了，\x01",
            "但是还不到破坏的地步！\x02\x03",

            "既然如此，\x01",
            "只好再制造一次机会了！\x02\x03",

            "帮我个忙！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#1006F#5P当然！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x107,
        "#062F#5P好！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D9A")

    ChrTalk(    #44
        0x103,
        "#024F#5P……上了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E12")

    label("loc_1D9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DC3")

    ChrTalk(    #45
        0x105,
        "#046F#5P……上了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E12")

    label("loc_1DC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DEC")

    ChrTalk(    #46
        0x104,
        "#530F#5P……上吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E12")

    label("loc_1DEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E12")

    ChrTalk(    #47
        0x108,
        "#076F#5P……上了！\x02",
    )

    CloseMessageWindow()

    label("loc_1E12")

    Fade(500)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 125)
    OP_70(0x0, 0xB4)
    Sleep(1300)

    def lambda_1E35():
        OP_6B(1500, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E35)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    Sleep(800)
    FadeToBright(0, 0)
    OP_0D()
    OP_44(0x101, 0x2)
    OP_23(0x90)
    Battle(0x44F, 0x0, 0x0, 0x80, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1E95"),
        (SWITCH_DEFAULT, "loc_1E9A"),
    )


    label("loc_1E95")

    OP_B4(0x0)
    Jump("loc_1E9A")

    label("loc_1E9A")

    OP_20(0x0)
    Return()

    # Function_5_BE5 end

    def Function_6_1EA0(): pass

    label("Function_6_1EA0")

    ClearChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 24)
    OP_96(0x106, 0xF14, 0x0, 0xFFFFED5E, 0x1F4, 0x1770)
    OP_8C(0x106, 0, 0)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 2)
    SetChrChipByIndex(0x106, 28)
    Return()

    # Function_6_1EA0 end

    def Function_7_1EDD(): pass

    label("Function_7_1EDD")

    ClearChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 24)
    OP_96(0x106, 0x2490, 0x0, 0xFFFFEC82, 0x1F4, 0x1770)
    OP_8C(0x106, 0, 0)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 2)
    SetChrChipByIndex(0x106, 28)
    Return()

    # Function_7_1EDD end

    def Function_8_1F1A(): pass

    label("Function_8_1F1A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(9500, 9450, 12390, 0)
    OP_67(0, 5510, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(346000, 0)
    OP_6E(510, 0)
    OP_71(0x1, 0x4)
    SetChrPos(0x106, 4950, 0, -2860, 0)
    SetChrPos(0x101, 3900, 0, -3700, 0)
    SetChrPos(0x107, 5990, 0, -3790, 0)
    SetChrPos(0xF9, 5500, 0, -4500, 0)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 3)
    SetChrChipByIndex(0x106, 28)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x107, 20)
    SetChrSubChip(0x107, 0)
    SetChrSubChip(0xF9, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1FEE"),
        (3, "loc_1FF6"),
        (4, "loc_1FFE"),
        (7, "loc_2006"),
        (SWITCH_DEFAULT, "loc_200E"),
    )


    label("loc_1FEE")

    SetChrChipByIndex(0xF9, 8)
    Jump("loc_200E")

    label("loc_1FF6")

    SetChrChipByIndex(0xF9, 11)
    Jump("loc_200E")

    label("loc_1FFE")

    SetChrChipByIndex(0xF9, 14)
    Jump("loc_200E")

    label("loc_2006")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_200E")

    label("loc_200E")

    OP_A1(0xA, 0x0)
    SetChrPos(0xA, 10000, 300, 14130, 192)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 630)
    OP_70(0x0, 0x280)
    OP_8C(0xB, 180, 0)
    OP_CF(0xB, 0x0, "Frame127_FireEmitter")
    SetChrFlags(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1964), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x249F0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    OP_43(0xA, 0x0, 0x0, 0x19)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 640)
    OP_70(0x0, 0x29E)
    Sleep(3000)
    Fade(500)
    OP_6D(4300, 0, -3270, 0)
    OP_67(0, 7030, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_2107():
        OP_6D(4300, 0, -4270, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2107)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2171")
    OP_62(0xF9, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_21A5")

    label("loc_2171")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2193")
    OP_62(0xF9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_21A5")

    label("loc_2193")

    OP_62(0xF9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_21A5")

    OP_43(0xF9, 0x1, 0x0, 0x12)
    Sleep(100)
    OP_43(0x101, 0x1, 0x0, 0xF)
    Sleep(50)
    OP_43(0x107, 0x1, 0x0, 0x11)
    Sleep(100)
    OP_43(0x106, 0x1, 0x0, 0x10)
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #48
        0x107,
        "#065F#6P啊、啊呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1005F#6P呜……\x01",
            "应该打倒了才对啊！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_225A")

    ChrTalk(    #50
        0x103,
        (
            "#523F#6P无限的生命力……\x01",
            "和传说一样！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_230F")

    label("loc_225A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2296")

    ChrTalk(    #51
        0x105,
        (
            "#042F#6P无限的生命力……\x01",
            "和传说一样！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_230F")

    label("loc_2296")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22D4")

    ChrTalk(    #52
        0x104,
        (
            "#039F#6P无限的生命力……\x01",
            "和传说一样吗！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_230F")

    label("loc_22D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_230F")

    ChrTalk(    #53
        0x108,
        (
            "#077F#6P无限的生命力……\x01",
            "和传说一样啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_230F")

    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2331():
        OP_6D(3260, 8370, -1910, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2331)

    def lambda_2349():
        OP_67(0, 2800, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2349)

    def lambda_2361():
        OP_6B(3400, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2361)

    def lambda_2371():
        OP_6C(315000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2371)

    def lambda_2381():
        OP_6E(342, 2500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2381)
    WaitChrThread(0x101, 0x0)
    Sleep(1500)
    Fade(500)
    OP_6D(4300, 0, -4270, 0)
    OP_67(0, 7030, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #54
        0x106,
        (
            "#054F#5P提妲！\x01",
            "你带了闪光弹吗！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)
    Sleep(500)

    ChrTalk(    #55
        0x107,
        "#064F#6P呜哎……带了！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2491")

    ChrTalk(    #56
        0x106,
        (
            "#054F#5P用那个扰乱龙的视线！\x02\x03",

            "艾丝蒂尔，雪拉扎德！\x02\x03",

            "别让他动，哪怕一下子也行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25B7")

    label("loc_2491")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24F6")

    ChrTalk(    #57
        0x106,
        (
            "#054F#5P用那个扰乱龙的视线！\x02\x03",

            "艾丝蒂尔，公主殿下！\x02\x03",

            "别让他动，哪怕一下子也行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25B7")

    label("loc_24F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_255B")

    ChrTalk(    #58
        0x106,
        (
            "#054F#5P用那个扰乱龙的视线！\x02\x03",

            "艾丝蒂尔，奥利维尔！\x02\x03",

            "别让他动，哪怕一下子也行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25B7")

    label("loc_255B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25B7")

    ChrTalk(    #59
        0x106,
        (
            "#054F#5P用那个扰乱龙的视线！\x02\x03",

            "艾丝蒂尔，金！\x02\x03",

            "别让他动，哪怕一下子也行！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25B7")


    ChrTalk(    #60
        0x101,
        "#1020F#6P咦咦！？\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 23)
    SetChrSubChip(0x106, 0)
    OP_21()
    OP_1D(0x2B)
    Sleep(500)

    def lambda_25F5():
        OP_69(0xFE, 0x5DC)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_25F5)
    OP_67(0, 4500, -10000, 1500)
    OP_C4(0x0, 0x40)
    OP_6A(0x106)

    def lambda_261D():

        label("loc_261D")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_261D")

    QueueWorkItem2(0x101, 1, lambda_261D)

    def lambda_262E():

        label("loc_262E")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_262E")

    QueueWorkItem2(0x107, 1, lambda_262E)

    def lambda_263F():

        label("loc_263F")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_263F")

    QueueWorkItem2(0xF9, 1, lambda_263F)
    ClearChrFlags(0x106, 0x2)
    ClearChrFlags(0x106, 0x20)
    ClearChrFlags(0x106, 0x10)
    SetChrFlags(0x106, 0x4)
    SetChrFlags(0x106, 0x20)
    SetChrFlags(0x106, 0x1000)
    Sleep(500)
    OP_43(0x106, 0x0, 0x0, 0xD)
    OP_8E(0x106, 0xFFFFF0CE, 0x0, 0xFFFFFE8E, 0x2710, 0x0)
    OP_44(0x106, 0x0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x106, 2)
    OP_96(0x106, 0xFFFFEC32, 0x7D0, 0x53C, 0x9C4, 0x2710)
    SetChrSubChip(0x106, 3)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x106, 270, 0)
    SetChrSubChip(0x106, 4)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x106, 6)
    OP_96(0x106, 0xFFFFDDF0, 0xFA0, 0x62C, 0x9C4, 0x2710)
    SetChrSubChip(0x106, 7)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x106, 0, 0)
    SetChrSubChip(0x106, 6)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x106, 2)
    OP_96(0x106, 0xFFFFD698, 0x1770, 0x1112, 0x9C4, 0x2710)
    SetChrSubChip(0x106, 3)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    SetChrSubChip(0x106, 4)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x106, 6)
    OP_96(0x106, 0xFFFFD1A2, 0x1F40, 0x1DE2, 0x9C4, 0x2710)
    SetChrSubChip(0x106, 7)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x106, 90, 0)
    SetChrSubChip(0x106, 0)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x106, 2)
    OP_96(0x106, 0xFFFFE55C, 0x2710, 0x1EDC, 0x9C4, 0x2710)
    SetChrSubChip(0x106, 3)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    SetChrChipByIndex(0x106, 23)
    SetChrSubChip(0x106, 0)
    ClearChrFlags(0x106, 0x20)
    Sleep(200)
    OP_6A(0xFF)
    OP_C4(0x1, 0x40)

    def lambda_27CD():
        OP_6B(2800, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27CD)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 8)
    SetChrChipByIndex(0x106, 32)
    OP_0D()
    Sleep(300)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(500)

    def lambda_2806():

        label("loc_2806")

        OP_99(0xFE, 0x9, 0xF, 0x5DC)
        OP_48()
        Jump("loc_2806")

    QueueWorkItem2(0x106, 2, lambda_2806)
    Sleep(1000)
    Fade(500)
    OP_6D(4300, 0, -4270, 0)
    OP_67(0, 7030, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_44(0x101, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)
    OP_0D()

    ChrTalk(    #61
        0x107,
        "#560F#4P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28B1")

    ChrTalk(    #62
        0x103,
        (
            "#020F#6P原来如此……\x01",
            "是这样啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2940")

    label("loc_28B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28E7")

    ChrTalk(    #63
        0x105,
        (
            "#040F#6P原来如此……\x01",
            "是这样吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2940")

    label("loc_28E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2916")

    ChrTalk(    #64
        0x104,
        "#030F#6P呼……是这样吗！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2940")

    label("loc_2916")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2940")

    ChrTalk(    #65
        0x108,
        "#070F#6P……是这样吗！\x02",
    )

    CloseMessageWindow()

    label("loc_2940")

    TurnDirection(0x101, 0x107, 500)

    ChrTalk(    #66
        0x101,
        (
            "#1005F#5P提妲！\x01",
            "往高打，别打中！\x02\x03",

            "我们去阻止住它！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #67
        0x107,
        "#062F#4P嗯……！\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x1, "Scraft\\\\sc003_12.eff")
    LoadEffect(0x2, "battle\\\\btgun60.eff")
    OP_8C(0x107, 0, 400)
    OP_8C(0x101, 0, 400)
    OP_8C(0xF9, 0, 400)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 22)
    SetChrSubChip(0x107, 1)
    OP_0D()
    Sleep(500)
    WaitChrThread(0x101, 0x3)
    PlayEffect(0x2, 0xFF, 0x107, 0, 500, 500, 0, -45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2A38():
        OP_99(0x107, 0x1, 0xD, 0x5DC)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2A38)
    PlayEffect(0x1, 0xFF, 0xFF, 5990, 11000, -2000, 0, -70, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Fade(500)
    OP_6D(7850, 19290, 3840, 0)
    OP_67(0, 8119, -10000, 0)
    OP_6B(1530, 0)
    OP_6C(315000, 0)
    OP_6E(594, 0)
    OP_0D()
    Sleep(200)
    LoadEffect(0x3, "map\\\\mp080_00.eff")
    PlayEffect(0x3, 0x1, 0xFF, 7490, 22750, 4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x12D, 0x0, 0x64)
    Sleep(1000)
    OP_82(0x1, 0x2)
    OP_22(0x195, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    Sleep(2000)
    Fade(500)
    OP_6D(4140, 0, -4630, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(3310, 0)
    OP_6C(302000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #68
        0x101,
        "#1002F#5P（……就是现在！）\x02",
    )

    CloseMessageWindow()

    def lambda_2BB5():
        OP_6D(6170, 3860, 9530, 2000)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2BB5)

    def lambda_2BCD():
        OP_67(0, 5160, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2BCD)

    def lambda_2BE5():
        OP_6B(3200, 2000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2BE5)

    def lambda_2BF5():
        OP_6C(315000, 2000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_2BF5)

    def lambda_2C05():
        OP_6E(447, 2000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2C05)
    LoadEffect(0x1, "scraft\\\\sc000_11.eff")
    OP_43(0x101, 0x1, 0x0, 0x13)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_2C46"),
        (3, "loc_2C50"),
        (4, "loc_2C6F"),
        (7, "loc_2C79"),
        (SWITCH_DEFAULT, "loc_2C83"),
    )


    label("loc_2C46")

    OP_43(0xF9, 0x1, 0x0, 0x15)
    Jump("loc_2C83")

    label("loc_2C50")

    LoadEffect(0x3, "battle\\btgun00.eff")
    OP_43(0xF9, 0x1, 0x0, 0x14)
    Jump("loc_2C83")

    label("loc_2C6F")

    OP_43(0xF9, 0x1, 0x0, 0x16)
    Jump("loc_2C83")

    label("loc_2C79")

    OP_43(0xF9, 0x1, 0x0, 0x17)
    Jump("loc_2C83")

    label("loc_2C83")

    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF9, 0x1)

    def lambda_2C93():

        label("loc_2C93")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_2C93")

    QueueWorkItem2(0x101, 3, lambda_2C93)

    def lambda_2CA4():

        label("loc_2CA4")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_2CA4")

    QueueWorkItem2(0xF9, 3, lambda_2CA4)
    WaitChrThread(0xF9, 0x1)
    SetChrFlags(0x107, 0x80)

    def lambda_2CBF():
        OP_6D(3460, 0, 11500, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CBF)

    def lambda_2CD7():
        OP_67(0, 3840, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CD7)

    def lambda_2CEF():
        OP_6B(5090, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2CEF)

    def lambda_2CFF():
        OP_6C(327000, 2500)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2CFF)

    def lambda_2D0F():
        OP_6E(358, 2500)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_2D0F)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 675)
    OP_70(0x0, 0x2CB)
    Sleep(1000)
    OP_22(0x88, 0x0, 0x64)
    OP_73(0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(3240, 0, 860, 0)
    OP_67(0, 4340, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(3000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(2000)
    Fade(500)
    OP_44(0x101, 0x3)
    OP_44(0xF9, 0x3)
    SetChrPos(0x101, -3310, 0, -12120, 0)
    SetChrPos(0x107, -1730, 0, -13800, 0)
    SetChrPos(0xF9, -2970, 0, -14040, 0)
    OP_6D(-6970, 10090, 7890, 0)
    OP_67(0, 3200, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_44(0x106, 0x2)
    ClearChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 27)
    OP_C4(0x0, 0x40)
    OP_69(0x106, 0x0)
    OP_6A(0x106)
    OP_0D()
    Sleep(500)

    ChrTalk(    #69
        0x106,
        "#053F#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_2E68():
        OP_6B(3200, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2E68)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 8)
    SetChrChipByIndex(0x106, 32)
    OP_0D()

    ChrTalk(    #70 op#5
        0x106,
        "#054F#5S呜哦哦哦哦哦哦哦！！\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)
    Fade(250)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 8)
    SetChrChipByIndex(0x106, 32)

    def lambda_2EDE():

        label("loc_2EDE")

        OP_99(0xFE, 0x9, 0xF, 0x7D0)
        OP_48()
        Jump("loc_2EDE")

    QueueWorkItem2(0x106, 2, lambda_2EDE)
    Sleep(300)
    LoadEffect(0x1, "map\\\\mp009_00.eff")
    LoadEffect(0x2, "map\\\\mp081_00.eff")
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x106, 0x2)
    SetChrFlags(0x106, 0x4)

    def lambda_2F35():
        OP_6C(0, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2F35)
    SetChrSubChip(0x106, 17)
    Sleep(200)
    SetChrSubChip(0x106, 18)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2F59():
        OP_96(0x106, 0xA5A, 0x640, 0xFFFFF31C, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_2F59)
    Sleep(500)
    Fade(500)
    OP_6D(840, 0, -2170, 0)
    OP_67(0, 20860, -10000, 0)
    OP_6C(327000, 0)
    OP_6B(890, 0)
    OP_6E(503, 0)

    def lambda_2FBE():
        OP_6D(2000, 0, -2900, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2FBE)

    def lambda_2FD6():
        OP_6B(630, 500)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_2FD6)
    SetChrSubChip(0x106, 19)
    SetChrFlags(0x106, 0x800)
    WaitChrThread(0x106, 0x0)
    WaitChrThread(0x106, 0x1)
    OP_6A(0xFF)
    OP_C4(0x1, 0x40)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x1F4)
    OP_20(0x0)
    OP_22(0x9B, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 3000, 1700, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 2650, 1600, -3300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_75(0x0, 0xC, 0x7)
    OP_22(0x268, 0x0, 0x64)
    Sleep(300)
    Sleep(1000)
    OP_6F(0x0, 720)
    OP_70(0x0, 0x32A)
    OP_22(0x195, 0x0, 0x64)
    ClearChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 25)
    SetChrSubChip(0x106, 6)
    OP_8C(0x106, 45, 0)
    SetChrFlags(0x106, 0x800)
    SetChrFlags(0x106, 0x20)
    OP_82(0x0, 0x2)

    def lambda_30D9():
        OP_96(0x106, 0x370, 0x0, 0xFFFFE3B8, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_30D9)

    def lambda_30F7():
        OP_99(0xFE, 0x5, 0x0, 0x9C4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_30F7)
    WaitChrThread(0x106, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_91(0x106, 0x0, 0x0, 0xFFFFF830, 0xFA0, 0x0)
    WaitChrThread(0x106, 0x1)
    SetChrChipByIndex(0x106, 26)

    def lambda_312F():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_312F)
    Sleep(500)
    Fade(500)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(5300, 0, 8070, 0)
    OP_67(0, 7510, -10000, 0)
    OP_6B(3680, 0)
    OP_6C(341000, 0)
    OP_6E(435, 0)
    ClearChrFlags(0x106, 0x800)
    Sleep(2500)
    OP_22(0x88, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x193, 0x0, 0x64)
    OP_73(0x0)
    Sleep(300)
    Fade(500)
    OP_6D(-2870, 0, -12330, 0)
    OP_67(0, 6010, -10000, 0)
    OP_6B(2490, 0)
    OP_6C(336000, 0)
    OP_6E(329, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x107, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x107, 65535)
    SetChrChipByIndex(0xF9, 65535)
    ClearChrFlags(0x107, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0xF9, 0x80)
    OP_0D()
    OP_75(0x0, 0xD, 0x7)
    Sleep(500)

    ChrTalk(    #71
        0x101,
        "#1008F成功了……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3270")

    ChrTalk(    #72
        0x103,
        "#021F#6P『福音』坏了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_32FA")

    label("loc_3270")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32A1")

    ChrTalk(    #73
        0x105,
        "#542F#6P『福音』坏了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_32FA")

    label("loc_32A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32D1")

    ChrTalk(    #74
        0x104,
        "#030F『福音』坏了吗……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_32FA")

    label("loc_32D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32FA")

    ChrTalk(    #75
        0x108,
        "#070F『福音』坏了吗！\x02",
    )

    CloseMessageWindow()

    label("loc_32FA")

    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #76
        0x107,
        "#065F#6P阿加特哥哥！！！\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x1)
    Sleep(300)

    def lambda_333C():
        OP_8E(0xFE, 0x244, 0x0, 0xFFFFD6FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_333C)
    Sleep(300)

    def lambda_335C():
        OP_8E(0xFE, 0xFFFFFD3A, 0x0, 0xFFFFDF30, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_335C)

    def lambda_3377():
        OP_6D(-330, 0, -7100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3377)

    def lambda_338F():
        OP_67(0, 5350, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_338F)

    def lambda_33A7():
        OP_6C(348000, 3000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_33A7)
    Sleep(100)

    def lambda_33BC():
        OP_8E(0xFE, 0xFFFFFD1C, 0x0, 0xFFFFD760, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_33BC)
    WaitChrThread(0x107, 0x1)

    def lambda_33DC():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_33DC)
    WaitChrThread(0x101, 0x1)

    def lambda_33EF():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33EF)
    WaitChrThread(0xF9, 0x1)
    TurnDirection(0xF9, 0x106, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #77
        0x107,
        (
            "#065F#6P阿加特哥哥！\x01",
            "不要紧吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x106,
        "#053F#5P啊啊……没问题。\x02",
    )

    CloseMessageWindow()
    OP_99(0x106, 0x3, 0x0, 0x5DC)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x106, 0x800)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x106, 225, 400)
    Sleep(500)

    ChrTalk(    #79
        0x106,
        (
            "#051F#2P看来……\x01",
            "好像很顺利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#1001F#5P嗯嗯！　很成功哦！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3504")

    ChrTalk(    #81
        0x103,
        (
            "#021F#6P呵呵，不是被你抢走\x01",
            "风头了嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_359D")

    label("loc_3504")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3537")

    ChrTalk(    #82
        0x105,
        "#041F#6P阿加特……太厉害了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_359D")

    label("loc_3537")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3571")

    ChrTalk(    #83
        0x104,
        (
            "#031F#6P哎呀哎呀，\x01",
            "风头都被抢走了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_359D")

    label("loc_3571")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_359D")

    ChrTalk(    #84
        0x108,
        "#071F#6P哈哈，真了不起！\x02",
    )

    CloseMessageWindow()

    label("loc_359D")


    ChrTalk(    #85
        0x106,
        (
            "#051F#2P嘿嘿嘿……\x02\x03",

            "龙也总算被打倒了，\x01",
            "该说是告一段落吧──\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #86
        "\x07\x05…………漂亮………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3691")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_36CF")

    label("loc_3691")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36B8")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_36CF")

    label("loc_36B8")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_36CF")

    Sleep(1000)

    ChrTalk(    #87
        0x101,
        "#1020F#5P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x107,
        "#065F刚、刚才的声音是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x106,
        "#055F#2P哪里传来的！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_374F")

    ChrTalk(    #90
        0x103,
        "#024F#6P难不成……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_37CB")

    label("loc_374F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_377C")

    ChrTalk(    #91
        0x105,
        "#043F#6P难、难不成……\x02",
    )

    CloseMessageWindow()
    Jump("loc_37CB")

    label("loc_377C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37A5")

    ChrTalk(    #92
        0x104,
        "#033F#6P哦哦……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_37CB")

    label("loc_37A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37CB")

    ChrTalk(    #93
        0x108,
        "#073F#6P哦哦……！\x02",
    )

    CloseMessageWindow()

    label("loc_37CB")

    OP_43(0xA, 0x0, 0x0, 0xC)

    def lambda_37D8():
        OP_6D(1620, 4000, -2120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37D8)

    def lambda_37F0():
        OP_67(0, 1110, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_37F0)

    def lambda_3808():
        OP_6C(359000, 3000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3808)

    def lambda_3818():
        OP_6B(2950, 3000)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3818)

    def lambda_3828():
        OP_6E(603, 3000)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_3828)
    OP_6F(0x0, 815)
    OP_70(0x0, 0x361)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 870)
    OP_70(0x0, 0x398)
    WaitChrThread(0x106, 0x3)
    Sleep(500)
    SetMessageWindowPos(320, 175, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #94
        (
            "\x07\x05干得漂亮……人类之子们啊。\x02\x03",

            "我名叫『雷格纳特』。\x01",
            "我是长眠于此的龙之眷族。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #95
        0x101,
        "#1004F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x106,
        (
            "#052F#5P这是……\x01",
            "你会说话吗！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #97
        (
            "\x07\x05我并没有像你们\x01",
            "一样的发声器官。\x02\x03",

            "所以只能用“意念”\x01",
            "的方式来同你们讲话。\x02\x03",

            "你们就用平常的方式\x01",
            "出声同我交谈就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #98
        0x106,
        "#055F#5P是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x107,
        "#064F#5P呜哎～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1015F#5P既、既然可以沟通的话，\x01",
            "我想确认一下……\x02\x03",

            "你不会再想\x01",
            "和我们战斗了吧？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #101
        (
            "\x07\x05嗯，我只是\x01",
            "被那机械操纵了而已。\x02\x03",

            "你们干得很好，竟能把我\x01",
            "从束缚中解放出来。\x02\x03",

            "请接受我诚挚的谢意。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #102
        0x101,
        (
            "#1016F#5P啊哈哈……\x01",
            "不、不客气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x106,
        (
            "#053F#5P呼……道谢就不必了。\x02\x03",

            "#057F我们来这里\x01",
            "并不是为了解放你。\x02\x03",

            "而是为了避免你造成更大的破坏。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #104
        (
            "\x07\x05你是说被我攻击的\x01",
            "那些城镇和村子吧……\x02\x03",

            "虽说这并非是我有意而为，\x01",
            "但我本身的确也有不可推卸的责任。\x02\x03",

            "那么……该如何补偿才好呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #105
        0x101,
        (
            "#1025F#5P嗯，不过，反正是\x01",
            "『结社』的人不好……\x02\x03",

            "虽然出现了伤者，\x01",
            "但却没有任何人牺牲……\x02\x03",

            "#1016F只要表达出诚意\x01",
            "应该可以原谅你哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x106,
        "#552F#5P………………………………\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #107
        (
            "\x07\x05唔，诚意吗……\x02\x03",

            "这种东西是否能表达\x01",
            "其实没什么自信……\x02\x03",

            "来，人类的孩子，\x01",
            "再稍微靠近这边一点可以吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #108
        0x101,
        (
            "#1004F#5P唔，嗯？\x01",
            "倒是没什么不可以……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x106,
        "#555F#5P……真是的，在说什么啊。\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0x106, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)

    def lambda_3D77():
        OP_6D(2860, 3050, 3590, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D77)

    def lambda_3D8F():
        OP_67(0, 3540, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3D8F)

    def lambda_3DA7():
        OP_6C(347000, 2000)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3DA7)

    def lambda_3DB7():
        OP_6E(596, 2000)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_3DB7)

    def lambda_3DC7():
        OP_6B(2970, 2000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_3DC7)

    def lambda_3DD7():
        OP_8E(0xFE, 0x35C, 0x0, 0xFFFFF574, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DD7)
    Sleep(100)
    ClearChrFlags(0x106, 0x1000)
    ClearChrFlags(0x106, 0x20)

    def lambda_3E01():
        OP_8E(0xFE, 0x8C0, 0x0, 0xFFFFF452, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3E01)
    Sleep(100)

    def lambda_3E21():
        OP_8E(0xFE, 0x762, 0x0, 0xFFFFEF98, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3E21)
    Sleep(100)

    def lambda_3E41():
        OP_8E(0xFE, 0x1FE, 0x0, 0xFFFFF0BA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3E41)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(300)
    LoadEffect(0x0, "map\\\\mp075_00.eff")
    Sleep(100)
    SetChrPos(0xC, 1100, 9000, -2550, 0)
    SetChrPos(0xD, 2420, 9000, -2650, 0)
    PlayEffect(0x0, 0x1, 0xC, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xD, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0x89, 0x0, 0x64)
    Sleep(2000)

    def lambda_3F1A():
        OP_91(0xFE, 0x0, 0xFFFFDFF8, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3F1A)

    def lambda_3F35():
        OP_91(0xFE, 0x0, 0xFFFFE0C0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3F35)
    Sleep(1000)
    Fade(500)
    OP_6D(2180, 0, -4750, 0)
    OP_67(0, 7100, -10000, 0)
    OP_6B(1240, 0)
    OP_6C(166000, 0)
    OP_6E(611, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 33)
    SetChrSubChip(0x101, 15)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 33)
    SetChrSubChip(0x106, 7)
    OP_0D()
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0xD, 0x1)
    SetChrPos(0xE, 1150, 0, -2550, 0)
    SetChrPos(0xF, 2500, 130, -2650, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Sleep(1000)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_23(0x89)

    ChrTalk(    #110
        0x106,
        "#052F#5P什……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x107,
        "#560F#5P哇……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1004F#5P这是……\x01",
            "七耀石的结晶！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4094")

    ChrTalk(    #113
        0x103,
        (
            "#023F#2P金色的光辉……\x02\x03",

            "蕴藏了空之力的\x01",
            "金耀石结晶对吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4179")

    label("loc_4094")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40E2")

    ChrTalk(    #114
        0x105,
        (
            "#044F#2P金色的光辉……\x02\x03",

            "蕴藏了空之力的\x01",
            "金耀石结晶对吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4179")

    label("loc_40E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4130")

    ChrTalk(    #115
        0x104,
        (
            "#033F#2P金色的光辉……\x02\x03",

            "蕴藏了空之力的\x01",
            "金耀石结晶吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4179")

    label("loc_4130")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4179")

    ChrTalk(    #116
        0x108,
        (
            "#073F#2P金色的光辉……\x02\x03",

            "蕴藏了空之力的\x01",
            "金耀石结晶吗！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4179")

    SetMessageWindowPos(50, 75, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #117
        (
            "\x07\x05这就算是我对自己犯下的过错而作的一点补偿吧。\x02\x03",

            "可以请你们帮忙\x01",
            "交给城镇和村中之长吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(500)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #118
        0x101,
        (
            "#1008F#5P原、原来如此……\x02\x03",

            "#1006F嗯，这样的话──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x106,
        "#053F#5P──不行啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #120
        0x101,
        "#1019F#6P慢、慢着！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x107,
        "#063F#5P阿加特哥哥……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 75, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #122
        (
            "\x07\x05唔，难道是这东西\x01",
            "还不足够表达我的诚意吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #123
        0x106,
        (
            "#053F#5P不是这个意思。\x02\x03",

            "#050F按这块结晶的大小来看……\x01",
            "估计一个价值1千万米拉吧。\x02\x03",

            "再给我们一快相同的结晶吧，\x01",
            "是这块的一万分之一就可以。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        "#1004F#6P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x106,
        (
            "#051F#5P如果是和犯罪无关的事情，\x01",
            "雇用游击士是要收费的。\x02\x03",

            "比如物品的搬运费，\x01",
            "收个１０００米拉就够了。\x02\x03",

            "只要你付了这笔钱，我们就帮你带这块结晶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x107,
        "#560F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#1007F#6P真受不了……\x01",
            "真是死板的家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 75, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #128
        (
            "\x07\x05唔，原来是这样。\x02\x03",

            "那么就收下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_6D(2860, 3050, 3590, 0)
    OP_67(0, 3540, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(347000, 0)
    OP_6E(596, 0)
    OP_0D()
    SetChrPos(0xC, 2420, 9000, -2650, 0)
    PlayEffect(0x0, 0x0, 0xC, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x89, 0x0, 0x64)
    Sleep(200)

    def lambda_4582():
        OP_91(0xFE, 0x0, 0xFFFFE0C0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_4582)
    Sleep(500)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 33)
    SetChrSubChip(0x106, 3)
    WaitChrThread(0xC, 0x3)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 33)
    SetChrSubChip(0xF, 17)
    SetChrPos(0xF, 2500, 200, -2650, 0)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_23(0x89)
    Sleep(300)
    Fade(500)
    ClearChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    SetChrFlags(0xF, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #129
        0x106,
        (
            "#051F#5P好……成交。\x02\x03",

            "这两样东西，我们会负责\x01",
            "送交给村长和市长的。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #130
        (
            "\x07\x05唔，拜托了。\x02\x03",

            "呵呵……话说回来，\x01",
            "刚才的那一击真是相当不错。\x02\x03",

            "当初与银发剑士作战的时候，\x01",
            "还根本派不上什么用……\x02\x03",

            "士别三日，刮目相看啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4716():
        OP_8C(0xFE, 25, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4716)

    ChrTalk(    #131
        0x106,
        "#055F#5P什…什么…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x107,
        (
            "#064F#5P废、废坑的事\x01",
            "你还记着吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(2710, 5820, 8720, 0)
    OP_67(0, 880, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(355000, 0)
    OP_6E(596, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #133
        (
            "\x07\x05虽然我被操纵了，\x01",
            "但还保留着意识。\x02\x03",

            "小姑娘啊。\x01",
            "你的勇气和活泼\x01",
            "相当令人钦佩。\x02\x03",

            "呵呵……\x01",
            "所以说人类真是有趣。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #134
        0x107,
        "#562F#5P啊、啊呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1016F#5P啊哈哈，\x01",
            "你还挺会开玩笑的嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #136
        (
            "\x07\x05唔，还有你……\x02\x03",

            "原来如此，难怪\x01",
            "气味很熟悉。\x02\x03",

            "你是『剑圣』的女儿吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #137
        0x101,
        "#1004F#3S#5P咦……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4947")

    ChrTalk(    #138
        0x103,
        (
            "#023F#5P为、为什么\x01",
            "你会知道老师的事！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49BC")

    label("loc_4947")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4993")

    ChrTalk(    #139
        0x108,
        (
            "#073F#5P这可真令人吃惊……\x01",
            "你怎么知道卡西乌斯大人的？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49BC")

    label("loc_4993")


    ChrTalk(    #140
        0x106,
        (
            "#055F#5P喂喂，为什么\x01",
            "认识大叔啊！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49BC")

    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #141
        (
            "\x07\x05他是２０年前，我开始沉睡之前，\x01",
            "最后遇见的人类之一。\x02\x03",

            "自称要追求剑之道的极至\x01",
            "而鲁莽地向我挑战……\x02\x03",

            "他现在还好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #142
        0x101,
        (
            "#1015F#5P嗯、嗯……\x01",
            "依旧还是生龙活虎的样子。\x02\x03",

            "#1019F……只是没想到\x01",
            "居然连龙都认识啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AEB")

    ChrTalk(    #143
        0x105,
        (
            "#045F#5P呵呵……\x01",
            "不愧是卡西乌斯先生。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4F")

    label("loc_4AEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B29")

    ChrTalk(    #144
        0x104,
        (
            "#031F#5P呵呵，不愧是\x01",
            "卡西乌斯·布莱特。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4F")

    label("loc_4B29")


    ChrTalk(    #145
        0x106,
        "#551F#5P真是个不得了的大叔啊……\x02",
    )

    CloseMessageWindow()

    label("loc_4B4F")


    ChrTalk(    #146
        0x101,
        (
            "#1004F#5P啊，这么说来……\x02\x03",

            "#1002F对了，『雷格纳特』。\x01",
            "可以问你件事吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #147
        "\x07\x05唔，什么？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #148
        0x101,
        (
            "#1002F#5P在你身上装置『福音』的人，\x01",
            "就是那个叫莱维的男子吧？\x02\x03",

            "他曾经说过『实验』什么的……\x01",
            "你知道究竟是什么实验吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #149
        (
            "\x07\x05#5P唔……我要解释一下。\x02\x03",

            "将漆黑的机关装在我身上的\x01",
            "不是那个银发剑士。\x02\x03",

            "是一位被称为教授，\x01",
            "拥有神秘力量的男人。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #150
        0x101,
        "#1005F#5P咦咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x106,
        "#052F#5P居然……！？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #152
        (
            "\x07\x05银发剑士是陪伴着教授\x01",
            "一同出现在这里的。\x02\x03",

            "而在我失控之后，\x01",
            "他用尽了各种手段，\x01",
            "力图避免我造成更大的破坏。\x02\x03",

            "如果不是有他的阻止，\x01",
            "我想我一定会将整个城镇和村子\x01",
            "都破坏殆尽的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #153
        0x101,
        "#1026F#5P不、不会吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x106,
        "#552F#5P这家伙……到底想干什么。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #155
        (
            "\x07\x05而『教授』的目的只有一个。\x02\x03",

            "就是看那个机关是否对我有效，\x01",
            "以此来确认作为『辉之环』的『福音』\x02\x03",

            "的完成度。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #156
        0x106,
        "#054F#5P什…什么…！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x107,
        "#065F#5P啊，『辉之环』！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        (
            "#1020F#5P等、等一下！\x02\x03",

            "莫非你知道『辉之环』\x01",
            "是什么东西！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #159
        (
            "\x07\x05…………………………………\x02\x03",

            "那是无所存在，\x01",
            "却又无处不在的东西。\x02\x03",

            "它的存在赋予了人们无限的力量和睿智。\x01",
            "同时，也赋予了人们无尽的绝望。\x02\x03",

            "当其迫近在眼前的时候……\x01",
            "人们必须要作出一个回答。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #160
        0x101,
        "#1004F#5P咦……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5051")

    ChrTalk(    #161
        0x103,
        (
            "#022F#5P那是……\x01",
            "什么意思？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50EC")

    label("loc_5051")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5085")

    ChrTalk(    #162
        0x105,
        (
            "#043F#5P那是……\x01",
            "什么意思呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50EC")

    label("loc_5085")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50BB")

    ChrTalk(    #163
        0x104,
        (
            "#032F#5P唔……\x01",
            "那是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50EC")

    label("loc_50BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50EC")

    ChrTalk(    #164
        0x108,
        (
            "#072F#5P唔……\x01",
            "那是什么意思？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50EC")

    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #165
        (
            "\x07\x05我能说的只有这些。\x02\x03",

            "过多的干预，\x01",
            "是古代的盟约所禁止的。\x02\x03",

            "所以我不能帮助你们，\x01",
            "也不能阻止他们。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_6D(990, 9040, 6400, 0)
    OP_67(0, 9540, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(302000, 0)
    OP_6E(537, 0)
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_A1(0xA, 0x1)
    OP_75(0x1, 0xD, 0x7)
    OP_75(0x1, 0xC, 0x7)
    SetChrFlags(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1964), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x249F0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x1, 225)
    OP_70(0x1, 0x113)
    OP_B0(0x1, 0xA)
    OP_6F(0x1, 185)
    OP_70(0x1, 0xE1)
    Sleep(1000)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x1)
    OP_6F(0x1, 225)
    OP_70(0x1, 0xF8)
    OP_B0(0x1, 0xA)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 235)
    OP_70(0x1, 0xF8)
    Fade(500)
    OP_6D(4560, 4330, 2550, 0)
    OP_67(0, 1770, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(359000, 0)
    OP_6E(644, 0)
    OP_43(0x101, 0x0, 0x0, 0xC)
    OP_43(0xA, 0x3, 0x0, 0x9)
    OP_0D()

    ChrTalk(    #166
        0x101,
        "#1020F#5P哇哇……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x106,
        "#052F#5P喂、喂！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(320, 175, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #168
        (
            "\x07\x05再见了，人类的孩子们啊。\x02\x03",

            "在你们找到答案之时，\x01",
            "我或许会再次现身吧。\x02\x03",

            "我期待着那一天的到来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_6D(7520, 0, 15130, 0)
    OP_67(0, 14200, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(340000, 0)
    OP_6E(473, 0)
    OP_44(0xA, 0x3)
    OP_0D()
    OP_43(0xA, 0x3, 0x0, 0xA)
    Fade(500)
    OP_72(0x1, 0x20)
    OP_73(0x1)
    OP_D8(0x1, 0x1F4)
    OP_6F(0x1, 545)
    OP_70(0x1, 0x234)

    def lambda_53FD():
        OP_6D(7000, 3000, 21300, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_53FD)

    def lambda_5415():
        OP_67(0, 18800, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5415)

    def lambda_542D():
        OP_6B(2810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_542D)

    def lambda_543D():
        OP_6C(2000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_543D)

    def lambda_544D():
        OP_6E(595, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_544D)
    OP_73(0x1)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 565)
    OP_70(0x1, 0x249)
    OP_43(0x106, 0x0, 0x0, 0xE)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F7)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1F1A end

    def Function_9_5496(): pass

    label("Function_9_5496")

    Sleep(400)

    label("loc_549B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54B1")
    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    Jump("loc_549B")

    label("loc_54B1")

    Return()

    # Function_9_5496 end

    def Function_10_54B2(): pass

    label("Function_10_54B2")

    OP_22(0x120, 0x0, 0x64)
    Sleep(2100)
    OP_22(0x120, 0x0, 0x64)
    Sleep(2000)
    OP_22(0x120, 0x0, 0x64)
    Sleep(2000)
    Return()

    # Function_10_54B2 end

    def Function_11_54D1(): pass

    label("Function_11_54D1")


    def lambda_54D7():

        label("loc_54D7")

        OP_8C(0xFE, 0, 400)
        OP_48()
        Jump("loc_54D7")

    QueueWorkItem2(0x106, 1, lambda_54D7)
    Sleep(100)

    def lambda_54ED():

        label("loc_54ED")

        OP_8C(0xFE, 0, 400)
        OP_48()
        Jump("loc_54ED")

    QueueWorkItem2(0x101, 1, lambda_54ED)
    Sleep(100)

    def lambda_5503():

        label("loc_5503")

        OP_8C(0xFE, 0, 400)
        OP_48()
        Jump("loc_5503")

    QueueWorkItem2(0x107, 1, lambda_5503)
    Sleep(100)

    def lambda_5519():

        label("loc_5519")

        OP_8C(0xFE, 0, 400)
        OP_48()
        Jump("loc_5519")

    QueueWorkItem2(0xF9, 1, lambda_5519)
    Return()

    # Function_11_54D1 end

    def Function_12_5525(): pass

    label("Function_12_5525")


    def lambda_552B():

        label("loc_552B")

        OP_8C(0xFE, 45, 400)
        OP_48()
        Jump("loc_552B")

    QueueWorkItem2(0x106, 1, lambda_552B)
    Sleep(100)

    def lambda_5541():

        label("loc_5541")

        OP_8C(0xFE, 45, 400)
        OP_48()
        Jump("loc_5541")

    QueueWorkItem2(0x101, 1, lambda_5541)
    Sleep(100)

    def lambda_5557():

        label("loc_5557")

        OP_8C(0xFE, 45, 400)
        OP_48()
        Jump("loc_5557")

    QueueWorkItem2(0x107, 1, lambda_5557)
    Sleep(100)

    def lambda_556D():

        label("loc_556D")

        OP_8C(0xFE, 45, 400)
        OP_48()
        Jump("loc_556D")

    QueueWorkItem2(0xF9, 1, lambda_556D)
    Return()

    # Function_12_5525 end

    def Function_13_5579(): pass

    label("Function_13_5579")

    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 29)
    OP_99(0x106, 0x0, 0x7, 0x9C4)
    OP_99(0x106, 0x0, 0x7, 0x9C4)
    OP_99(0x106, 0x0, 0x7, 0x9C4)
    OP_99(0x106, 0x0, 0x7, 0x9C4)
    OP_99(0x106, 0x0, 0x7, 0x9C4)
    Return()

    # Function_13_5579 end

    def Function_14_55B1(): pass

    label("Function_14_55B1")


    def lambda_55B7():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_55B7)
    Sleep(300)

    def lambda_55D7():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_55D7)
    Sleep(300)

    def lambda_55F7():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_55F7)
    Sleep(300)

    def lambda_5617():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5617)
    Sleep(300)

    def lambda_5637():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5637)
    Sleep(200)

    def lambda_5657():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5657)
    Sleep(200)

    def lambda_5677():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5677)
    Sleep(200)

    def lambda_5697():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5697)
    Sleep(200)

    def lambda_56B7():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_56B7)
    Return()

    # Function_14_55B1 end

    def Function_15_56CD(): pass

    label("Function_15_56CD")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 6)
    OP_91(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 5)
    Return()

    # Function_15_56CD end

    def Function_16_56F6(): pass

    label("Function_16_56F6")

    ClearChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 24)
    OP_91(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 3)
    SetChrChipByIndex(0x106, 28)
    Return()

    # Function_16_56F6 end

    def Function_17_5729(): pass

    label("Function_17_5729")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 21)
    OP_91(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 20)
    Return()

    # Function_17_5729 end

    def Function_18_5752(): pass

    label("Function_18_5752")

    SetChrSubChip(0xF9, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_5770"),
        (3, "loc_5778"),
        (4, "loc_5780"),
        (7, "loc_5788"),
        (SWITCH_DEFAULT, "loc_5790"),
    )


    label("loc_5770")

    SetChrChipByIndex(0xF9, 9)
    Jump("loc_5790")

    label("loc_5778")

    SetChrChipByIndex(0xF9, 12)
    Jump("loc_5790")

    label("loc_5780")

    SetChrChipByIndex(0xF9, 15)
    Jump("loc_5790")

    label("loc_5788")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_5790")

    label("loc_5790")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_57BD"),
        (3, "loc_57C5"),
        (4, "loc_57CD"),
        (7, "loc_57D5"),
        (SWITCH_DEFAULT, "loc_57DD"),
    )


    label("loc_57BD")

    SetChrChipByIndex(0xF9, 8)
    Jump("loc_57DD")

    label("loc_57C5")

    SetChrChipByIndex(0xF9, 11)
    Jump("loc_57DD")

    label("loc_57CD")

    SetChrChipByIndex(0xF9, 14)
    Jump("loc_57DD")

    label("loc_57D5")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_57DD")

    label("loc_57DD")

    Return()

    # Function_18_5752 end

    def Function_19_57DE(): pass

    label("Function_19_57DE")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x1734, 0x0, 0x2436, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_5811():
        OP_96(0xFE, 0x1EBE, 0x9C4, 0x36B0, 0xBB8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_5811)
    Sleep(100)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 7)

    def lambda_583E():
        OP_99(0xFE, 0x0, 0x9, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_583E)
    Sleep(100)
    OP_22(0x1F4, 0x0, 0x64)
    Sleep(300)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 7870, 2800, 15500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x0)
    WaitChrThread(0xFE, 0x2)

    def lambda_58AD():
        OP_96(0xFE, 0x154A, 0x0, 0x334A, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_58AD)

    def lambda_58CB():
        OP_99(0xFE, 0xA, 0xC, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_58CB)
    WaitChrThread(0xFE, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)
    SetChrSubChip(0xFE, 0)
    Sleep(100)
    OP_96(0xFE, 0x47E, 0x0, 0x286E, 0x1F4, 0xFA0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_19_57DE end

    def Function_20_590B(): pass

    label("Function_20_590B")

    Sleep(100)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 12)
    OP_8E(0xFE, 0x10F4, 0x0, 0xFFFFFDEE, 0x2710, 0x0)
    OP_8E(0xF9, 0x2F26, 0x0, 0x1BC6, 0x2710, 0x0)
    OP_22(0xD8, 0x0, 0x64)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 13)

    def lambda_5963():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_5963)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0x104, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 12930, 3530, 13500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x2)
    Sleep(100)

    def lambda_5A0E():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_5A0E)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x3, 0xFF, 0x104, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 12930, 3530, 13500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x2)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 11)
    Return()

    # Function_20_590B end

    def Function_21_5AB9(): pass

    label("Function_21_5AB9")

    Sleep(100)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x10F4, 0x0, 0xFFFFFDEE, 0x2710, 0x0)
    OP_8E(0xFE, 0x2C6A, 0x0, 0x20F8, 0x2710, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_5B0C():
        OP_96(0xFE, 0x32F0, 0x0, 0x32C8, 0xDAC, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_5B0C)
    Sleep(300)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_5B39():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5B39)
    Sleep(100)
    OP_22(0x1F6, 0x0, 0x64)
    Sleep(100)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 12930, 3530, 13500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x0)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0x2D5A, 0x0, 0x1856, 0xC8, 0x1388)
    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_21_5AB9 end

    def Function_22_5BE7(): pass

    label("Function_22_5BE7")

    Sleep(100)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 15)
    OP_8E(0xFE, 0x10F4, 0x0, 0xFFFFFDEE, 0x2710, 0x0)
    OP_8E(0xFE, 0x33FE, 0x0, 0x366A, 0x2710, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 16)

    def lambda_5C3A():
        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5C3A)
    OP_22(0x1F8, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 13310, 800, 15900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x2)

    def lambda_5C9A():
        OP_99(0xFE, 0x1, 0x7, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5C9A)
    OP_22(0x1F8, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 13310, 800, 15900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x2)
    Sleep(100)
    SetChrFlags(0xFE, 0x4)

    def lambda_5D04():
        OP_99(0xFE, 0x1, 0x7, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5D04)

    def lambda_5D14():
        OP_8E(0xFE, 0x3430, 0x1F4, 0x3908, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_5D14)
    OP_22(0x1F8, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 13310, 800, 16500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x0)
    WaitChrThread(0xFE, 0x2)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0x2D5A, 0x0, 0x1856, 0xC8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_22_5BE7 end

    def Function_23_5DA0(): pass

    label("Function_23_5DA0")

    Sleep(100)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 18)
    OP_8E(0xFE, 0x10F4, 0x0, 0xFFFFFDEE, 0x2710, 0x0)
    OP_8E(0xFE, 0x3138, 0x0, 0x23BE, 0x2710, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 30)

    def lambda_5DF3():
        OP_99(0xFE, 0x0, 0x9, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5DF3)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_5E12():
        OP_96(0xFE, 0x3282, 0xDCA, 0x32C8, 0xFA0, 0x2710)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_5E12)
    OP_99(0xFE, 0x0, 0x3, 0xDAC)
    SetChrSubChip(0xFE, 3)
    SetChrChipByIndex(0xFE, 30)
    WaitChrThread(0xFE, 0x0)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 12930, 4000, 14500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x106, 0x3, 0x0, 0x18)
    Sleep(200)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    OP_99(0xFE, 0x4, 0x7, 0x5DC)
    OP_99(0xFE, 0x4, 0x7, 0x5DC)
    OP_A2(0x0)

    def lambda_5EC0():
        OP_99(0xFE, 0x8, 0xF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5EC0)
    Sleep(600)
    PlayEffect(0x1, 0xFF, 0xFF, 12930, 4000, 14500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    OP_22(0x22A, 0x0, 0x64)
    OP_22(0x22A, 0x0, 0x64)
    OP_22(0x22A, 0x0, 0x64)
    OP_22(0x22A, 0x0, 0x64)
    OP_22(0x22A, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)

    def lambda_5F39():
        OP_96(0xFE, 0x34C6, 0x0, 0x2EC2, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_5F39)

    def lambda_5F57():
        OP_99(0xFE, 0x10, 0x17, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5F57)
    WaitChrThread(0xFE, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    Sleep(100)
    OP_96(0xFE, 0x3192, 0x0, 0x16DA, 0x1F4, 0x1388)
    Return()

    # Function_23_5DA0 end

    def Function_24_5FA1(): pass

    label("Function_24_5FA1")

    Sleep(200)

    label("loc_5FA6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5FFE")
    OP_22(0x321, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 12930, 4000, 14500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5FF6")
    OP_23(0x321)
    Jump("loc_5FFE")

    label("loc_5FF6")

    Sleep(100)
    Jump("loc_5FA6")

    label("loc_5FFE")

    Return()

    # Function_24_5FA1 end

    def Function_25_5FFF(): pass

    label("Function_25_5FFF")

    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    Sleep(1000)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    Sleep(1000)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    Sleep(1000)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    Return()

    # Function_25_5FFF end

    def Function_26_60A1(): pass

    label("Function_26_60A1")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_611E"),
        (1, "loc_6124"),
        (SWITCH_DEFAULT, "loc_612A"),
    )


    label("loc_611E")

    OP_A2(0x1200)
    Jump("loc_612A")

    label("loc_6124")

    OP_A2(0x1201)
    Jump("loc_612A")

    label("loc_612A")

    Return()

    # Function_26_60A1 end

    def Function_27_612B(): pass

    label("Function_27_612B")

    ClearMapFlags(0x1)
    OP_6D(97010, 0, 95840, 0)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_27_612B end

    SaveToFile()

Try(main)
