from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Function_4_443",          # 04, 4
        "Function_5_59A",          # 05, 5
        "Function_6_707",          # 06, 6
        "Function_7_BDC",          # 07, 7
        "Function_8_C74",          # 08, 8
        "Function_9_CDA",          # 09, 9
        "Function_10_EDD",         # 0A, 10
        "Function_11_1125",        # 0B, 11
        "Function_12_1177",        # 0C, 12
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

    OP_EA(0x2, 0xC4, 0x0, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C5")
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
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x20#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1568)
    Jump("loc_431")

    label("loc_3C5")


    AnonymousTalk(    #1
        (
            "\x07\x05Baby, come back, you can blame it all on me. ♪\x01",
            "I was wrong, and I just can't live without you... ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_431")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2CF end

    def Function_4_443(): pass

    label("Function_4_443")

    OP_EA(0x2, 0xC5, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_4B4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "Found \x1F\xF9\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x156A)
    Jump("loc_518")

    label("loc_4B4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "Found \x1F\xF9\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF9\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_518")

    Jump("loc_58C")

    label("loc_51B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05So...what really stops you from wearing more\x01",
            "than two accessories? Social decorum?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_58C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_443 end

    def Function_5_59A(): pass

    label("Function_5_59A")

    OP_EA(0x2, 0xC6, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_672")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xC4, 1)"), scpexpr(EXPR_END)), "loc_60B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "Found \x1F\xC4\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x156B)
    Jump("loc_66F")

    label("loc_60B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "Found \x1F\xC4\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xC4\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_66F")

    Jump("loc_6F9")

    label("loc_672")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05You open the chest, ponder putting the item you\x01",
            "took from it back, and close it again with a soft\x01",
            "smile.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6F9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_59A end

    def Function_6_707(): pass

    label("Function_6_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_713")
    Return()

    label("loc_713")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_733")
    Call(0, 7)
    Call(0, 8)
    FadeToBright(0, 0)

    label("loc_733")

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

    def lambda_7E1():
        OP_8E(0xFE, 0xFFFFFE5C, 0x0, 0xFFFF39CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E1)
    Sleep(300)

    def lambda_801():
        OP_8E(0xFE, 0x46, 0x0, 0xFFFF3486, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_801)
    Sleep(500)

    def lambda_821():
        OP_8E(0xFE, 0x23A, 0x0, 0xFFFF38AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_821)
    Sleep(400)

    def lambda_841():
        OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0xFFFF3DDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_841)
    WaitChrThread(0x101, 0x1)

    def lambda_861():
        OP_8C(0x101, 257, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_861)

    def lambda_86F():
        OP_6D(-755, 0, -50870, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_86F)
    WaitChrThread(0xF7, 0x1)

    def lambda_88C():
        OP_8C(0xF7, 257, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_88C)
    WaitChrThread(0x107, 0x1)

    def lambda_89F():
        OP_8C(0x107, 257, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_89F)
    WaitChrThread(0xF9, 0x1)

    def lambda_8B2():
        OP_8C(0xF9, 257, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_8B2)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #8
        0x107,
        (
            "#560FHey...the water isn't boiling here.\x02\x03",

            "#061FAhaha! It looks like just the right\x01",
            "temperature for a bath!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9B")

    ChrTalk(    #9
        0x104,
        (
            "#030F#6PSplendid! There is only one option\x01",
            "for us, my friends.\x02\x03",

            "#031FLet us doff our burdens and bare...\x01",
            "our souls to one another!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#1007F#4PYeah, you go right ahead with\x01",
            "'baring your soul,' Olivier.\x01",
            "We'll watch (in horror).\x02\x03",

            "#1006FIgnoring him, though, it really is a\x01",
            "great bit of hot water. Wouldn't hurt\x01",
            "to dip our feet in, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B64")

    label("loc_A9B")


    ChrTalk(    #11
        0x105,
        (
            "#542F#6PI must admit, after all our toils,\x01",
            "a bath would feel very...very nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1016F#4PYou got that right!\x02\x03",

            "#1006FThe water does look really good.\x01",
            "Wouldn't hurt to dip our feet in, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_BA9")

    ChrTalk(    #13
        0x106,
        (
            "#552FTch... Fine. Go ahead.\x01",
            "Just don't take too long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD6")

    label("loc_BA9")


    ChrTalk(    #14
        0x103,
        "#021FAll right! A footbath it is, then.\x02",
    )

    CloseMessageWindow()

    label("loc_BD6")

    OP_A2(0x1424)
    EventEnd(0x0)
    Return()

    # Function_6_707 end

    def Function_7_BDC(): pass

    label("Function_7_BDC")

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
        (0, "loc_C55"),
        (1, "loc_C5B"),
        (SWITCH_DEFAULT, "loc_C61"),
    )


    label("loc_C55")

    OP_A2(0x1200)
    Jump("loc_C61")

    label("loc_C5B")

    OP_A2(0x1201)
    Jump("loc_C61")

    label("loc_C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C6F")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_C73")

    label("loc_C6F")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_C73")

    Return()

    # Function_7_BDC end

    def Function_8_C74(): pass

    label("Function_8_C74")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_CAE")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_CC8")

    label("loc_CAE")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_CC8")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_8_C74 end

    def Function_9_CDA(): pass

    label("Function_9_CDA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #15
        "\x07\x05The water is at the perfect temperature.\x02",
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
            "Enjoy a Footbath\x01",      # 0
            "Don't\x01",                 # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D72"),
        (1, "loc_ED3"),
        (SWITCH_DEFAULT, "loc_ED6"),
    )


    label("loc_D72")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E31")
    OP_31(0x0, 0xFB, 0x0)

    label("loc_E31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E44")
    OP_31(0x1, 0xFB, 0x0)

    label("loc_E44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E57")
    OP_31(0x2, 0xFB, 0x0)

    label("loc_E57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E6A")
    OP_31(0x3, 0xFB, 0x0)

    label("loc_E6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E7D")
    OP_31(0x5, 0xFB, 0x0)

    label("loc_E7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E90")
    OP_31(0x4, 0xFB, 0x0)

    label("loc_E90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA3")
    OP_31(0x6, 0xFB, 0x0)

    label("loc_EA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB6")
    OP_31(0x7, 0xFB, 0x0)

    label("loc_EB6")

    OP_8C(0x0, 90, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_ED9")

    label("loc_ED3")

    Jump("loc_ED9")

    label("loc_ED6")

    Jump("loc_ED9")

    label("loc_ED9")

    TalkEnd(0xFF)
    Return()

    # Function_9_CDA end

    def Function_10_EDD(): pass

    label("Function_10_EDD")

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

    # Function_10_EDD end

    def Function_11_1125(): pass

    label("Function_11_1125")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1146"),
        (1, "loc_114E"),
        (2, "loc_1156"),
        (3, "loc_115E"),
        (4, "loc_1166"),
        (SWITCH_DEFAULT, "loc_116E"),
    )


    label("loc_1146")

    Sleep(500)
    Jump("loc_1176")

    label("loc_114E")

    Sleep(1000)
    Jump("loc_1176")

    label("loc_1156")

    Sleep(1500)
    Jump("loc_1176")

    label("loc_115E")

    Sleep(2000)
    Jump("loc_1176")

    label("loc_1166")

    Sleep(2500)
    Jump("loc_1176")

    label("loc_116E")

    Sleep(3000)
    Jump("loc_1176")

    label("loc_1176")

    Return()

    # Function_11_1125 end

    def Function_12_1177(): pass

    label("Function_12_1177")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_118D")
    OP_22(0x10D, 0x0, 0x64)
    Sleep(7000)
    Jump("Function_12_1177")

    label("loc_118D")

    Return()

    # Function_12_1177 end

    SaveToFile()

Try(main)
