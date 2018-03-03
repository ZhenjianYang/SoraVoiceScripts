from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5503   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5503.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60233",
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
        'Anelace',                              # 9
        'Werewolf',                             # 10
        'Werewolf',                             # 11
        'Sealing Stone 9',                      # 12
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
        'ED6_DT07/CH00420 ._CH',             # 00
        'ED6_DT07/CH00421 ._CH',             # 01
        'ED6_DT29/CH15070 ._CH',             # 02
        'ED6_DT29/CH15071 ._CH',             # 03
        'ED6_DT26/CH20621 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH00420P._CP',             # 00
        'ED6_DT07/CH00421P._CP',             # 01
        'ED6_DT29/CH15070P._CP',             # 02
        'ED6_DT29/CH15071P._CP',             # 03
        'ED6_DT26/CH20621P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -1750,
        Y                   = -1000,
        Z                   = 199430,
        Range               = 3280,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x31ECA,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = -14010,
        TriggerZ            = 0,
        TriggerY            = 202210,
        TriggerRange        = 1000,
        ActorX              = -14010,
        ActorZ              = 2000,
        ActorY              = 202210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 30500,
        TriggerZ            = 0,
        TriggerY            = 202010,
        TriggerRange        = 1000,
        ActorX              = 30500,
        ActorZ              = 1000,
        ActorY              = 202010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BA",          # 00, 0
        "Function_1_1CB",          # 01, 1
        "Function_2_205",          # 02, 2
        "Function_3_335",          # 03, 3
        "Function_4_FB0",          # 04, 4
        "Function_5_FDE",          # 05, 5
        "Function_6_1011",         # 06, 6
        "Function_7_1044",         # 07, 7
        "Function_8_1077",         # 08, 8
        "Function_9_1098",         # 09, 9
        "Function_10_10A9",        # 0A, 10
        "Function_11_178C",        # 0B, 11
        "Function_12_1C60",        # 0C, 12
        "Function_13_1C84",        # 0D, 13
        "Function_14_1CA8",        # 0E, 14
        "Function_15_1CCC",        # 0F, 15
        "Function_16_1CF0",        # 10, 16
        "Function_17_1D45",        # 11, 17
        "Function_18_1DAD",        # 12, 18
        "Function_19_1E15",        # 13, 19
        "Function_20_209C",        # 14, 20
        "Function_21_20EB",        # 15, 21
    )


    def Function_0_1BA(): pass

    label("Function_0_1BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CA")
    Event(0, 3)

    label("loc_1CA")

    Return()

    # Function_0_1BA end

    def Function_1_1CB(): pass

    label("Function_1_1CB")

    OP_1B(0x0, 0x0, 0x15)
    OP_22(0x85, 0x1, 0x4B)
    SetMapFlags(0x100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB")
    OP_82(0xA9, 0x0)
    OP_82(0xAA, 0x0)
    OP_82(0xAC, 0x0)

    label("loc_1EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x532, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FD")
    OP_6F(0x2, 0)
    Jump("loc_204")

    label("loc_1FD")

    OP_6F(0x2, 60)

    label("loc_204")

    Return()

    # Function_1_1CB end

    def Function_2_205(): pass

    label("Function_2_205")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x532, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x18A, 1)"), scpexpr(EXPR_END)), "loc_273")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x8A\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2994)
    Jump("loc_2DB")

    label("loc_273")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x8A\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x8A\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_2DB")

    Jump("loc_327")

    label("loc_2DE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05I see you enjoy finding empty spaces.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x77, 0x0)

    label("loc_327")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_205 end

    def Function_3_335(): pass

    label("Function_3_335")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    OP_22(0x85, 0x1, 0x46)
    OP_43(0x10, 0x0, 0x0, 0x8)
    SetChrPos(0x109, 8910, 4000, 5150, 270)
    SetChrPos(0x102, 9200, 4000, 6540, 270)
    SetChrPos(0xF0, 8910, 4000, 5150, 270)
    SetChrPos(0xF1, 9200, 4000, 6540, 270)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(2000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #3
        (
            "\x07\x00#1063FIt sure is dark here...\x02\x03",

            "#1065FStill, I guess you can't expect much in\x01",
            "the way of light from a staircase leading\x01",
            "to an underground waterway.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 100, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #4
        (
            "\x07\x00#1500FFrom what I've heard, this used to be an old ruin\x01",
            "until the Bracer Guild repurposed it as a training\x01",
            "area.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AF")
    SetMessageWindowPos(300, 150, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #5
        (
            "\x07\x00#065FTh-That doesn't explain why it's so hot, though.\x02\x03",

            "I would've thought an underground waterway\x01",
            "would be cool...but it's boiling down here.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_98E")

    label("loc_5AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68D")
    SetMessageWindowPos(300, 150, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #6
        (
            "\x07\x00#1544FYou might not be able to expect much light,\x01",
            "but I would've preferred it to be a little cooler\x01",
            "than this...\x02\x03",

            "#1547FMy ever-so fashionable attire is getting covered \x01",
            "in sweat.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_98E")

    label("loc_68D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74B")
    SetMessageWindowPos(300, 150, -1, -1)
    SetChrName("Josette")

    AnonymousTalk(    #7
        (
            "\x07\x00#413FWhy the heck is it so hot here, though?\x02\x03",

            "#210FYou'd think an underground waterway would\x01",
            "be nice and cool, but it's like stepping into an\x01",
            "oven.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_98E")

    label("loc_74B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_810")
    SetMessageWindowPos(300, 150, -1, -1)
    SetChrName("Kloe")

    AnonymousTalk(    #8
        (
            "\x07\x00#1165FIs it just me or is it a little hot, though?\x02\x03",

            "#1382FI would have thought a passage leading to an\x01",
            "underground waterway would be much cooler\x01",
            "than this...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_98E")

    label("loc_810")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C3")
    SetMessageWindowPos(300, 150, -1, -1)
    SetChrName("Julia")

    AnonymousTalk(    #9
        (
            "\x07\x00#175FStill, it's rather hot down here, isn't it?\x02\x03",

            "I would've expected a passage like this to be\x01",
            "cooler than the surface above, not hotter.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_98E")

    label("loc_8C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_98E")
    SetMessageWindowPos(300, 150, -1, -1)
    SetChrName("Mueller")

    AnonymousTalk(    #10
        (
            "\x07\x00#276FI would have expected it to be a lot cooler\x01",
            "than this passage is, though.\x02\x03",

            "If anything, it feels warmer here than it did\x01",
            "on the surface. Significantly warmer.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_98E")

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #11
        (
            "\x07\x00#1067FIt IS pretty damn hot...\x02\x03",

            "That weird rumbling sound I can hear's\x01",
            "been bugging me for a while, too...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 100, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #12
        (
            "\x07\x00#1502FActually, I think we're almost at the end,\x01",
            "so maybe it'll cool down in a second.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_6D(3970, 1750, 6640, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_22(0x85, 0x1, 0x4B)
    OP_A2(0x0)
    OP_44(0x10, 0x0)

    def lambda_AD7():
        OP_6D(1500, 0, 7020, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AD7)

    def lambda_AEF():
        OP_67(0, 6420, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_AEF)

    def lambda_B07():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B07)

    def lambda_B17():
        OP_6E(280, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_B17)
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0x4)
    OP_43(0x102, 0x0, 0x0, 0x5)
    OP_43(0xF0, 0x0, 0x0, 0x6)
    OP_43(0xF1, 0x0, 0x0, 0x7)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA7")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C0E")

    label("loc_BA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCF")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C0E")

    label("loc_BCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF7")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C0E")

    label("loc_BF7")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_C0E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3B")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CA2")

    label("loc_C3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C63")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CA2")

    label("loc_C63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CA2")

    label("loc_C8B")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CA2")

    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x2)

    ChrTalk(    #13
        0x102,
        "#1502F#5PWhat in the world...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D27")

    ChrTalk(    #14
        0x108,
        "#075F#5PWell, it's no wonder we were feeling hot.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E8C")

    label("loc_D27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D73")

    ChrTalk(    #15
        0x10D,
        "#272F#5PHmph. Well, this certainly explains the heat.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E8C")

    label("loc_D73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DBC")

    ChrTalk(    #16
        0x10E,
        "#176F#5PWell...it's no wonder we were feeling hot.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E8C")

    label("loc_DBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DFF")

    ChrTalk(    #17
        0x105,
        "#1163F#5PThis certainly explains the heat...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E8C")

    label("loc_DFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E48")

    ChrTalk(    #18
        0x10B,
        "#216F#5PWell, this sure explains why it feels hot.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E8C")

    label("loc_E48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E8C")

    ChrTalk(    #19
        0x104,
        "#1544F#5PWell, this certainly explains the heat.\x02",
    )

    CloseMessageWindow()

    label("loc_E8C")


    ChrTalk(    #20
        0x109,
        (
            "#1075F#5PCall me an optimist, but I doubt this is how\x01",
            "this place normally is.\x02\x03",

            "#1840FLet's write this one off as our enemies' work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#1505F#5PI think that's a safe assumption to make.\x02\x03",

            "#1502FWhich means we're really going to need\x01",
            "to proceed cautiously.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2903)
    OP_28(0x32, 0x1, 0x100)
    OP_28(0x32, 0x1, 0x200)
    OP_1D(0xE9)
    Sleep(500)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_3_335 end

    def Function_4_FB0(): pass

    label("Function_4_FB0")


    def lambda_FB6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB6)
    OP_8E(0xFE, 0xFFFFFE3E, 0x0, 0x14BE, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_FB0 end

    def Function_5_FDE(): pass

    label("Function_5_FDE")

    Sleep(300)

    def lambda_FE9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FE9)
    OP_8E(0xFE, 0xFFFFFD94, 0x0, 0x19FA, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_5_FDE end

    def Function_6_1011(): pass

    label("Function_6_1011")

    Sleep(600)

    def lambda_101C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_101C)
    OP_8E(0xFE, 0x366, 0x0, 0x148C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_1011 end

    def Function_7_1044(): pass

    label("Function_7_1044")

    Sleep(800)

    def lambda_104F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_104F)
    OP_8E(0xFE, 0x3FC, 0x0, 0x1A9A, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_7_1044 end

    def Function_8_1077(): pass

    label("Function_8_1077")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1097")
    OP_22(0x1B, 0x0, 0x64)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1094")
    Jump("loc_1097")

    label("loc_1094")

    Jump("Function_8_1077")

    label("loc_1097")

    Return()

    # Function_8_1077 end

    def Function_9_1098(): pass

    label("Function_9_1098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 4)), scpexpr(EXPR_END)), "loc_10A0")
    Return()

    label("loc_10A0")

    Call(0, 10)
    Call(0, 11)
    Return()

    # Function_9_1098 end

    def Function_10_10A9(): pass

    label("Function_10_10A9")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    OP_E0(238, 0x45, 0x2)
    OP_E0(238, 0x46, 0x3)
    OP_E0(239, 0x47, 0x2)
    OP_E0(239, 0x48, 0x3)
    OP_E0(240, 0x49, 0x2)
    OP_E0(240, 0x4A, 0x3)
    OP_E0(241, 0x4B, 0x2)
    OP_E0(241, 0x4C, 0x3)
    OP_20(0x7D0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1154")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_11BB")

    label("loc_1154")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_11BB")

    label("loc_117C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A4")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_11BB")

    label("loc_11A4")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_11BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E3")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_124A")

    label("loc_11E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_124A")

    label("loc_120B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1233")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_124A")

    label("loc_1233")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_124A")

    Sleep(1000)

    def lambda_1255():
        OP_6D(11980, 0, 202530, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1255)

    def lambda_126D():
        OP_67(0, 7500, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_126D)

    def lambda_1285():
        OP_6B(2170, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_1285)

    def lambda_1295():
        OP_6E(324, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_1295)

    def lambda_12A5():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_12A5)

    def lambda_12B3():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_12B3)

    def lambda_12C1():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_12C1)

    def lambda_12CF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_12CF)
    WaitChrThread(0xEE, 0x2)
    SetChrPos(0xEE, -4000, 0, 201070, 90)
    SetChrPos(0xEF, -4740, 0, 202500, 90)
    SetChrPos(0xF0, -5880, 0, 201050, 90)
    SetChrPos(0xF1, -6500, 0, 202550, 90)
    Sleep(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 11420, 100, 201870, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 14000, 0, 203770, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, 14000, 0, 199870, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    def lambda_13E8():
        OP_6B(1900, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13E8)
    OP_22(0x85, 0x1, 0x64)

    def lambda_13FD():

        label("loc_13FD")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_13FD")

    QueueWorkItem2(0x109, 0, lambda_13FD)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 11420, -3100, 201870, 270)
    SetChrSubChip(0x10, 0)
    OP_43(0x10, 0x0, 0x0, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 14000, -3100, 203770, 270)
    OP_43(0x11, 0x0, 0x0, 0x11)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 14000, -3100, 199870, 270)
    OP_43(0x12, 0x0, 0x0, 0x12)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    OP_44(0x109, 0x0)
    OP_22(0x85, 0x1, 0x4B)
    OP_1D(0xC4)
    WaitChrThread(0x109, 0x1)
    Sleep(1000)

    ChrTalk(    #22
        0x102,
        "#1504F#2PAnelace?!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_14B5():
        OP_6D(8540, 0, 203300, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14B5)

    def lambda_14CD():
        OP_67(0, 6160, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_14CD)

    def lambda_14E5():
        OP_6B(2050, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_14E5)

    def lambda_14F5():
        OP_6E(412, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14F5)
    OP_43(0x109, 0x0, 0x0, 0xC)
    OP_43(0x102, 0x0, 0x0, 0xD)
    OP_43(0xF0, 0x0, 0x0, 0xE)
    OP_43(0xF1, 0x0, 0x0, 0xF)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #23
        0x10,
        "#1313F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1063F#6PIt's another grimoire. Not the real thing.\x02\x03",

            "It's like she's completely lifeless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#1505F#6PWell, at least that means we don't need\x01",
            "to hold back to avoid hurting her.\x02\x03",

            "#1506FLet's do this!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_162E():
        OP_6D(8840, 0, 202800, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_162E)

    def lambda_1646():
        OP_67(0, 6580, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1646)

    def lambda_165E():
        OP_6B(1700, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_165E)

    def lambda_166E():
        OP_6E(360, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_166E)
    SetChrChipByIndex(0x10, 1)

    def lambda_1683():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1683)

    def lambda_169E():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_169E)
    Sleep(10)

    def lambda_16BE():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_16BE)
    SetChrChipByIndex(0x11, 3)

    def lambda_16DE():

        label("loc_16DE")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_16DE")

    QueueWorkItem2(0x11, 3, lambda_16DE)

    def lambda_16F1():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFE0C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_16F1)
    Sleep(10)

    def lambda_1711():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1711)
    SetChrChipByIndex(0x12, 3)

    def lambda_1731():

        label("loc_1731")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_1731")

    QueueWorkItem2(0x12, 3, lambda_1731)

    def lambda_1744():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x1F4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1744)
    Sleep(10)

    def lambda_1764():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1764)
    WaitChrThread(0x109, 0x1)
    Battle(0x1A3, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_10_10A9 end

    def Function_11_178C(): pass

    label("Function_11_178C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x109, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    OP_E0(238, 0x45, 0x2)
    OP_E0(238, 0x46, 0x3)
    OP_E0(239, 0x47, 0x2)
    OP_E0(239, 0x48, 0x3)
    OP_E0(240, 0x49, 0x2)
    OP_E0(240, 0x4A, 0x3)
    OP_E0(241, 0x4B, 0x2)
    OP_E0(241, 0x4C, 0x3)
    SetChrPos(0xEE, 6670, 0, 201380, 90)
    SetChrPos(0xEF, 6570, 0, 203010, 90)
    SetChrPos(0xF0, 4810, 0, 201060, 90)
    SetChrPos(0xF1, 4760, 0, 202870, 90)
    SetChrChipByIndex(0xEE, 5)
    SetChrSubChip(0xEE, 0)
    SetChrChipByIndex(0xEF, 7)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 9)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 11)
    SetChrSubChip(0xF1, 0)
    OP_6D(8790, 0, 202960, 0)
    OP_67(0, 6310, -10000, 0)
    OP_6B(2120, 0)
    OP_6C(45000, 0)
    OP_6E(389, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, 10500, 1200, 201870, 0)
    PlayEffect(0x7, 0x7, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)

    def lambda_19C9():
        OP_6D(10000, 0, 203500, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_19C9)

    def lambda_19E1():
        OP_67(0, 6140, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_19E1)
    OP_8E(0x109, 0x251C, 0x0, 0x31498, 0x7D0, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 4)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x13, 0x2710, 0x4B0, 0x313E4, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x13, 0x80)
    OP_0D()
    Sleep(150)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05Received \x1F\x5A\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x35A, 1)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #27
        0x102,
        "#1513F#6PWhew... That wraps that up.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #28
        0x109,
        (
            "#1075F#11PSure does. Probably no prize for guessing\x01",
            "who's in this sealing stone, either.\x02\x03",

            "#1840FLet's head back to base and let her out.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2904)
    OP_28(0x32, 0x1, 0x400)
    OP_28(0x32, 0x1, 0x800)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(10180, 0, 201880, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 10180, 0, 201880, 270)
    SetChrPos(0x1, 10180, 0, 201880, 270)
    SetChrPos(0x2, 10180, 0, 201880, 270)
    SetChrPos(0x3, 10180, 0, 201880, 270)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_11_178C end

    def Function_12_1C60(): pass

    label("Function_12_1C60")

    OP_8E(0xFE, 0x13E2, 0x0, 0x31286, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_12_1C60 end

    def Function_13_1C84(): pass

    label("Function_13_1C84")

    OP_8E(0xFE, 0x139C, 0x0, 0x318DA, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_13_1C84 end

    def Function_14_1CA8(): pass

    label("Function_14_1CA8")

    OP_8E(0xFE, 0xD66, 0x0, 0x31128, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_14_1CA8 end

    def Function_15_1CCC(): pass

    label("Function_15_1CCC")

    OP_8E(0xFE, 0xDCA, 0x0, 0x31916, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_15_1CCC end

    def Function_16_1CF0(): pass

    label("Function_16_1CF0")

    PlayEffect(0x1, 0x3, 0xFF, 11420, 100, 201870, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x3, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_16_1CF0 end

    def Function_17_1D45(): pass

    label("Function_17_1D45")

    PlayEffect(0x1, 0x4, 0xFF, 14000, 0, 203770, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_1D80():

        label("loc_1D80")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1D80")

    QueueWorkItem2(0xFE, 3, lambda_1D80)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_17_1D45 end

    def Function_18_1DAD(): pass

    label("Function_18_1DAD")

    PlayEffect(0x1, 0x5, 0xFF, 14000, 0, 199870, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_1DE8():

        label("loc_1DE8")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1DE8")

    QueueWorkItem2(0xFE, 3, lambda_1DE8)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_18_1DAD end

    def Function_19_1E15(): pass

    label("Function_19_1E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE4")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0xA9, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0xAA, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0xAC, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(3072)
    Sleep(500)
    Jump("loc_1EE7")

    label("loc_1EE4")

    TalkBegin(0xFF)

    label("loc_1EE7")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #29
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2066")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F7F"),
        (1, "loc_1FFA"),
        (2, "loc_2028"),
        (SWITCH_DEFAULT, "loc_2056"),
    )


    label("loc_1F7F")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE9)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2063")

    label("loc_1FFA")

    OP_A9(0x1E)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #30
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_2063")

    label("loc_2028")

    OP_A9(0x6)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #31
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_2063")

    label("loc_2056")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2063")

    label("loc_2063")

    Jump("loc_1F23")

    label("loc_2066")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2093")
    OP_A2(0x258F)
    EventEnd(0x1)
    Jump("loc_2096")

    label("loc_2093")

    TalkEnd(0xFF)

    label("loc_2096")

    SetMapFlags(0x100000)
    Return()

    # Function_19_1E15 end

    def Function_20_209C(): pass

    label("Function_20_209C")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #32
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_209C end

    def Function_21_20EB(): pass

    label("Function_21_20EB")

    ClearMapFlags(0x2000000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_210E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_211F")

    label("loc_210E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_211F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_211F")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2144"),
        (1, "loc_2173"),
        (2, "loc_21A2"),
        (SWITCH_DEFAULT, "loc_21D1"),
    )


    label("loc_2144")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP001._CH")
    Jump("loc_21D1")

    label("loc_2173")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP002._CH")
    Jump("loc_21D1")

    label("loc_21A2")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP003._CH")
    Jump("loc_21D1")

    label("loc_21D1")

    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2206")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_250B")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2231"),
        (1, "loc_225D"),
        (2, "loc_229E"),
        (SWITCH_DEFAULT, "loc_22F2"),
    )


    label("loc_2231")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",          # 0
            "[Balstar Channel]\x01",      # 1
        )
    )

    Jump("loc_22F2")

    label("loc_225D")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",             # 0
            "[Balstar Channel]\x01",         # 1
            "[Saint-Croix Forest]\x01",      # 2
        )
    )

    Jump("loc_22F2")

    label("loc_229E")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",             # 0
            "[Balstar Channel]\x01",         # 1
            "[Saint-Croix Forest]\x01",      # 2
            "[Grimsel Fortress]\x01",        # 3
        )
    )

    Jump("loc_22F2")

    label("loc_22F2")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_231C"),
        (1, "loc_2393"),
        (2, "loc_240E"),
        (3, "loc_248C"),
        (SWITCH_DEFAULT, "loc_2508"),
    )


    label("loc_231C")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #33
        "\x07\x05Travel to [Guild Lodge]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2380"),
        (1, "loc_238D"),
        (SWITCH_DEFAULT, "loc_2390"),
    )


    label("loc_2380")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2390")

    label("loc_238D")

    Jump("loc_2390")

    label("loc_2390")

    Jump("loc_2508")

    label("loc_2393")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #34
        "\x07\x05Travel to [Balstar Channel]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23FB"),
        (1, "loc_2408"),
        (SWITCH_DEFAULT, "loc_240B"),
    )


    label("loc_23FB")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_240B")

    label("loc_2408")

    Jump("loc_240B")

    label("loc_240B")

    Jump("loc_2508")

    label("loc_240E")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #35
        "\x07\x05Travel to [Saint-Croix Forest]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2479"),
        (1, "loc_2486"),
        (SWITCH_DEFAULT, "loc_2489"),
    )


    label("loc_2479")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2489")

    label("loc_2486")

    Jump("loc_2489")

    label("loc_2489")

    Jump("loc_2508")

    label("loc_248C")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #36
        "\x07\x05Travel to [Grimsel Fortress]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24F5"),
        (1, "loc_2502"),
        (SWITCH_DEFAULT, "loc_2505"),
    )


    label("loc_24F5")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2505")

    label("loc_2502")

    Jump("loc_2505")

    label("loc_2505")

    Jump("loc_2508")

    label("loc_2508")

    Jump("loc_2206")

    label("loc_250B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2524"),
        (1, "loc_2558"),
        (2, "loc_258C"),
        (3, "loc_25C0"),
        (SWITCH_DEFAULT, "loc_25F4"),
    )


    label("loc_2524")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_25F4")

    label("loc_2558")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_25F4")

    label("loc_258C")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_25F4")

    label("loc_25C0")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_25F4")

    label("loc_25F4")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapFlags(0x100000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_261B"),
        (1, "loc_263B"),
        (2, "loc_2647"),
        (3, "loc_2653"),
        (SWITCH_DEFAULT, "loc_265F"),
    )


    label("loc_261B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262F")
    NewScene("ED6_DT21/U5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2638")

    label("loc_262F")

    NewScene("ED6_DT21/U5102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2638")

    Jump("loc_265F")

    label("loc_263B")

    NewScene("ED6_DT21/M5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_265F")

    label("loc_2647")

    NewScene("ED6_DT21/M5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_265F")

    label("loc_2653")

    NewScene("ED6_DT21/M5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_265F")

    label("loc_265F")

    Return()

    # Function_21_20EB end

    SaveToFile()

Try(main)
