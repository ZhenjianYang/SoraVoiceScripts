from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U5111   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U5111.x',
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
        X                   = 112940,
        Z                   = 0,
        Y                   = -3200,
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
        Unknown_1C          = 8,
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
        TalkFunctionIndex   = 7,
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
        "Function_1_314",          # 01, 1
        "Function_2_38A",          # 02, 2
        "Function_3_4B0",          # 03, 3
        "Function_4_5D6",          # 04, 4
        "Function_5_6FC",          # 05, 5
        "Function_6_7FA",          # 06, 6
        "Function_7_D18",          # 07, 7
        "Function_8_FB0",          # 08, 8
        "Function_9_1282",         # 09, 9
    )


    def Function_0_2AE(): pass

    label("Function_0_2AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CF")
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_2CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_313")
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

    label("loc_313")

    Return()

    # Function_0_2AE end

    def Function_1_314(): pass

    label("Function_1_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_325")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_337")
    OP_6F(0x1D, 0)
    Jump("loc_33E")

    label("loc_337")

    OP_6F(0x1D, 60)

    label("loc_33E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350")
    OP_6F(0x1E, 0)
    Jump("loc_357")

    label("loc_350")

    OP_6F(0x1E, 60)

    label("loc_357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_369")
    OP_6F(0x1F, 0)
    Jump("loc_370")

    label("loc_369")

    OP_6F(0x1F, 60)

    label("loc_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_382")
    OP_6F(0x20, 0)
    Jump("loc_389")

    label("loc_382")

    OP_6F(0x20, 60)

    label("loc_389")

    Return()

    # Function_1_314 end

    def Function_2_38A(): pass

    label("Function_2_38A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D9, 1)"), scpexpr(EXPR_END)), "loc_3FE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xD9\x02\x07\x00。\x02",
    )

    Jump("loc_3E3")

    label("loc_3E3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2998)
    Jump("loc_46C")

    label("loc_3FE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xD9\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xD9\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_44D")

    label("loc_44D")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1D, 60)
    OP_70(0x1D, 0x0)

    label("loc_46C")

    Jump("loc_4A2")

    label("loc_46F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4A2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_38A end

    def Function_3_4B0(): pass

    label("Function_3_4B0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_595")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29C, 1)"), scpexpr(EXPR_END)), "loc_524")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x9C\x02\x07\x00。\x02",
    )

    Jump("loc_509")

    label("loc_509")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2999)
    Jump("loc_592")

    label("loc_524")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x9C\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x9C\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_573")

    label("loc_573")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1E, 60)
    OP_70(0x1E, 0x0)

    label("loc_592")

    Jump("loc_5C8")

    label("loc_595")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5C8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4B0 end

    def Function_4_5D6(): pass

    label("Function_4_5D6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x18C, 1)"), scpexpr(EXPR_END)), "loc_64A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x8C\x01\x07\x00。\x02",
    )

    Jump("loc_62F")

    label("loc_62F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x299A)
    Jump("loc_6B8")

    label("loc_64A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x8C\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x8C\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_699")

    label("loc_699")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1F, 60)
    OP_70(0x1F, 0x0)

    label("loc_6B8")

    Jump("loc_6EE")

    label("loc_6BB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6EE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5D6 end

    def Function_5_6FC(): pass

    label("Function_5_6FC")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x20, 0x1E)
    OP_73(0x20)
    OP_6F(0x20, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x1EC, 1)

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xEC\x01\x07\x00。\x02",
    )

    Jump("loc_753")

    label("loc_753")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x28)"), scpexpr(EXPR_END)), "loc_76D")
    Jump("loc_7BA")

    label("loc_76D")

    CloseMessageWindow()

    AnonymousTalk(    #10
        "\x07\x00得到了\x1F\xEC\x01\x07\x00的食谱。\x02",
    )

    Jump("loc_794")

    label("loc_794")

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #11
        "\x1F\xEC\x01\x07\x00的制作方法已经记下了。\x02",
    )


    label("loc_7BA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x299B)
    Jump("loc_7E8")

    label("loc_7CC")


    AnonymousTalk(    #12
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_7E8")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6FC end

    def Function_6_7FA(): pass

    label("Function_6_7FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 21630, 0, 12910, 180)
    SetChrPos(0x102, 20700, 0, 13000, 180)
    SetChrPos(0xF0, 20520, 0, 14070, 180)
    SetChrPos(0xF1, 21540, 0, 13940, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(22000, 0, 14800, 0)
    OP_67(0, 6660, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_8B9():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_8B9)
    FadeToBright(2000, 0)
    Sleep(1000)
    LoadEffect(0x0, "map\\mp252_04.eff")
    PlayEffect(0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(2000)

    def lambda_9CD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9CD)

    def lambda_9DF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_9DF)

    def lambda_9F1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_9F1)

    def lambda_A03():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A03)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    OP_83(0x0, 0x2)
    OP_83(0x1, 0x2)
    OP_83(0x2, 0x2)
    OP_83(0x3, 0x2)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A94")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AFB")

    label("loc_A94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABC")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AFB")

    label("loc_ABC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE4")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AFB")

    label("loc_AE4")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_AFB")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B28")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B8F")

    label("loc_B28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B50")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B8F")

    label("loc_B50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B78")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B8F")

    label("loc_B78")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B8F")

    Sleep(1200)

    def lambda_B9A():
        OP_6D(24480, 0, 14710, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B9A)

    def lambda_BB2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BB2)
    Sleep(100)

    def lambda_BC5():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BC5)
    Sleep(100)

    def lambda_BD8():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_BD8)
    Sleep(100)

    def lambda_BEB():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_BEB)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #13
        0x109,
        "#1079F#6P这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#1504F#6P照明什么时候……\x02\x03",

            "#1503F而且……\x01",
            "窗户外面变暗了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x109,
        (
            "#1065F#6P啊啊……\x01",
            "看来和之前的王都一样，\x01",
            "变成了夜晚呢。\x02\x03",

            "#1063F也许附近会有什么变化……\x01",
            "我们仔细找一找吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#1502F#6P知道了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x290F)
    OP_28(0x34, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_6_7FA end

    def Function_7_D18(): pass

    label("Function_7_D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE7")
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
    Jump("loc_DEA")

    label("loc_DE7")

    TalkBegin(0xFF)

    label("loc_DEA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #17
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_E14")

    label("loc_E14")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F7F")

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

    Jump("loc_E79")

    label("loc_E79")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E96"),
        (1, "loc_F11"),
        (2, "loc_F40"),
        (SWITCH_DEFAULT, "loc_F6F"),
    )


    label("loc_E96")

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
    Jump("loc_F7C")

    label("loc_F11")

    OP_A9(0x1E)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #18
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_F3D")

    label("loc_F3D")

    Jump("loc_F7C")

    label("loc_F40")

    OP_A9(0x6)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_F6C")

    label("loc_F6C")

    Jump("loc_F7C")

    label("loc_F6F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F7C")

    label("loc_F7C")

    Jump("loc_E27")

    label("loc_F7F")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAC")
    OP_A2(0x258E)
    EventEnd(0x1)
    Jump("loc_FAF")

    label("loc_FAC")

    TalkEnd(0xFF)

    label("loc_FAF")

    Return()

    # Function_7_D18 end

    def Function_8_FB0(): pass

    label("Function_8_FB0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FC0")
    Return()

    label("loc_FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC9")
    Return()

    label("loc_FC9")

    EventBegin(0x1)
    OP_8C(0x0, 174, 500)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F7")
    OP_A2(0x0)

    NpcTalk(    #20
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
    OP_43(0x18, 0x1, 0x0, 0x9)

    NpcTalk(    #21
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

    NpcTalk(    #22
        0x18,
        "基尔巴特的声音",
        "#5P#4S噗哈——————！！\x02",
    )

    OP_7C(0x12C, 0x12C, 0xBB8, 0x12C)
    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #23
        0x18,
        "基尔巴特的声音",
        "#5P#40W……我、我还以为会死掉呢……\x02",
    )

    CloseMessageWindow()
    Sleep(800)

    NpcTalk(    #24
        0x18,
        "基尔巴特的声音",
        (
            "#5P#40W……哎……怎么回事？\x01",
            "……………从眼睛里面流出了汗………………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1266")

    label("loc_11F7")


    NpcTalk(    #25
        0x18,
        "基尔巴特的声音",
        (
            "#5P#40W我……我才没有哭呢……\x02\x03",

            "咕咚……嚼嚼嚼嚼……\x01",
            "……呜呜……咔嚓咔嚓……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1266")

    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_8_FB0 end

    def Function_9_1282(): pass

    label("Function_9_1282")

    OP_7C(0x12C, 0x12C, 0xBB8, 0x64)
    Sleep(800)
    OP_7C(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    OP_22(0x72, 0x0, 0x64)
    Return()

    # Function_9_1282 end

    SaveToFile()

Try(main)
