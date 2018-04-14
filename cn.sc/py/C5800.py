from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5800   ._SN',
        MapName             = 'Other',
        Location            = 'C5800.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        '居住区域『克雷德尔』外部２',           # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT29/CH12060 ._CH',             # 00
        'ED6_DT29/CH12061 ._CH',             # 01
        'ED6_DT29/CH12190 ._CH',             # 02
        'ED6_DT29/CH12191 ._CH',             # 03
        'ED6_DT29/CH12970 ._CH',             # 04
        'ED6_DT29/CH12971 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH12060P._CP',             # 00
        'ED6_DT29/CH12061P._CP',             # 01
        'ED6_DT29/CH12190P._CP',             # 02
        'ED6_DT29/CH12191P._CP',             # 03
        'ED6_DT29/CH12970P._CP',             # 04
        'ED6_DT29/CH12971P._CP',             # 05
    )

    DeclNpc(
        X                   = -115090,
        Z                   = 0,
        Y                   = -63840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -205120,
        Z                   = -8000,
        Y                   = -101640,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x50B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -180970,
        Z                   = -8000,
        Y                   = -82860,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x50C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -200190,
        Z                   = -8000,
        Y                   = -62040,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x50D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -147140,
        Z                   = 0,
        Y                   = -92600,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x50B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -138240,
        Z                   = 0,
        Y                   = -63500,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x50B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -167890,
        Z                   = 0,
        Y                   = -42410,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x50C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -159230,
        TriggerZ            = 0,
        TriggerY            = -95940,
        TriggerRange        = 1000,
        ActorX              = -158560,
        ActorZ              = 0,
        ActorY              = -95940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -161810,
        TriggerZ            = 0,
        TriggerY            = -33530,
        TriggerRange        = 1000,
        ActorX              = -161810,
        ActorZ              = 0,
        ActorY              = -34220,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1EA",          # 00, 0
        "Function_1_222",          # 01, 1
        "Function_2_271",          # 02, 2
        "Function_3_388",          # 03, 3
        "Function_4_467",          # 04, 4
        "Function_5_4DB",          # 05, 5
        "Function_6_C7B",          # 06, 6
        "Function_7_CC4",          # 07, 7
        "Function_8_D14",          # 08, 8
        "Function_9_D64",          # 09, 9
        "Function_10_DB4",         # 0A, 10
        "Function_11_E3B",         # 0B, 11
        "Function_12_ECC",         # 0C, 12
    )


    def Function_0_1EA(): pass

    label("Function_0_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_200")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_221")

    label("loc_200")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_20C"),
        (SWITCH_DEFAULT, "loc_221"),
    )


    label("loc_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_221")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_221")

    Return()

    # Function_0_1EA end

    def Function_1_222(): pass

    label("Function_1_222")

    OP_16(0x2, 0xFA0, 0xFFFB4CE0, 0xFFFCEED8, 0x230077)
    OP_22(0x1C7, 0x0, 0x64)
    OP_71(0x7, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_250")
    OP_6F(0x5, 0)
    Jump("loc_257")

    label("loc_250")

    OP_6F(0x5, 60)

    label("loc_257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_269")
    OP_6F(0x6, 0)
    Jump("loc_270")

    label("loc_269")

    OP_6F(0x6, 60)

    label("loc_270")

    Return()

    # Function_1_222 end

    def Function_2_271(): pass

    label("Function_2_271")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_349")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_2E0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x00\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x230B)
    Jump("loc_346")

    label("loc_2E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x00\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x00\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_346")

    Jump("loc_37A")

    label("loc_349")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_37A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_271 end

    def Function_3_388(): pass

    label("Function_3_388")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x1E)
    OP_73(0x6)
    OP_6F(0x6, 30)
    AddSepith(0x1, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x5, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "\x07\x00得到了\x07\x02#57I水之耀晶片×１００\x01",
            "\x07\x02#59I风之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x230C)
    Jump("loc_455")

    label("loc_43B")


    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_455")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_388 end

    def Function_4_467(): pass

    label("Function_4_467")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-179400, -7920, -81170, 0)
    OP_67(0, 6920, -10000, 0)
    OP_6B(12360, 0)
    OP_6C(322000, 0)
    OP_6E(451, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(2000)
    OP_22(0x7C, 0x0, 0x64)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5700   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_467 end

    def Function_5_4DB(): pass

    label("Function_5_4DB")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F2")
    Call(0, 10)
    Call(0, 11)

    label("loc_4F2")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_6D(-153000, -8000, -103040, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3770, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x4, 0)
    OP_70(0x4, 0x1E)
    OP_73(0x4)

    def lambda_582():
        OP_6D(-151420, -8000, -108390, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_582)
    OP_43(0x101, 0x1, 0x0, 0x6)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0x7)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x8)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x9)
    Sleep(1500)
    OP_6F(0x4, 30)
    OP_70(0x4, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #5
        0x101,
        "#1025F#5P呼～终于到了外面。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #6
        0x102,
        "#1044F#2P……这里是……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_11(0xED, 0xFF, 0xEE, 0xC350, 0xC3500, 0x0)
    OP_6D(-214540, -8000, -101210, 0)
    OP_67(0, 3870, -10000, 0)
    OP_6B(11840, 0)
    OP_6C(319000, 0)
    OP_6E(262, 0)

    def lambda_677():
        OP_6D(-158900, -4000, -56630, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_677)

    def lambda_68F():
        OP_67(0, 6100, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_68F)
    OP_C8(0x80, 0x46, "C_PLAC26._CH", 0x1, 0x5DC)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Fade(500)
    OP_11(0xED, 0xFF, 0xEE, 0xD6D8, 0x186A0, 0x0)
    OP_6D(-151930, -8000, -108070, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(3730, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_8C(0x101, 270, 0)
    OP_8C(0x102, 270, 0)
    OP_8C(0xF8, 270, 0)
    OP_8C(0xF9, 270, 0)
    OP_6F(0x4, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_795")

    ChrTalk(    #7
        0x104,
        (
            "#035F#6P呼……\x01",
            "多么美丽的街道啊。\x02\x03",

            "#030F看来是古代人\x01",
            "生活的地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91F")

    label("loc_795")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E2")

    ChrTalk(    #8
        0x105,
        (
            "#1382F#6P好漂亮的街道……\x02\x03",

            "看来是古代人\x01",
            "生活的地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91F")

    label("loc_7E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_830")

    ChrTalk(    #9
        0x103,
        (
            "#020F#6P……好漂亮的街道。\x02\x03",

            "应该是古代人\x01",
            "生活的地方吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91F")

    label("loc_830")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87D")

    ChrTalk(    #10
        0x109,
        (
            "#1060F#6P好漂亮的街道……\x02\x03",

            "应该是古代人\x01",
            "生活的地方吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91F")

    label("loc_87D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8CD")

    ChrTalk(    #11
        0x108,
        (
            "#070F#6P嗯，好漂亮的街道……\x02\x03",

            "看来是古代人\x01",
            "生活的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91F")

    label("loc_8CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91F")

    ChrTalk(    #12
        0x107,
        (
            "#064F#6P哇～好漂亮的街道……\x02\x03",

            "#061F看来是古代人\x01",
            "生活的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_973")

    ChrTalk(    #13
        0x106,
        (
            "#051F#6P的确，和我们迫降的地方相比，\x01",
            "更有着人们生活过的气息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B20")

    label("loc_973")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C9")

    ChrTalk(    #14
        0x107,
        (
            "#560F#6P的确，和我们迫降的地方相比，\x01",
            "更有着人们生活过的气息呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B20")

    label("loc_9C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A1D")

    ChrTalk(    #15
        0x108,
        (
            "#070F#6P的确，和我们迫降的地方相比，\x01",
            "更有着人们生活过的气息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B20")

    label("loc_A1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A76")

    ChrTalk(    #16
        0x109,
        (
            "#1060F#6P的确，和我们迫降的地方相比，\x01",
            "好像更有着人们生活过的气息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B20")

    label("loc_A76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ACC")

    ChrTalk(    #17
        0x103,
        (
            "#027F#6P的确，和我们迫降的地方相比，\x01",
            "更有着人们生活过的气息呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B20")

    label("loc_ACC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B20")

    ChrTalk(    #18
        0x105,
        (
            "#1382F#6P的确，和我们迫降的地方相比，\x01",
            "更有着人们生活过的气息呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B20")


    ChrTalk(    #19
        0x101,
        (
            "#1006F#6P嗯……\x01",
            "这里的气氛似乎非常安静祥和。\x02\x03",

            "#1015F但是……为什么过去的人们\x01",
            "要放弃这么美好的都市呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#1035F#6P……调查一下的话，\x01",
            "说不定可以了解到当时的情况。\x02\x03",

            "#1040F反正也要寻找新的路线，\x01",
            "就赶快探索一下这附近吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C06():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C06)
    Sleep(50)

    def lambda_C19():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_C19)
    Sleep(50)

    def lambda_C2C():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_C2C)
    WaitChrThread(0x101, 0x1)
    Sleep(300)

    ChrTalk(    #21
        0x101,
        "#1006F#5P嗯，ＯＫ。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_A2(0x2218)
    EventEnd(0x0)
    Return()

    # Function_5_4DB end

    def Function_6_C7B(): pass

    label("Function_6_C7B")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -151160, -7920, -102500, 180)
    OP_8E(0xFE, 0xFFFDB246, 0xFFFFE0C0, 0xFFFE6236, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFDAF94, 0xFFFFE0C0, 0xFFFE5354, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_C7B end

    def Function_7_CC4(): pass

    label("Function_7_CC4")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -151160, -7920, -102500, 180)
    OP_8E(0xFE, 0xFFFDB246, 0xFFFFE0C0, 0xFFFE6236, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFDB624, 0xFFFFE0C0, 0xFFFE5336, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_7_CC4 end

    def Function_8_D14(): pass

    label("Function_8_D14")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -151160, -7920, -102500, 180)
    OP_8E(0xFE, 0xFFFDB246, 0xFFFFE0C0, 0xFFFE6236, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFDAEB8, 0xFFFFE0C0, 0xFFFE5962, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_D14 end

    def Function_9_D64(): pass

    label("Function_9_D64")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -151160, -7920, -102500, 180)
    OP_8E(0xFE, 0xFFFDB246, 0xFFFFE0C0, 0xFFFE6236, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFDB552, 0xFFFFE0C0, 0xFFFE5980, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_D64 end

    def Function_10_DB4(): pass

    label("Function_10_DB4")

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
        (0, "loc_E2E"),
        (1, "loc_E34"),
        (SWITCH_DEFAULT, "loc_E3A"),
    )


    label("loc_E2E")

    OP_A2(0x1200)
    Jump("loc_E3A")

    label("loc_E34")

    OP_A2(0x1201)
    Jump("loc_E3A")

    label("loc_E3A")

    Return()

    # Function_10_DB4 end

    def Function_11_E3B(): pass

    label("Function_11_E3B")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_11_E3B end

    def Function_12_ECC(): pass

    label("Function_12_ECC")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_12_ECC end

    SaveToFile()

Try(main)
