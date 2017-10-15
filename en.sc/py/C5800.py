from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Residential Block - Cradle II',        # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
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
        "Function_3_39D",          # 03, 3
        "Function_4_49B",          # 04, 4
        "Function_5_50F",          # 05, 5
        "Function_6_E0E",          # 06, 6
        "Function_7_E57",          # 07, 7
        "Function_8_EA7",          # 08, 8
        "Function_9_EF7",          # 09, 9
        "Function_10_F47",         # 0A, 10
        "Function_11_FCD",         # 0B, 11
        "Function_12_105E",        # 0C, 12
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

    OP_EA(0x2, 0xB2, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_349")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_2E2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x00\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x230B)
    Jump("loc_346")

    label("loc_2E2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x00\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x00\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_346")

    Jump("loc_38F")

    label("loc_349")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Nooo! Give it back! That was my spleen!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_38F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_271 end

    def Function_3_39D(): pass

    label("Function_3_39D")

    OP_EA(0x2, 0xB3, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44B")
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
            "Found\x01",
            "#2C#57IWater Sepith x100\x01",
            "#59IWind Sepith x100\x01",
            "#60ISpace Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x230C)
    Jump("loc_489")

    label("loc_44B")


    AnonymousTalk(    #4
        (
            "\x07\x05GET A SILK BAG FROM THE GRAVEYARD DUCK TO LOOT\x01",
            "LONGER.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_489")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_39D end

    def Function_4_49B(): pass

    label("Function_4_49B")

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

    # Function_4_49B end

    def Function_5_50F(): pass

    label("Function_5_50F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_526")
    Call(0, 10)
    Call(0, 11)

    label("loc_526")

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

    def lambda_5B6():
        OP_6D(-151420, -8000, -108390, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5B6)
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
        "#1025F#6PPhew! Finally.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #6
        0x102,
        "#1044F#2PThis...\x02",
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

    def lambda_6A0():
        OP_6D(-158900, -4000, -56630, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A0)

    def lambda_6B8():
        OP_67(0, 6100, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6B8)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D8")

    ChrTalk(    #7
        0x104,
        (
            "#035FOh. What a lovely city.\x02\x03",

            "#030FI would guess this is where the\x01",
            "ancients actually dwelled.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1B")

    label("loc_7D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84C")

    ChrTalk(    #8
        0x105,
        (
            "#1382FIt's so beautiful...\x02\x03",

            "This must be where the majority\x01",
            "of the island's population lived.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1B")

    label("loc_84C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C2")

    ChrTalk(    #9
        0x103,
        (
            "#020FAnother breathtaking view.\x02\x03",

            "I suppose this is where most of\x01",
            "the citizenry must have lived.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1B")

    label("loc_8C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_93D")

    ChrTalk(    #10
        0x109,
        (
            "#1060FThe views just keep comin'!\x02\x03",

            "Guess this is where most of the\x01",
            "folks around here actually lived.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1B")

    label("loc_93D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A4")

    ChrTalk(    #11
        0x108,
        (
            "#070FA beautiful city.\x02\x03",

            "These would be the proper homes\x01",
            "of the island residents.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1B")

    label("loc_9A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A1B")

    ChrTalk(    #12
        0x107,
        (
            "#064FIt's so pretty!\x02\x03",

            "#061FI guess this is where all the people\x01",
            "who lived here actually, um, lived!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7A")

    ChrTalk(    #13
        0x106,
        (
            "#051FIt does seem more like a livin' space\x01",
            "compared to where we crashed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C56")

    label("loc_A7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AE2")

    ChrTalk(    #14
        0x107,
        (
            "#560FYeah! This does look more like homes\x01",
            "and stuff compared to where we crashed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C56")

    label("loc_AE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B46")

    ChrTalk(    #15
        0x108,
        (
            "#070FThis does look more like a residential\x01",
            "area, compared to our crash site.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C56")

    label("loc_B46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA2")

    ChrTalk(    #16
        0x109,
        (
            "#1060FDoes sorta look like a livin'\x01",
            "space compared to the crash site.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C56")

    label("loc_BA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF3")

    ChrTalk(    #17
        0x103,
        (
            "#027FIt does feel a bit 'homier' than\x01",
            "our crash site, yes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C56")

    label("loc_BF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C56")

    ChrTalk(    #18
        0x105,
        (
            "#1382FYes, it does seem like more of a residential\x01",
            "area than our crash site is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C56")


    ChrTalk(    #19
        0x101,
        (
            "#1006F#6PYeah, it's kind of nice and...homey,\x01",
            "here, I guess.\x02\x03",

            "#1015FBut, you know. This just bothers me even more.\x01",
            "WHY did the residents abandon such a nice city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#1035F#2PThis seems like a good place to\x01",
            "find an answer to that question.\x02\x03",

            "#1040FWe need to find a new route, anyway,\x01",
            "so shall we investigate?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D98():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D98)
    Sleep(50)

    def lambda_DAB():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_DAB)
    Sleep(50)

    def lambda_DBE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_DBE)
    WaitChrThread(0x101, 0x1)
    Sleep(300)

    ChrTalk(    #21
        0x101,
        "#1006F#6PYeah, okay.\x02",
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

    # Function_5_50F end

    def Function_6_E0E(): pass

    label("Function_6_E0E")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -151160, -7920, -102500, 180)
    OP_8E(0xFE, 0xFFFDB246, 0xFFFFE0C0, 0xFFFE6236, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFDAF94, 0xFFFFE0C0, 0xFFFE5354, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_E0E end

    def Function_7_E57(): pass

    label("Function_7_E57")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -151160, -7920, -102500, 180)
    OP_8E(0xFE, 0xFFFDB246, 0xFFFFE0C0, 0xFFFE6236, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFDB624, 0xFFFFE0C0, 0xFFFE5336, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_7_E57 end

    def Function_8_EA7(): pass

    label("Function_8_EA7")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -151160, -7920, -102500, 180)
    OP_8E(0xFE, 0xFFFDB246, 0xFFFFE0C0, 0xFFFE6236, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFDAEB8, 0xFFFFE0C0, 0xFFFE5962, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_EA7 end

    def Function_9_EF7(): pass

    label("Function_9_EF7")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -151160, -7920, -102500, 180)
    OP_8E(0xFE, 0xFFFDB246, 0xFFFFE0C0, 0xFFFE6236, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFDB552, 0xFFFFE0C0, 0xFFFE5980, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_EF7 end

    def Function_10_F47(): pass

    label("Function_10_F47")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_FC0"),
        (1, "loc_FC6"),
        (SWITCH_DEFAULT, "loc_FCC"),
    )


    label("loc_FC0")

    OP_A2(0x1200)
    Jump("loc_FCC")

    label("loc_FC6")

    OP_A2(0x1201)
    Jump("loc_FCC")

    label("loc_FCC")

    Return()

    # Function_10_F47 end

    def Function_11_FCD(): pass

    label("Function_11_FCD")

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

    # Function_11_FCD end

    def Function_12_105E(): pass

    label("Function_12_105E")

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

    # Function_12_105E end

    SaveToFile()

Try(main)
