from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U5110   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U5110.x',
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
        '器皿',                                 # 9
        '器皿',                                 # 10
        '器皿',                                 # 11
        '瓶子',                                 # 12
        '瓶子',                                 # 13
        '餐具',                                 # 14
        '小刀',                                 # 15
        '空杯',                                 # 16
        '基尔巴特',                             # 17
        '',                                     # 18
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
        'ED6_DT06/CH20020 ._CH',             # 00
        'ED6_DT06/CH20021 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT06/CH20020P._CP',             # 00
        'ED6_DT06/CH20021P._CP',             # 01
    )

    DeclNpc(
        X                   = 18160,
        Z                   = 800,
        Y                   = 11100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65536,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18670,
        Z                   = 800,
        Y                   = 12140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65536,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18200,
        Z                   = 800,
        Y                   = 11940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65536,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17600,
        Z                   = 800,
        Y                   = 12140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835008,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17900,
        Z                   = 800,
        Y                   = 11800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835008,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17600,
        Z                   = 800,
        Y                   = 11180,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917504,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18470,
        Z                   = 800,
        Y                   = 11100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 851968,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18350,
        Z                   = 800,
        Y                   = 11550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65537,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 112000,
        Z                   = 0,
        Y                   = -3670,
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
        X                   = 112600,
        Y                   = 0,
        Z                   = 1000,
        Range               = 115170,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7D0,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = 21010,
        TriggerZ            = 0,
        TriggerY            = 15470,
        TriggerRange        = 1000,
        ActorX              = 21010,
        ActorZ              = 2000,
        ActorY              = 15470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 86740,
        TriggerZ            = 0,
        TriggerY            = 41680,
        TriggerRange        = 1000,
        ActorX              = 86740,
        ActorZ              = 1000,
        ActorY              = 41680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 139740,
        TriggerZ            = 0,
        TriggerY            = 41770,
        TriggerRange        = 1000,
        ActorX              = 139740,
        ActorZ              = 1000,
        ActorY              = 41770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 115250,
        TriggerZ            = 0,
        TriggerY            = -34470,
        TriggerRange        = 1000,
        ActorX              = 115250,
        ActorZ              = 1000,
        ActorY              = -34470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 142700,
        TriggerZ            = 0,
        TriggerY            = -34000,
        TriggerRange        = 1000,
        ActorX              = 142700,
        ActorZ              = 1000,
        ActorY              = -34000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AE",          # 00, 0
        "Function_1_31E",          # 01, 1
        "Function_2_394",          # 02, 2
        "Function_3_4BA",          # 03, 3
        "Function_4_5E0",          # 04, 4
        "Function_5_706",          # 05, 5
        "Function_6_804",          # 06, 6
        "Function_7_A9C",          # 07, 7
        "Function_8_DA2",          # 08, 8
        "Function_9_DD4",          # 09, 9
        "Function_10_E49",         # 0A, 10
        "Function_11_FCD",         # 0B, 11
        "Function_12_1103",        # 0C, 12
        "Function_13_11AE",        # 0D, 13
    )


    def Function_0_2AE(): pass

    label("Function_0_2AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_2F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31D")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (116, "loc_30A"),
        (SWITCH_DEFAULT, "loc_31D"),
    )


    label("loc_30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_31A")
    SetMapFlags(0x10000000)
    Event(0, 13)

    label("loc_31A")

    Jump("loc_31D")

    label("loc_31D")

    Return()

    # Function_0_2AE end

    def Function_1_31E(): pass

    label("Function_1_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341")
    OP_6F(0x1C, 0)
    Jump("loc_348")

    label("loc_341")

    OP_6F(0x1C, 60)

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A")
    OP_6F(0x1D, 0)
    Jump("loc_361")

    label("loc_35A")

    OP_6F(0x1D, 60)

    label("loc_361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_373")
    OP_6F(0x1E, 0)
    Jump("loc_37A")

    label("loc_373")

    OP_6F(0x1E, 60)

    label("loc_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C")
    OP_6F(0x1F, 0)
    Jump("loc_393")

    label("loc_38C")

    OP_6F(0x1F, 60)

    label("loc_393")

    Return()

    # Function_1_31E end

    def Function_2_394(): pass

    label("Function_2_394")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_479")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D9, 1)"), scpexpr(EXPR_END)), "loc_408")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xD9\x02\x07\x00。\x02",
    )

    Jump("loc_3ED")

    label("loc_3ED")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2998)
    Jump("loc_476")

    label("loc_408")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xD9\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xD9\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_457")

    label("loc_457")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1C, 60)
    OP_70(0x1C, 0x0)

    label("loc_476")

    Jump("loc_4AC")

    label("loc_479")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4AC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_394 end

    def Function_3_4BA(): pass

    label("Function_3_4BA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29C, 1)"), scpexpr(EXPR_END)), "loc_52E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x9C\x02\x07\x00。\x02",
    )

    Jump("loc_513")

    label("loc_513")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2999)
    Jump("loc_59C")

    label("loc_52E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x9C\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x9C\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_57D")

    label("loc_57D")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1D, 60)
    OP_70(0x1D, 0x0)

    label("loc_59C")

    Jump("loc_5D2")

    label("loc_59F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5D2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4BA end

    def Function_4_5E0(): pass

    label("Function_4_5E0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x18C, 1)"), scpexpr(EXPR_END)), "loc_654")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x8C\x01\x07\x00。\x02",
    )

    Jump("loc_639")

    label("loc_639")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x299A)
    Jump("loc_6C2")

    label("loc_654")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x8C\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x8C\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_6A3")

    label("loc_6A3")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1E, 60)
    OP_70(0x1E, 0x0)

    label("loc_6C2")

    Jump("loc_6F8")

    label("loc_6C5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6F8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5E0 end

    def Function_5_706(): pass

    label("Function_5_706")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1F, 0x1E)
    OP_73(0x1F)
    OP_6F(0x1F, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x1EC, 1)

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xEC\x01\x07\x00。\x02",
    )

    Jump("loc_75D")

    label("loc_75D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x28)"), scpexpr(EXPR_END)), "loc_777")
    Jump("loc_7C4")

    label("loc_777")

    CloseMessageWindow()

    AnonymousTalk(    #10
        "\x07\x00得到了\x1F\xEC\x01\x07\x00的食谱。\x02",
    )

    Jump("loc_79E")

    label("loc_79E")

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #11
        "\x1F\xEC\x01\x07\x00的制作方法已经记下了。\x02",
    )


    label("loc_7C4")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x299B)
    Jump("loc_7F2")

    label("loc_7D6")


    AnonymousTalk(    #12
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_7F2")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_706 end

    def Function_6_804(): pass

    label("Function_6_804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D3")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(2816)
    Sleep(500)
    Jump("loc_8D6")

    label("loc_8D3")

    TalkBegin(0xFF)

    label("loc_8D6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #13
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_900")

    label("loc_900")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_913")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A6B")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_965")

    label("loc_965")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_982"),
        (1, "loc_9FD"),
        (2, "loc_A2C"),
        (SWITCH_DEFAULT, "loc_A5B"),
    )


    label("loc_982")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xDD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A68")

    label("loc_9FD")

    OP_A9(0x1E)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #14
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_A29")

    label("loc_A29")

    Jump("loc_A68")

    label("loc_A2C")

    OP_A9(0x6)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #15
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_A58")

    label("loc_A58")

    Jump("loc_A68")

    label("loc_A5B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A68")

    label("loc_A68")

    Jump("loc_913")

    label("loc_A6B")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A98")
    OP_A2(0x258E)
    EventEnd(0x1)
    Jump("loc_A9B")

    label("loc_A98")

    TalkEnd(0xFF)

    label("loc_A9B")

    Return()

    # Function_6_804 end

    def Function_7_A9C(): pass

    label("Function_7_A9C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAC")
    Return()

    label("loc_AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB5")
    Return()

    label("loc_AB5")

    EventBegin(0x1)
    OP_8C(0x0, 174, 500)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #16
        "\x07\x05门牢牢地锁着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D17")
    OP_A2(0x0)

    NpcTalk(    #17
        0x18,
        "基尔巴特的声音",
        (
            "#5P#40W嘎吱嘎吱嘎吱嘎吱……\x01",
            "……呼……咔嚓咔嚓咔嚓咔嚓……\x02\x03",

            "谁会帮助……咕嘟咕嘟……\x01",
            "……那些家伙……嚼嚼嚼嚼………\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x18, 0x1, 0x0, 0x8)

    NpcTalk(    #18
        0x18,
        "基尔巴特的声音",
        (
            "#5P#60W咕咚！#500W\x01",
            "#40W呜呜呜呜呜呜呜呜～……#500W\x01",
            "#20W咚咚（←捶胸的声音）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #19
        0x18,
        "基尔巴特的声音",
        "#5P#4S噗哈——————！！\x02",
    )

    OP_7C(0x12C, 0x12C, 0xBB8, 0x12C)
    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #20
        0x18,
        "基尔巴特的声音",
        "#5P#40W……我、我还以为会死掉呢……\x02",
    )

    CloseMessageWindow()
    Sleep(800)

    NpcTalk(    #21
        0x18,
        "基尔巴特的声音",
        (
            "#5P#40W……哎……怎么回事？\x01",
            "……………从眼睛里面流出了汗………………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D86")

    label("loc_D17")


    NpcTalk(    #22
        0x18,
        "基尔巴特的声音",
        (
            "#5P#40W我……我才没有哭呢……\x02\x03",

            "咕咚……嚼嚼嚼嚼……\x01",
            "……呜呜……咔嚓咔嚓……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D86")

    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_7_A9C end

    def Function_8_DA2(): pass

    label("Function_8_DA2")

    OP_7C(0x12C, 0x12C, 0xBB8, 0x64)
    Sleep(800)
    OP_7C(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    OP_22(0x72, 0x0, 0x64)
    Return()

    # Function_8_DA2 end

    def Function_9_DD4(): pass

    label("Function_9_DD4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_E32")

    label("loc_E32")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Return()

    # Function_9_DD4 end

    def Function_10_E49(): pass

    label("Function_10_E49")

    TalkBegin(0xFF)
    OP_22(0x222, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x18, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E99")
    OP_28(0x18, 0x4, 0x2)
    OP_82(0x88, 0x2)
    PlayEffect(0x89, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_E99")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05头脑中有个声音在回旋——\x02",
    )

    CloseMessageWindow()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #25
        (
            "\x07\x0C\x18#2S#80W      来得正好……\x02\x03",

            "将自己的命运托付给骰子……\x01",
            "     是吉是凶……\x01",
            "     只有骰子知道。\x01",
            "    请出示『骰子』，\x02\x03",

            "  之后『门』便会打开……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x339, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC9")
    Sleep(500)
    OP_22(0x138, 0x0, 0x64)
    Sleep(2000)
    Call(0, 9)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC6")
    Call(0, 11)

    label("loc_FC6")

    Jump("loc_FC9")

    label("loc_FC9")

    TalkEnd(0xFF)
    Return()

    # Function_10_E49 end

    def Function_11_FCD(): pass

    label("Function_11_FCD")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x0, 115300, 0, 38890, 0)
    SetChrPos(0x1, 113750, 0, 38610, 0)
    SetChrPos(0x2, 115320, 0, 37500, 0)
    SetChrPos(0x3, 113600, 0, 37500, 0)
    OP_6D(114660, 0, 40150, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(3670, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1B, 0)
    OP_70(0x1B, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1B)
    Sleep(500)

    def lambda_10B6():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_10B6)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0xF, 0, 0x0)
    NewScene("ED6_DT21/P9002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_FCD end

    def Function_12_1103(): pass

    label("Function_12_1103")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -16250, -38000, 52300, 0)
    SetChrPos(0x1, -17950, -38000, 52240, 0)
    SetChrPos(0x2, -16580, -38000, 50060, 0)
    SetChrPos(0x3, -18080, -38000, 50420, 0)
    OP_6D(-17350, -38000, 53300, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(4630, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_12_1103 end

    def Function_13_11AE(): pass

    label("Function_13_11AE")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/U5111   ._SN", 115, 0, 0)
    IdleLoop()
    Return()

    # Function_13_11AE end

    SaveToFile()

Try(main)
