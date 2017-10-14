from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2601   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2601.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        'Card',                                 # 9
        'Academy - Back Road',                  # 10
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
        'ED6_DT06/CH20021 ._CH',             # 00
        'ED6_DT27/CH03005 ._CH',             # 01
        'ED6_DT26/CH20311 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT06/CH20021P._CP',             # 00
        'ED6_DT27/CH03005P._CP',             # 01
        'ED6_DT26/CH20311P._CP',             # 02
    )

    DeclNpc(
        X                   = 0,
        Z                   = 1000,
        Y                   = 8450,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589824,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 170,
        Z                   = 0,
        Y                   = -16239,
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


    DeclActor(
        TriggerX            = 24940,
        TriggerZ            = 5000,
        TriggerY            = 24830,
        TriggerRange        = 800,
        ActorX              = 24940,
        ActorZ              = 5000,
        ActorY              = 24830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33200,
        TriggerZ            = 0,
        TriggerY            = 14520,
        TriggerRange        = 1000,
        ActorX              = 32570,
        ActorZ              = 0,
        ActorY              = 14530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_16B",          # 01, 1
        "Function_2_1A7",          # 02, 2
        "Function_3_2F2",          # 03, 3
        "Function_4_DF6",          # 04, 4
        "Function_5_E0B",          # 05, 5
        "Function_6_E27",          # 06, 6
        "Function_7_E57",          # 07, 7
        "Function_8_E6C",          # 08, 8
        "Function_9_E9C",          # 09, 9
        "Function_10_135A",        # 0A, 10
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_156"),
        (SWITCH_DEFAULT, "loc_16A"),
    )


    label("loc_156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_167")

    Jump("loc_16A")

    label("loc_16A")

    Return()

    # Function_0_14A end

    def Function_1_16B(): pass

    label("Function_1_16B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x268, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D")
    OP_6F(0x2, 0)
    Jump("loc_184")

    label("loc_17D")

    OP_6F(0x2, 60)

    label("loc_184")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE61F0, 0x23004E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A6")
    OP_64(0x0, 0x1)

    label("loc_1A6")

    Return()

    # Function_1_16B end

    def Function_2_1A7(): pass

    label("Function_2_1A7")

    OP_EA(0x2, 0xFD, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x268, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    AddSepith(0x0, 0xA)
    AddSepith(0x1, 0xA)
    AddSepith(0x2, 0xA)
    AddSepith(0x3, 0xA)
    AddSepith(0x4, 0xA)
    AddSepith(0x5, 0xA)
    AddSepith(0x6, 0xA)
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
            "#61IMirage Sepith x10#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1340)
    Jump("loc_2E0")

    label("loc_29D")


    AnonymousTalk(    #1
        "\x07\x05I hope you washed your hands if you're going to double-dip.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2E0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1A7 end

    def Function_3_2F2(): pass

    label("Function_3_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_303")
    Call(0, 10)

    label("loc_303")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrPos(0x101, 210, 0, -7580, 0)
    SetChrPos(0x105, 940, 0, -9530, 0)
    SetChrPos(0xF7, -1100, 0, -10140, 0)
    SetChrPos(0x104, 800, 0, -11070, 0)
    SetChrPos(0x127, -680, 0, -11530, 0)
    OP_6D(340, 1000, 10340, 0)
    OP_67(0, 9440, -10000, 0)
    OP_6B(6060, 0)
    OP_6C(36000, 0)
    OP_6E(262, 0)
    StopSound(0x9470, 0x2BF20, 0x0)
    OP_72(0x3, 0x4)
    OP_C8(0x200, 0x46, "C_PLAC07._CH", 0x0, 0x7D0)
    OP_DE("Old Schoolhouse")
    FadeToBright(2000, 0)

    def lambda_3E3():
        OP_6D(350, 0, 2160, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E3)

    def lambda_3FB():
        OP_67(0, 9440, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3FB)

    def lambda_413():
        OP_8E(0xFE, 0x46A, 0x0, 0x4F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_413)
    Sleep(200)

    def lambda_433():
        OP_8E(0xFE, 0xFFFFFD58, 0x0, 0xFFFFFFEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_433)
    Sleep(200)

    def lambda_453():
        OP_8E(0xFE, 0x49C, 0x0, 0xFFFFFE7A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_453)

    def lambda_46E():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0xFFFFFBD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_46E)
    Sleep(200)

    def lambda_48E():
        OP_8E(0xFE, 0xD2, 0x0, 0x6E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48E)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x127, 0x1)
    Fade(1000)
    OP_6D(210, 0, 1760, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_531")

    ChrTalk(    #2
        0x106,
        "#057F#5PSo this is the old schoolhouse, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_57D")

    label("loc_531")


    ChrTalk(    #3
        0x103,
        (
            "#027F#5PSo this is the old schoolhouse.\x01",
            "Appropriately spooky, I think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57D")


    ChrTalk(    #4
        0x104,
        (
            "#031F#4PHeheh... Now we're getting somewhere.\x02\x03",

            "I can feel my blood begin to\x01",
            "sing with the terror of it all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x127,
        "#151FHee, I'm getting gooooosebumps!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x127, 400)

    ChrTalk(    #6
        0x101,
        (
            "#1019FYeah, you two sure seem terrified,\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x105,
        "#044FOh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #8
        0x101,
        "#1004FWhat's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x105,
        "#043FEstelle, on the door...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    def lambda_6EC():
        OP_6D(0, 1000, 8010, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_6EC)

    def lambda_704():
        OP_67(0, 8000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_704)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x0, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_742():
        OP_6D(0, 1000, 9000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_742)

    def lambda_75A():
        OP_67(0, 8000, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_75A)
    OP_43(0x101, 0x1, 0x0, 0x4)
    Sleep(300)
    OP_43(0x105, 0x1, 0x0, 0x5)
    Sleep(200)
    OP_43(0xF7, 0x1, 0x0, 0x6)
    Sleep(200)
    OP_43(0x104, 0x1, 0x0, 0x7)
    Sleep(100)
    OP_43(0x127, 0x1, 0x0, 0x8)
    WaitChrThread(0x127, 0x1)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x0, 0x1)

    ChrTalk(    #10
        0x101,
        (
            "#1002F#6PThis is...a card? Great.\x02\x03",

            "Let's see what's written on it...\x02",
        )
    )

    CloseMessageWindow()
    OP_6B(2780, 1000)
    Fade(250)
    OP_71(0x3, 0x4)
    SetChrChipByIndex(0x101, 2)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05O uninvited wanderers,\x01",
            "welcome unto my transient abode.\x02\x03",

            "If you do not fear the curse of a thousand\x01",
            "years, then hasten to join me.\x02\x03",

            "The first curse is in the great room.\x01",
            "The hollow flame shall guide thee.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    LoadEffect(0x0, "map\\\\mpfire6.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -150, 1700, 9440, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x86, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(500)

    ChrTalk(    #12
        0x101,
        "#1K#1020F#3PWaah...!\x02",
    )


    ChrTalk(    #13
        0x105,
        "#1K#043F#4PEek!\x02",
    )

    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_9EB():
        OP_8F(0x105, 0x2BC, 0x3E8, 0x208A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9EB)
    OP_8F(0x101, 0xFFFFFF24, 0x3E8, 0x2116, 0x7D0, 0x0)
    Sleep(500)
    OP_56(0x1)
    OP_59()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #14
        "\x07\x05The card was engulfed in flame and burned away.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A9F")

    ChrTalk(    #15
        0x106,
        "#055F#5PWhat the hell?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_ABD")

    label("loc_A9F")


    ChrTalk(    #16
        0x103,
        "#023F#5PBy the Goddess?!\x02",
    )

    CloseMessageWindow()

    label("loc_ABD")


    ChrTalk(    #17
        0x127,
        (
            "#154F#5POooooh, maybe it's spontaneous\x01",
            "combustion!\x02\x03",

            "I've heard that happens with\x01",
            "spooooky poltergeists...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x104,
        (
            "#035F#2PHeh... What a provocative little\x01",
            "ghost we have.\x02\x03",

            "Attempting to riddle us, is he?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x101,
        (
            "#1005F#6POoooh! It's ON now!\x02\x03",

            "I'll teach him not to mess\x01",
            "with real, living people!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CAA")

    ChrTalk(    #20
        0x106,
        (
            "#5P#051FWell, long as you can keep the\x01",
            "bravery up, we'll be okay.\x02\x03",

            "#053FBut...'the hollow flame shall guide thee'...\x01",
            "The hell does that mean...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3A")

    label("loc_CAA")


    ChrTalk(    #21
        0x103,
        (
            "#5P#020FAs long as you can keep that\x01",
            "brave face on, we'll be okay.\x02\x03",

            "#026FThe riddle, though...\x01",
            "'The hollow flame shall guide thee.'\x01",
            "Hmm...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3A")

    TurnDirection(0x105, 0x101, 400)
    Sleep(400)

    ChrTalk(    #22
        0x105,
        (
            "#042F#4PI'd be willing to guess the 'great room'\x01",
            "is the big entry hall just beyond.\x02\x03",

            "We'll need to investigate it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #23
        0x101,
        "#1002F#6PRight! C'mon...!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1224)
    OP_28(0x84, 0x1, 0x1)
    OP_28(0x84, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_3_2F2 end

    def Function_4_DF6(): pass

    label("Function_4_DF6")

    OP_8E(0xFE, 0xFFFFFF10, 0x3E8, 0x2328, 0x1388, 0x0)
    Return()

    # Function_4_DF6 end

    def Function_5_E0B(): pass

    label("Function_5_E0B")

    OP_8E(0xFE, 0x26C, 0x3E8, 0x20DA, 0x1388, 0x0)
    OP_8C(0xFE, 327, 400)
    Return()

    # Function_5_E0B end

    def Function_6_E27(): pass

    label("Function_6_E27")

    OP_8E(0xFE, 0xFFFFFC40, 0x3E8, 0x1900, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFF876, 0x3E8, 0x1F2C, 0x1388, 0x0)
    OP_8C(0xFE, 42, 400)
    Return()

    # Function_6_E27 end

    def Function_7_E57(): pass

    label("Function_7_E57")

    OP_8E(0xFE, 0xFFFFFE98, 0x3E8, 0x19FA, 0x1388, 0x0)
    Return()

    # Function_7_E57 end

    def Function_8_E6C(): pass

    label("Function_8_E6C")

    OP_8E(0xFE, 0xFFFFFC40, 0x3E8, 0x1900, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFF8DA, 0x3E8, 0x1A9A, 0x1388, 0x0)
    OP_8C(0xFE, 30, 400)
    Return()

    # Function_8_E6C end

    def Function_9_E9C(): pass

    label("Function_9_E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB6")
    Call(0, 10)
    FadeToBright(0, 0)

    label("loc_EB6")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 23920, 5000, 25980, 135)
    SetChrPos(0xF7, 24140, 5000, 24250, 104)
    SetChrPos(0x105, 25000, 5000, 26400, 180)
    SetChrPos(0x104, 26660, 5000, 24580, 261)
    SetChrPos(0x127, 25940, 5000, 23050, 345)
    OP_6D(23920, 5000, 25980, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #24
        0x105,
        (
            "#040F#4PA 'fallen neck' in the 'garden'...\x02\x03",

            "This matches the requirements,\x01",
            "in a way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1006FYeah, this looks like it. Look...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05The stone planter held a card and an old key.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x101, 2)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_AD(0x240096, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "\x07\x05Now thine curse is realized. Overcome\x01",
            "the final trial, and stand before me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    LoadEffect(0x0, "map\\\\mpfire6.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 24440, 5900, 25460, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0x86, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #28
        "\x07\x05The card burst into flames.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #29
        "\x07\x00Received #1012i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x3F4, 1)

    ChrTalk(    #30
        0x101,
        (
            "#1007FThat's the end of the riddles,\x01",
            "I think. I hope.\x02\x03",

            "#1019FI hope 'thine curse is realized'\x01",
            "is just a metaphor, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x104,
        (
            "#035FHeh, regardless, he wishes us\x01",
            "to use the key.\x02\x03",

            "#030FLet's find a lock it might open!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(23920, 5000, 25980, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 23920, 5000, 25980, 135)
    SetChrPos(0xF7, 23920, 5000, 25980, 135)
    SetChrPos(0x105, 23920, 5000, 25980, 135)
    SetChrPos(0x104, 23920, 5000, 25980, 135)
    SetChrPos(0x127, 23920, 5000, 25980, 135)
    OP_64(0x0, 0x1)
    OP_A2(0x1227)
    OP_28(0x84, 0x1, 0x10)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_E9C end

    def Function_10_135A(): pass

    label("Function_10_135A")

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
        (0, "loc_13D3"),
        (1, "loc_13D9"),
        (SWITCH_DEFAULT, "loc_13DF"),
    )


    label("loc_13D3")

    OP_A2(0x1200)
    Jump("loc_13DF")

    label("loc_13D9")

    OP_A2(0x1201)
    Jump("loc_13DF")

    label("loc_13DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_13ED")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_13F1")

    label("loc_13ED")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_13F1")

    Return()

    # Function_10_135A end

    SaveToFile()

Try(main)
