from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3403   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3403.x',
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
        ' ',                                    # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
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
        'ED6_DT29/CH12110 ._CH',             # 00
        'ED6_DT29/CH12111 ._CH',             # 01
        'ED6_DT29/CH12410 ._CH',             # 02
        'ED6_DT29/CH12411 ._CH',             # 03
        'ED6_DT29/CH12250 ._CH',             # 04
        'ED6_DT29/CH12251 ._CH',             # 05
        'ED6_DT29/CH12130 ._CH',             # 06
        'ED6_DT29/CH12131 ._CH',             # 07
        'ED6_DT09/CH10130 ._CH',             # 08
        'ED6_DT09/CH10131 ._CH',             # 09
        'ED6_DT09/CH10750 ._CH',             # 0A
        'ED6_DT09/CH10751 ._CH',             # 0B
        'ED6_DT29/CH12270 ._CH',             # 0C
        'ED6_DT29/CH12271 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12110P._CP',             # 00
        'ED6_DT29/CH12111P._CP',             # 01
        'ED6_DT29/CH12410P._CP',             # 02
        'ED6_DT29/CH12411P._CP',             # 03
        'ED6_DT29/CH12250P._CP',             # 04
        'ED6_DT29/CH12251P._CP',             # 05
        'ED6_DT29/CH12130P._CP',             # 06
        'ED6_DT29/CH12131P._CP',             # 07
        'ED6_DT09/CH10130P._CP',             # 08
        'ED6_DT09/CH10131P._CP',             # 09
        'ED6_DT09/CH10750P._CP',             # 0A
        'ED6_DT09/CH10751P._CP',             # 0B
        'ED6_DT29/CH12270P._CP',             # 0C
        'ED6_DT29/CH12271P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x49,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -39890,
        Z                   = 0,
        Y                   = 38220,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -26760,
        Z                   = 0,
        Y                   = 11040,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2720,
        Z                   = 0,
        Y                   = -14290,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 880,
        Y                   = 0,
        Z                   = -49130,
        Range               = 10060,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF4B7E,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = 10810,
        TriggerZ            = 0,
        TriggerY            = 31850,
        TriggerRange        = 1000,
        ActorX              = 11490,
        ActorZ              = 0,
        ActorY              = 31930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3060,
        TriggerZ            = 0,
        TriggerY            = -61790,
        TriggerRange        = 1000,
        ActorX              = -3060,
        ActorZ              = 0,
        ActorY              = -62430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10970,
        TriggerZ            = 0,
        TriggerY            = -47730,
        TriggerRange        = 1000,
        ActorX              = -11680,
        ActorZ              = 0,
        ActorY              = -47710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_21A",          # 00, 0
        "Function_1_21B",          # 01, 1
        "Function_2_2B9",          # 02, 2
        "Function_3_2CF",          # 03, 3
        "Function_4_414",          # 04, 4
        "Function_5_52B",          # 05, 5
        "Function_6_642",          # 06, 6
        "Function_7_9C5",          # 07, 7
        "Function_8_A5E",          # 08, 8
        "Function_9_AC4",          # 09, 9
        "Function_10_CAE",         # 0A, 10
        "Function_11_EF6",         # 0B, 11
        "Function_12_F48",         # 0C, 12
    )


    def Function_0_21A(): pass

    label("Function_0_21A")

    Return()

    # Function_0_21A end

    def Function_1_21B(): pass

    label("Function_1_21B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D")
    OP_6F(0x0, 0)
    Jump("loc_234")

    label("loc_22D")

    OP_6F(0x0, 60)

    label("loc_234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_246")
    OP_6F(0x1, 0)
    Jump("loc_24D")

    label("loc_246")

    OP_6F(0x1, 60)

    label("loc_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F")
    OP_6F(0x2, 0)
    Jump("loc_266")

    label("loc_25F")

    OP_6F(0x2, 60)

    label("loc_266")

    OP_BE(0x0, 0x4, 0x2, 0x2, 0x0, 0x1, -4380, -1120, -52330, 3600, 3000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2AC")
    OP_82(0x87, 0x0)
    OP_82(0x88, 0x0)
    OP_82(0x89, 0x0)
    OP_82(0x8A, 0x0)
    OP_82(0x8B, 0x0)
    OP_82(0x8C, 0x0)
    OP_82(0x91, 0x0)
    OP_22(0x1C7, 0x0, 0x64)
    Jump("loc_2B8")

    label("loc_2AC")

    OP_43(0x8, 0x0, 0x0, 0xA)
    OP_22(0x10B, 0x0, 0x64)

    label("loc_2B8")

    Return()

    # Function_1_21B end

    def Function_2_2B9(): pass

    label("Function_2_2B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2B9")

    label("loc_2CE")

    Return()

    # Function_2_2B9 end

    def Function_3_2CF(): pass

    label("Function_3_2CF")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    AddSepith(0x0, 0x14)
    AddSepith(0x1, 0x14)
    AddSepith(0x2, 0x14)
    AddSepith(0x3, 0x14)
    AddSepith(0x4, 0x14)
    AddSepith(0x5, 0x14)
    AddSepith(0x6, 0x14)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x00得到了\x07\x02#56I地之耀晶片×２０\x01",
            "\x07\x02#57I水之耀晶片×２０\x01",
            "\x07\x02#58I火之耀晶片×２０\x01",
            "\x07\x02#59I风之耀晶片×２０\x01",
            "\x07\x02#62I时之耀晶片×２０\x01",
            "\x07\x02#60I空之耀晶片×２０\x01",
            "\x07\x02#61I幻之耀晶片×２０\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1568)
    Jump("loc_402")

    label("loc_3E8")


    AnonymousTalk(    #1
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_402")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2CF end

    def Function_4_414(): pass

    label("Function_4_414")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_483")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\xF9\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x156A)
    Jump("loc_4E9")

    label("loc_483")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "宝箱里装有\x1F\xF9\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF9\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_4E9")

    Jump("loc_51D")

    label("loc_4EC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_51D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_414 end

    def Function_5_52B(): pass

    label("Function_5_52B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_603")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xC4, 1)"), scpexpr(EXPR_END)), "loc_59A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\xC4\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x156B)
    Jump("loc_600")

    label("loc_59A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\xC4\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xC4\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_600")

    Jump("loc_634")

    label("loc_603")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_634")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_52B end

    def Function_6_642(): pass

    label("Function_6_642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_64E")
    Return()

    label("loc_64E")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66E")
    Call(0, 7)
    Call(0, 8)
    FadeToBright(0, 0)

    label("loc_66E")

    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(200)
    Fade(1000)
    OP_6D(-1690, -650, -51270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 4880, 0, -47730, 219)
    SetChrPos(0x107, 6180, 0, -47670, 220)
    SetChrPos(0xF9, 4620, 0, -46710, 234)
    SetChrPos(0xF7, 6170, 0, -48910, 240)
    OP_0D()

    def lambda_71C():
        OP_8E(0xFE, 0xFFFFFE5C, 0x0, 0xFFFF39CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71C)
    Sleep(300)

    def lambda_73C():
        OP_8E(0xFE, 0x46, 0x0, 0xFFFF3486, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_73C)
    Sleep(500)

    def lambda_75C():
        OP_8E(0xFE, 0x23A, 0x0, 0xFFFF38AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_75C)
    Sleep(400)

    def lambda_77C():
        OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0xFFFF3DDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_77C)
    WaitChrThread(0x101, 0x1)

    def lambda_79C():
        OP_8C(0x101, 257, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_79C)

    def lambda_7AA():
        OP_6D(-755, 0, -50870, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7AA)
    WaitChrThread(0xF7, 0x1)

    def lambda_7C7():
        OP_8C(0xF7, 257, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7C7)
    WaitChrThread(0x107, 0x1)

    def lambda_7DA():
        OP_8C(0x107, 257, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_7DA)
    WaitChrThread(0xF9, 0x1)

    def lambda_7ED():
        OP_8C(0xF9, 257, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_7ED)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #8
        0x107,
        (
            "#560F哇……\x01",
            "这里没沸腾呢。\x02\x03",

            "#061F嘿嘿，感觉\x01",
            "好像很舒服呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EE")

    ChrTalk(    #9
        0x104,
        (
            "#030F#5P呼，那么\x01",
            "我们该做的事情\x01",
            "就只有一件了吧。\x02\x03",

            "#031F嘿嘿，坦诚相见！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#1007F#2P别擅自脱掉啦。\x02\x03",

            "#1006F不过也好，看来是不错的温泉，\x01",
            "泡泡脚也不错吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96B")

    label("loc_8EE")


    ChrTalk(    #11
        0x105,
        (
            "#542F#5P的确，满身大汗的，\x01",
            "让人忍不住就想下去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1016F#2P嗯嗯，我也是。\x02\x03",

            "#1006F看来是不错的温泉\x01",
            "泡泡脚也不错吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_99A")

    ChrTalk(    #13
        0x106,
        "#552F……真是的，适可而止一点。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9BF")

    label("loc_99A")


    ChrTalk(    #14
        0x103,
        "#021F呵呵，这就是所谓的足浴吧。\x02",
    )

    CloseMessageWindow()

    label("loc_9BF")

    OP_A2(0x1424)
    EventEnd(0x0)
    Return()

    # Function_6_642 end

    def Function_7_9C5(): pass

    label("Function_7_9C5")

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
        (0, "loc_A3F"),
        (1, "loc_A45"),
        (SWITCH_DEFAULT, "loc_A4B"),
    )


    label("loc_A3F")

    OP_A2(0x1200)
    Jump("loc_A4B")

    label("loc_A45")

    OP_A2(0x1201)
    Jump("loc_A4B")

    label("loc_A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A59")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_A5D")

    label("loc_A59")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_A5D")

    Return()

    # Function_7_9C5 end

    def Function_8_A5E(): pass

    label("Function_8_A5E")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A98")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_AB2")

    label("loc_A98")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_AB2")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_8_A5E end

    def Function_9_AC4(): pass

    label("Function_9_AC4")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #15
        "\x07\x05正好有温度适中的温泉。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "享受足浴。\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B43"),
        (1, "loc_CA4"),
        (SWITCH_DEFAULT, "loc_CA7"),
    )


    label("loc_B43")

    FadeToDark(1000, 0, -1)
    Sleep(600)
    OP_22(0xA2, 0x0, 0x64)
    Sleep(1500)
    OP_22(0xB, 0x0, 0x64)
    Sleep(800)
    OP_0D()
    SetChrPos(0x0, 820, 0, -51320, 90)
    SetChrPos(0x1, 820, 0, -51320, 90)
    SetChrPos(0x2, 820, 0, -51320, 90)
    SetChrPos(0x3, 820, 0, -51320, 90)
    SetChrPos(0x4, 820, 0, -51320, 90)
    SetChrPos(0x5, 820, 0, -51320, 90)
    SetChrPos(0x6, 820, 0, -51320, 90)
    SetChrPos(0x7, 820, 0, -51320, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C02")
    OP_31(0x0, 0xFB, 0x0)

    label("loc_C02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C15")
    OP_31(0x1, 0xFB, 0x0)

    label("loc_C15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C28")
    OP_31(0x2, 0xFB, 0x0)

    label("loc_C28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3B")
    OP_31(0x3, 0xFB, 0x0)

    label("loc_C3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C4E")
    OP_31(0x5, 0xFB, 0x0)

    label("loc_C4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C61")
    OP_31(0x4, 0xFB, 0x0)

    label("loc_C61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C74")
    OP_31(0x6, 0xFB, 0x0)

    label("loc_C74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C87")
    OP_31(0x7, 0xFB, 0x0)

    label("loc_C87")

    OP_8C(0x0, 90, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_CAA")

    label("loc_CA4")

    Jump("loc_CAA")

    label("loc_CA7")

    Jump("loc_CAA")

    label("loc_CAA")

    TalkEnd(0xFF)
    Return()

    # Function_9_AC4 end

    def Function_10_CAE(): pass

    label("Function_10_CAE")

    Call(0, 11)
    OP_43(0x8, 0x3, 0x0, 0xC)
    PlayEffect(0x9B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x9B, 0x1, 0x6E)
    Call(0, 11)
    PlayEffect(0x9C, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x9C, 0x1, 0x6E)
    Call(0, 11)
    PlayEffect(0x9D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x9D, 0x1, 0x6E)
    Call(0, 11)
    PlayEffect(0x9E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x9E, 0x1, 0x6E)
    Call(0, 11)
    PlayEffect(0x9F, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x9F, 0x1, 0x6E)
    Call(0, 11)
    PlayEffect(0xA0, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0xA0, 0x1, 0x6E)
    Call(0, 11)
    PlayEffect(0xA1, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0xA1, 0x1, 0x6E)
    Call(0, 11)
    PlayEffect(0xA2, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0xA2, 0x1, 0x6E)
    Call(0, 11)
    PlayEffect(0xA3, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0xA3, 0x1, 0x6E)
    Return()

    # Function_10_CAE end

    def Function_11_EF6(): pass

    label("Function_11_EF6")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_F17"),
        (1, "loc_F1F"),
        (2, "loc_F27"),
        (3, "loc_F2F"),
        (4, "loc_F37"),
        (SWITCH_DEFAULT, "loc_F3F"),
    )


    label("loc_F17")

    Sleep(500)
    Jump("loc_F47")

    label("loc_F1F")

    Sleep(1000)
    Jump("loc_F47")

    label("loc_F27")

    Sleep(1500)
    Jump("loc_F47")

    label("loc_F2F")

    Sleep(2000)
    Jump("loc_F47")

    label("loc_F37")

    Sleep(2500)
    Jump("loc_F47")

    label("loc_F3F")

    Sleep(3000)
    Jump("loc_F47")

    label("loc_F47")

    Return()

    # Function_11_EF6 end

    def Function_12_F48(): pass

    label("Function_12_F48")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F5E")
    OP_22(0x10D, 0x0, 0x64)
    Sleep(7000)
    Jump("Function_12_F48")

    label("loc_F5E")

    Return()

    # Function_12_F48 end

    SaveToFile()

Try(main)
